import csv
import platform
import sys
from pathlib import Path
from pprint import pprint

from airtest.core.api import *
import torch

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from ultralytics.utils.plotting import Annotator, colors, save_one_box

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.torch_utils import select_device, smart_inference_mode


def run(
        model,
        weights=ROOT / 'yolov5s.pt',  # model path or triton URL
        source=ROOT / 'data/images',  # file/dir/URL/glob/screen/0(webcam)
        data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
        imgsz=(640, 640),  # inference size (height, width)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        max_det=1000,  # maximum detections per image
        device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        view_img=False,  # show results
        save_txt=False,  # save results to *.txt
        save_csv=False,  # save results in CSV format
        save_conf=False,  # save confidences in --save-txt labels
        save_crop=False,  # save cropped prediction boxes
        nosave=False,  # do not save images/videos
        classes=None,  # filter by class: --class 0, or --class 0 2 3
        agnostic_nms=False,  # class-agnostic NMS
        augment=False,  # augmented inference
        visualize=False,  # visualize features
        update=False,  # update all models
        project=ROOT / 'runs/detect',  # save results to project/name
        name='exp',  # save results to project/name
        exist_ok=False,  # existing project/name ok, do not increment
        line_thickness=1,  # bounding box thickness (pixels)
        hide_labels=False,  # hide labels
        hide_conf=False,  # hide confidences
        half=False,  # use FP16 half-precision inference
        dnn=False,  # use OpenCV DNN for ONNX inference
        vid_stride=1,  # video frame-rate stride
):
    sourcXe = str(source)
    save_img = not nosave and not source.endswith('.txt')  # save inference images
    is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)

    screenshot = source.lower().startswith('screen')

    # Directories
    save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # 加载模型这一段封装出去
    # Load model
    # device = select_device(device)
    # model = load_my_model(weights, device=device, dnn=dnn, data=data, half=half)
    stride, names, pt = model.stride, model.names, model.pt
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    # Dataloader
    bs = 1  # batch_size

    if screenshot:
        dataset = LoadScreenshots(source, img_size=imgsz, stride=stride, auto=pt)
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=vid_stride)

    # Run inference
    model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
    seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
    result = []

    for path, im, im0s, vid_cap, s in dataset:
        with dt[0]:
            im = torch.from_numpy(im).to(model.device)
            im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim

        # Inference
        with dt[1]:
            visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
            pred = model(im, augment=augment, visualize=visualize)
        # NMS
        with dt[2]:
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)

        # Process predictions
        for i, det in enumerate(pred):  # per image
            seen += 1
            p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)
            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # im.jpg
            s += '%gx%g ' % im.shape[2:]  # print string
            imc = im0.copy() if save_crop else im0  # for save_crop
            annotator = Annotator(im0, line_width=line_thickness, example=str(names))
            if len(det):
                # 将盒子从img大小缩放到im0大小
                det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, 5].unique():
                    n = (det[:, 5] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    c = int(cls)  # integer class
                    label = names[c] if hide_conf else f'{names[c]}'
                    confidence = float(conf)
                    confidence_str = f'{confidence:.2f}'
                    list_from_tensors = [tensor.item() for tensor in xyxy]
                    ## 新增代码，转化可理解的结果
                    dict_dt = {"label": label, "rectangle": list_from_tensors, "confidence": confidence}
                    result.append(dict_dt)

                    if save_img or save_crop or view_img:  # Add bbox to image
                        c = int(cls)  # integer class
                        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                        annotator.box_label(xyxy, label, color=colors(c, True))
                    if save_crop:
                        save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)

            # Stream results
            im0 = annotator.result()
            if view_img:
                if platform.system() == 'Linux' and p not in windows:
                    windows.append(p)
                    cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                    cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                cv2.imshow(str(p), im0)
                cv2.waitKey(1)  # 1 millisecond

            # Save results (image with detections)
            if save_img:
                if dataset.mode == 'image':
                    cv2.imwrite(save_path, im0)
                else:  # 'video' or 'stream'
                    LOGGER.warning("不支持除image模式外的其他模式")
                    pass

        # Print time (inference-only)
        # image 1/1 D:\Y_PythonProject\yolo_target_detection\yolov5\MyData\test1\20231201172908.jpg: 448x960 2 cashs, 2 closes, 222.9ms
        LOGGER.info(f"{s}{'' if len(det) else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")

    # Print results
    t = tuple(x.t / seen * 1E3 for x in dt)  # speeds per image
    LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *imgsz)}' % t)
    if save_txt or save_img:
        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
        LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")
    if update:
        strip_optimizer(weights[0])  # update model (to fix SourceChangeWarning)

    return result


# 加载模型
@smart_inference_mode()
def load_my_model(weights=None, device=None, dnn=False, data=ROOT / 'data/coco128.yaml', half=False):
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data, fp16=half)
    return model


class RunDetect:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RunDetect, cls).__new__(cls)
            # 以下是您希望仅执行一次的初始化代码
            # 例如：模型加载
            cls._instance.model = load_my_model(**kwargs)
        return cls._instance

    def __init__(self, **kwargs):
        # __init__ 可能会在每次对象创建时被调用，
        # 但是实际的初始化只需要在 __new__ 方法中进行一次。
        # 这里可以添加其他的初始化代码，如果它们需要在每次对象创建时执行
        pass


def predictor(**kwargs):
    """
    Args:
        weights：是训练后的权重文件，默认值best3.pt
        source :预测对象，必填，可以是图片路径，也可以是 numpy.ndarray 类型的图像数据
        data ：是要预测的类别的配置文件，有默认值
        imgsz :[640, 640] 输入图像数据的尺度，可选参数 是32的倍数 ，320 640，960,1024,1056
        conf_thres: 置信度阈值，默认值 0.25
        iou_thres:NMS（非极大值抑制）的 IOU（交并比）阈值。默认值 `0.45` 表示在执行 NMS 时，两个框的 IOU 必须小于 `0.45` 才能被认为是不重叠的
        max_det: 最大检测数量，默认值 20
        device:用于推理的 CUDA 设备，可以是数字（如 `0` 或 `0,1,2,3`）或 `'cpu'`。默认值为 CPU。
        nosave ：有默认值，默认值为True,可选值为True,False,为True时，会把预测结果存到project参数下，project为目录
        classes:是否过滤检测结果。默认值 `None` 表示不过滤。
        augment: True,  # 是否使用增加数据推理
        project：有默认值，是目录数据，sting 类型,默认值 `ROOT / 'runs/detect'` 表示结果保存在 `detect` 文件夹下。
        line_thickness: 边界框的厚度（像素）。默认值1像素。

    Returns:

    """

    ks = {
        # "weights": kwargs.get("weights", ROOT / 'best3.pt'),
        "weights": kwargs.get("weights", ROOT / "weights/mydetect.pt"),
        "source": kwargs.get("source"),
        "data": kwargs.get('data', ROOT / 'data/myyolov5s.yaml'),
        "imgsz": kwargs.get('imgsz', 640),
        "conf_thres": kwargs.get('conf_thres', 0.25),
        "iou_thres": kwargs.get('iou_thres', 0.45),
        "max_det": kwargs.get('max_det', 20),
        "device": kwargs.get('device', ''),
        "view_img": kwargs.get('view_img', False),
        "save_txt": kwargs.get('save_txt', False),
        "save_csv": kwargs.get('save_csv', False),
        "save_conf": kwargs.get('save_conf', False),
        "save_crop": kwargs.get('save_crop', False),
        "nosave": kwargs.get('nosave', True),
        "classes": kwargs.get('classes', None),
        "agnostic_nms": kwargs.get('agnostic_nms', False),
        "augment": kwargs.get('augment', True),
        "visualize": kwargs.get('visualize', False),
        "update": kwargs.get('update', False),
        "project": kwargs.get('project', ROOT / 'runs/detect'),
        "name": kwargs.get('name', 'exp'),
        "exist_ok": kwargs.get('exist_ok', False),
        "line_thickness": kwargs.get('line_thickness', 1),
        "hide_labels": kwargs.get('hide_labels', False),
        "hide_conf": kwargs.get('hide_conf', False),
        "half": kwargs.get('half', False),
        "dnn": kwargs.get('dnn', False),
        "vid_stride": kwargs.get('vid_stride', 1),
    }

    ks_model = {
        "weights": ks.get("weights"),
        # "device": ks.get("device"),
        "dnn": ks.get("dnn"),
        "data": ks.get("data"),
        "half": ks.get("half"),
    }

    my_model = RunDetect(**ks_model).model
    ks["model"] = my_model
    res = run(**ks)
    if res:
        pred = []
        reversed_list = list(reversed(res))
        for ps in reversed_list:
            box = ps.get('rectangle')
            xmin = box[0]
            ymin = box[1]
            xmax = box[2]
            ymax = box[3]
            posx = (xmax - xmin) / 2 + xmin
            posy = (ymax - ymin) / 2 + ymin
            pos = (int(posx), int(posy))
            key_value_list = list(ps.items())
            key_value_list.insert(1, ('result', pos))
            my_dict = dict(key_value_list)
            pred.append(my_dict)
        return pred
    else:
        return False


if __name__ == '__main__':
    # opt = parse_opt()
    # main(opt)
    # import cv2
    # import numpy as np
    # devices= "BH9504LNDQ"
    # connect_device('android://127.0.0.1:5037/{}?'.format(devices))
    # screen = G.DEVICE.snapshot(quality=99)
    # res = predictor(source=screen,imgsz=960,save =True,project =r'D:\Demoheji\touping')
    for i in range(1):
        img = r"D:\Y_PythonProject\yolo_target_detection\yolov5\MyData\test1\20231201173523.jpg"
        kw = {
            "weights": "weights/mydetect.pt",
            "source": img,
            "data": "data\myyolov5s.yaml",
            "imgsz": [960, 960],
            "conf_thres": 0.25,
            "iou_thres": 0.45,
            "max_det": 20,
            "device": "gpu",
            "nosave": False,  # 是否不保存结果图片
            "classes": None,
            "augment": True,  # 是否使用增加数据推理
            "project": "runs\detect",
            "name": "exp",
            "line_thickness": 1,
        }

        start_time = time.time()
        res = predictor(**kw)
        print("===================")
        pprint(res)
        # #
        # for t in res:
        #     print(t)
        #     if t.get("label") =='menu':
        #         pos = t.get("result")
        #         # click(pos)
        end_time = time.time()
        print("耗时:", end_time - start_time)
