import datetime
import time

import cv2
from airtest.aircv import cv2
from airtest.aircv.cal_confidence import cal_ccoeff_confidence
from airtest.core.api import Template
from File import bbs
bbs = bbs()
from airtest.core.api import *

# bbs.scan_for_images('cashhoard','R28M405TJBX','alert','tpl1599189033537.png')

# print(bbs.scan_for_images('mania','R28M405TJBX','home','tpl1750322700081.png'))

import numpy as np

from collections import defaultdict


def save_blocks_to_directory(blocks, output_dir="screen_blocks"):
    """
    保存所有区块到指定目录
    :param blocks: get_dot_by_color()返回的区块列表
    :param output_dir: 输出目录路径
    :return: 保存的文件路径列表
    """
    # 创建目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)

    saved_files = []
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    for idx, block in enumerate(blocks):
        # 生成文件名：时间戳_行列位置.png
        # filename = f"block_{timestamp}_{block['position'][0]}x{block['position'][1]}.png"
        filename = f"{idx}.png"
        filepath = os.path.join(output_dir, filename)

        # 保存图像（假设block['image']是numpy数组）
        cv2.imwrite(filepath, block['image'])
        saved_files.append(filepath)


        most_common_color = get_dominant_color(block['image'])

        # avg_color = tuple(np.mean(block_rgb, axis=(0, 1)))

        print(f"提取{idx}的颜色:", most_common_color)

    print(f"已保存 {len(saved_files)} 个区块到目录: {os.path.abspath(output_dir)}")
    return saved_files


def get_most_common_color(block):
    pixels = block.reshape(-1, 3)
    color_counts = defaultdict(int)
    for pixel in pixels:
        color_counts[tuple(pixel)] += 1
    return max(color_counts.items(), key=lambda x: x[1])[0]

def get_dominant_color(block, bin_size=10, ignore_colors=None):
    """
    综合优化版：量化颜色 + 过滤背景
    :param block: 输入图像区块 (numpy数组)
    :param bin_size: 颜色量化粒度 (建议10-20)
    :param ignore_colors: 要忽略的背景色列表
    """
    ignore_colors = ignore_colors or []
    pixels = block.reshape(-1, 3)

    # 颜色量化 + 过滤
    quantized = (pixels // bin_size) * bin_size
    filtered = [p for p in quantized if tuple(p) not in ignore_colors]
    if not filtered:
        filtered = quantized

    # 统计众数
    color_counts = defaultdict(int)
    for pixel in filtered:
        color_counts[tuple(pixel)] += 1
    return max(color_counts.items(), key=lambda x: x[1])[0]

def get_dot_by_colorbak(block_width,block_height):
    # 获取设备分辨率并截屏
    screen_width, screen_height = G.DEVICE.get_current_resolution()
    print(f"屏幕分辨率: {screen_width}x{screen_height}")
    screen = G.DEVICE.snapshot()  # 假设返回的是numpy数组或PIL Image

    # 转换为numpy数组统一处理
    if not isinstance(screen, np.ndarray):
        screen = np.array(screen)

    # 计算分割块数（向下取整）
    cols = screen_width // block_width
    rows = screen_height // block_height

    print(f"将分割为 {rows}行 x {cols}列 的区块")

    # 存储所有分割块
    blocks = []

    # 有序分割（从左到右，从上到下）
    for y in range(rows):
        for x in range(cols):
            # 计算当前块的像素范围
            x_start = x * block_width
            y_start = y * block_height
            x_end = (x + 1) * block_width
            y_end = (y + 1) * block_height

            # 提取区块
            block = screen[y_start:y_end, x_start:x_end]

            avg_color = tuple(np.mean(block, axis=(0, 1)))

            print("实际颜色", avg_color)
            blocks.append({
                "position": (x, y),  # 区块坐标(列,行)
                "rectangle": (x_start, y_start, x_end, y_end),  # 像素范围
                "coordinate": ((x_start + x_end) // 2, (y_start + y_end) // 2),
                "image": block  # 图像数据
            })



    return blocks


def _ensure_rgb(image):
    """强制转换任何图像格式到RGB numpy数组"""
    if isinstance(image, np.ndarray):
        if image.shape[2] == 3:  # 已经是3通道
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB) if _is_bgr(image) else image
        elif image.shape[2] == 4:  # 处理RGBA
            return cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    else:  # PIL Image或其他
        return np.array(image.convert('RGB'))


def _is_bgr(image):
    """启发式判断是否是BGR格式（OpenCV默认）"""
    # 方法1：检查红色通道是否在最后一个维度（经验性判断）
    return image[0, 0, 0] > image[0, 0, 2]  # 如果B>R可能是BGR


def get_dominant_color_rgb(block_rgb, bin_size=10):
    """
    直接处理RGB区块的众数颜色（无需BGR转换）
    :param block_rgb: RGB格式的图像区块
    :param bin_size: 颜色量化粒度
    """
    pixels = block_rgb.reshape(-1, 3)
    quantized = (pixels // bin_size) * bin_size
    color_counts = defaultdict(int)
    for pixel in quantized:
        color_counts[tuple(pixel)] += 1
    return max(color_counts.items(), key=lambda x: x[1])[0]

def get_dot_by_color(block_width,block_height):
    # 获取设备分辨率并截屏
    screen_width, screen_height = G.DEVICE.get_current_resolution()
    print(f"屏幕分辨率: {screen_width}x{screen_height}")
    screen = G.DEVICE.snapshot()  # 假设返回的是numpy数组或PIL Image

    # 转换为numpy数组统一处理
    if not isinstance(screen, np.ndarray):
        screen = np.array(screen)

    # 计算分割块数（向下取整）
    cols = screen_width // block_width
    rows = screen_height // block_height

    print(f"将分割为 {rows}行 x {cols}列 的区块")

    # 存储所有分割块
    blocks = []

    # 有序分割（从左到右，从上到下）
    for y in range(rows):
        for x in range(cols):
            # 计算当前块的像素范围
            x_start = x * block_width
            y_start = y * block_height
            x_end = (x + 1) * block_width
            y_end = (y + 1) * block_height

            # 提取区块
            block = screen[y_start:y_end, x_start:x_end]

            # avg_color = tuple(np.mean(block, axis=(0, 1)))
            # median_color = tuple(np.median(block, axis=(0, 1)))  # 对R/G/B通道分别取中位数
            block_rgb = cv2.cvtColor(block, cv2.COLOR_RGB2BGR)
            most_common_color = get_dominant_color(block_rgb)  # 返回出现次数最多的颜色
            # print("实际颜色", most_common_color)
            blocks.append({
                "position": (x, y),  # 区块坐标(列,行)
                "rectangle": (x_start, y_start, x_end, y_end),  # 像素范围
                "coordinate": ((x_start + x_end) // 2, (y_start + y_end) // 2),
                "color":most_common_color,
                # "image": block  # 图像数据
            })

    quadrants = {
        "top_left": [],
        "top_right": [],
        "bottom_left": [],
        "bottom_right": []
    }

    for item in blocks:
        x, y = item['coordinate']
        # print("坐标数据", (x, y))
        quadrant = ("top" if y < screen_height / 2 else "bottom") + \
                   ("_left" if x < screen_width / 2 else "_right")
        quadrants[quadrant].append(item)

    return quadrants

def get_dotall_by_color(block_width,block_height):
    # 获取设备分辨率并截屏
    screen_width, screen_height = G.DEVICE.get_current_resolution()
    print(f"屏幕分辨率: {screen_width}x{screen_height}")
    screen = G.DEVICE.snapshot()  # 假设返回的是numpy数组或PIL Image
    # 强制转换截图到RGB（无论输入是PIL/OpenCV/numpy）
    # screen = _ensure_rgb(G.DEVICE.snapshot())
    # 转换为numpy数组统一处理
    if not isinstance(screen, np.ndarray):
        screen = np.array(screen)

    # 计算分割块数（向下取整）
    cols = screen_width // block_width
    rows = screen_height // block_height

    print(f"将分割为 {rows}行 x {cols}列 的区块")

    # 存储所有分割块
    blocks = []

    # 有序分割（从左到右，从上到下）
    n =0
    for y in range(rows):
        for x in range(cols):
            n+=1
            # 计算当前块的像素范围
            x_start = x * block_width
            y_start = y * block_height
            x_end = (x + 1) * block_width
            y_end = (y + 1) * block_height

            # 提取区块
            block = screen[y_start:y_end, x_start:x_end]

            # avg_color = tuple(np.mean(block, axis=(0, 1)))
            # median_color = tuple(np.median(block, axis=(0, 1)))  # 对R/G/B通道分别取中位数
            # block_rgb = cv2.cvtColor(block, cv2.COLOR_RGB2BGR)
            most_common_color = get_dominant_color(block)  # 返回出现次数最多的颜色
            # print("实际颜色", most_common_color)
            blocks.append({
                "index":n,
                "position": (x, y),  # 区块坐标(列,行)
                "rectangle": (x_start, y_start, x_end, y_end),  # 像素范围
                "coordinate": ((x_start + x_end) // 2, (y_start + y_end) // 2),
                "color":most_common_color,
                "image": block  # 图像数据
            })

    quadrants = {
        "top_left": [],
        "top_right": [],
        "bottom_left": [],
        "bottom_right": []
    }

    for item in blocks:
        x, y = item['coordinate']
        # print("坐标数据", (x, y))
        quadrant = ("top" if y < screen_height / 2 else "bottom") + \
                   ("_left" if x < screen_width / 2 else "_right")
        quadrants[quadrant].append(item)

    return blocks

def get_dot_by_color2(block_width,block_height):
    # 获取设备分辨率并截屏
    screen_width, screen_height = G.DEVICE.get_current_resolution()
    print(f"屏幕分辨率: {screen_width}x{screen_height}")
    screen = G.DEVICE.snapshot()  # 假设返回的是numpy数组或PIL Image
    # 强制转换截图到RGB（无论输入是PIL/OpenCV/numpy）
    # screen = _ensure_rgb(G.DEVICE.snapshot())
    # 转换为numpy数组统一处理
    if not isinstance(screen, np.ndarray):
        screen = np.array(screen)

    # 计算分割块数（向下取整）
    cols = screen_width // block_width
    rows = screen_height // block_height

    print(f"将分割为 {rows}行 x {cols}列 的区块")

    # 存储所有分割块
    blocks = []

    # 有序分割（从左到右，从上到下）
    n =0
    for y in range(rows):
        for x in range(cols):
            n+=1
            # 计算当前块的像素范围
            x_start = x * block_width
            y_start = y * block_height
            x_end = (x + 1) * block_width
            y_end = (y + 1) * block_height

            # 提取区块
            block = screen[y_start:y_end, x_start:x_end]

            # avg_color = tuple(np.mean(block, axis=(0, 1)))
            # median_color = tuple(np.median(block, axis=(0, 1)))  # 对R/G/B通道分别取中位数
            # block_rgb = cv2.cvtColor(block, cv2.COLOR_RGB2BGR)
            most_common_color = get_dominant_color(block)  # 返回出现次数最多的颜色
            # print("实际颜色", most_common_color)
            blocks.append({
                "index":n,
                "position": (x, y),  # 区块坐标(列,行)
                "rectangle": (x_start, y_start, x_end, y_end),  # 像素范围
                "coordinate": ((x_start + x_end) // 2, (y_start + y_end) // 2),
                "color":most_common_color,
                "image": block  # 图像数据
            })

    quadrants = {
        "top_left": [],
        "top_right": [],
        "bottom_left": [],
        "bottom_right": []
    }

    for item in blocks:
        x, y = item['coordinate']
        # print("坐标数据", (x, y))
        quadrant = ("top" if y < screen_height / 2 else "bottom") + \
                   ("_left" if x < screen_width / 2 else "_right")
        quadrants[quadrant].append(item)

    return quadrants

def get_crop_by_block(block_rows=8, block_cols=8):
    """
    动态分割屏幕为 block_rows x block_cols 的网格，适配任意分辨率
    :param block_rows: 纵向分割数 (默认8行)
    :param block_cols: 横向分割数 (默认8列)
    :return: 分象限的区块字典
    """
    try:
        # 1. 获取设备分辨率并截屏
        screen_width, screen_height = G.DEVICE.get_current_resolution()
        print(f"屏幕分辨率: {screen_width}x{screen_height}")
        screen = G.DEVICE.snapshot()

        # 2. 统一转为numpy数组 (适配PIL/numpy)
        if not isinstance(screen, np.ndarray):
            screen = np.array(screen)
            if screen.ndim == 3 and screen.shape[2] == 4:  # 处理RGBA截图
                screen = screen[:, :, :3]  # 丢弃Alpha通道

        # 3. 动态计算区块大小 (向下取整)
        block_width = screen_width // block_cols
        block_height = screen_height // block_rows
        print(f"区块尺寸: {block_width}x{block_height}")

        # 4. 高斯模糊减少噪点 (可选)
        blurred = cv2.GaussianBlur(screen, (3, 3), 0)

        # 5. 分割区块
        blocks = []
        for y in range(block_rows):
            for x in range(block_cols):
                x_start = x * block_width
                y_start = y * block_height
                x_end = min((x + 1) * block_width, screen_width)  # 防越界
                y_end = min((y + 1) * block_height, screen_height)

                block = blurred[y_start:y_end, x_start:x_end]

                block_bgr = cv2.cvtColor(block, cv2.COLOR_RGB2BGR)  # 假设设备截图是RGB
                most_common_color = get_dominant_color(block_bgr)

                blocks.append({
                    "position": (x, y),
                    "rectangle": (x_start, y_start, x_end, y_end),
                    "coordinate": ((x_start + x_end) // 2, (y_start + y_end) // 2),
                    "color": most_common_color,
                    "image": block
                })

        # 6. 分象限归类
        quadrants = {
            "top_left": [],
            "top_right": [],
            "bottom_left": [],
            "bottom_right": []
        }
        for block in blocks:
            x, y = block['coordinate']
            quadrant = ("top" if y < screen_height / 2 else "bottom") + \
                       ("_left" if x < screen_width / 2 else "_right")
            quadrants[quadrant].append(block)

        return quadrants

    except Exception as e:
        print(f"分割屏幕时出错: {e}")
        return {k: [] for k in ["top_left", "top_right", "bottom_left", "bottom_right"]}


def extract_color(crop_area, output_dir="extract_screen_blocks"):
    try:
        # 1. 获取截图
        screen = G.DEVICE.snapshot()
        # screen = _ensure_rgb(G.DEVICE.snapshot())
        print(f"截图尺寸: {screen.shape}")  # 检查截图是否有效
        # 2. 检查裁剪区域是否合法
        h, w = screen.shape[:2]
        x1, y1, x2, y2 = crop_area
        if x2 <= x1 or y2 <= y1 or x2 > w or y2 > h:
            raise ValueError(f"非法裁剪区域: {crop_area} (截图尺寸: {w}x{h})")

        # 3. 裁剪并转换颜色空间（假设截图是RGB）
        block = screen[y1:y2, x1:x2]

        # 4. 确保目录存在
        os.makedirs(output_dir, exist_ok=True)

        # 5. 保存文件
        filepath = os.path.join(output_dir, "extract.png")
        cv2.imwrite(filepath, block)
        print(f"图片已保存到: {filepath}")
        # 降噪，可忽略
        blurred = cv2.GaussianBlur(block, (3, 3), 0)
        # 6. 提取颜色

        most_common_color = get_dominant_color(blurred)

        # avg_color = tuple(np.mean(block_rgb, axis=(0, 1)))
        print("提取的颜色:", most_common_color)

    except Exception as e:
        print(f"错误: {e}")


def get_block_by_color(blocks, expected_rgb, tolerance=2):
    """
    tolerance  容忍差值
    :param blocks:
    :param expected_rgb:
    :param tolerance:
    :return:
    """
    target =[]
    for block in blocks:
        # if block['color'] == expected_rgb:
        #     print(block)
        #     df = abs(np.array(block['color']) - np.array(expected_rgb))
        #     print("差值",df)


        # res = all(abs(block['color'] - expected_rgb) < tolerance)
        res = all(abs( np.array(block['color']) - np.array(expected_rgb)) < tolerance)
        if res:
            # print(block)
            df = abs(np.array(block['color']) - np.array(expected_rgb))
            print("差值", df)
            # click(block['coordinate'])
            target.append(block)

        # if res:
        #     target.append(block)

    return target


def find_best_match1( project=None, file=None, confidence_threshold=0.80):

    template_paths = bbs.scan_for_images('mania', 'R28M405TJBX', 'home', )
    print("图片路径",template_paths)

    screen = G.DEVICE.snapshot()
    confidences = []

    for template_path in template_paths:
        try:
            template_img = cv2.imread(template_path)
            if template_img is None:
                print(f"警告: 无法读取图片 {template_path}")
                continue

            confidence = cal_ccoeff_confidence(screen, template_img)
            print(f"模板 {os.path.basename(template_path)} 置信度: {confidence:.2f}")
            confidences.append((confidence, template_path))

        except Exception as e:
            print(f"处理图片 {template_path} 时出错: {str(e)}")
            continue

    #这一步
    # 4. 分析结果
    # if not confidences:
    #     print("无有效匹配数据")
    #     return False

    print("confidences",confidences)

    max_confidence, best_template_path = max(confidences, key=lambda x: x[0])

    if max_confidence < confidence_threshold:
        print(f"未找到置信度≥{confidence_threshold}的匹配 (最高: {max_confidence:.2f})")
        return False

    print("best_template_path", best_template_path)

    template = Template(best_template_path, threshold= confidence_threshold)
    match_pos = template.match_in(screen)

    if match_pos:
        print(f"最佳匹配: {os.path.basename(best_template_path)}")
        print(f"坐标: {match_pos}, 置信度: {max_confidence:.2f}")
        return match_pos


    return []

def find_best_filter(project, devicefolder, dataset, confidence_threshold=0.80):

    template_paths =  bbs.scan_for_images(project, devicefolder, dataset )
    # print("图片路径",template_paths)

    screen_width, screen_height = G.DEVICE.get_current_resolution()

    # print("分辨率", (screen_width,screen_height))
    screen = G.DEVICE.snapshot()
    confidences = []

    for template_path in template_paths:
        try:
            template_img = cv2.imread(template_path)
            if template_img is None:
                print(f"警告: 无法读取图片 {template_path}")
                continue

            confidence = cal_ccoeff_confidence(screen, template_img)
            # print(f"模板 {os.path.basename(template_path)} 置信度: {confidence:.2f}")
            confidences.append((confidence, template_path))

        except Exception as e:
            print(f"处理图片 {template_path} 时出错: {str(e)}")
            continue

    # 4. 分析结果
    if not confidences:
        print("无有效匹配数据")
        return False

    # print("confidences",confidences)

    max_confidence, best_template_path = max(confidences, key=lambda x: x[0])
    best_template = []
    for item in confidences:
        confi,_ = item
        if confi > confidence_threshold:
            best_template.append(item)

    # print("best_template", best_template)
    if not best_template:
        print(f"未找到置信度≥{confidence_threshold}的匹配 (最高: {max_confidence:.2f})")
        return False

    # print("best_template_path", best_template_path)
    match_pos_list = []
    for template in best_template:

        _ ,best_template_path = template
        # print("best_template_path",best_template_path)
        template = Template(best_template_path, threshold= confidence_threshold ,resolution=(screen_width,screen_height) )
        match_pos = template.match_in(screen)
        # print(f"坐标: {match_pos}, 置信度: {max_confidence:.2f}")
        match_pos_list.append(match_pos)


    return match_pos_list

def find_best_match(project ,devicefolder , dataset, confidence_threshold=0.80):

    """
    直接模板匹配
    :param project:
    :param file:
    :param dataset:
    :param confidence_threshold:
    :return: []
    """
    screen_width, screen_height = G.DEVICE.get_current_resolution()
    screen = G.DEVICE.snapshot()


    if screen.size == 0:  # 正确检查numpy数组是否为空
        raise ValueError("获取的屏幕截图为空")
    template_paths = bbs.scan_for_images(project, devicefolder, dataset)
    # print("图片路径", template_paths)

    # 如果匹配成功且置信度达标，记录最佳结果
    best_match = []
    for template_path in template_paths:
        template = Template(template_path, threshold=confidence_threshold, resolution=(screen_width, screen_height))
        match_pos = template.match_in(screen)
        if match_pos:
            best_match.append(match_pos)

    # print("匹配结果", best_match)

    return best_match

def find_single_match(project ,devicefolder , dataset,image, confidence_threshold=0.80):

    """
    单张图片，直接模板匹配
    :param project:
    :param file:
    :param dataset:
    :param confidence_threshold:
    :return:
    """
    screen_width, screen_height = G.DEVICE.get_current_resolution()
    screen = G.DEVICE.snapshot()

    template_path = bbs.scan_for_target_image(project, devicefolder, dataset, image)
    # print("图片路径", template_path)
    template = Template(template_path, threshold=confidence_threshold, resolution=(screen_width, screen_height))
    match_pos = template.match_in(screen)
    # print("匹配结果", match_pos)

    return match_pos


def multi_method_match(screen, template):
    """
    核心思想：结合多种匹配方法的结果，避免单一方法失效。
    :param screen:
    :param template:
    :return:
    """
    methods = [
        cv2.TM_CCOEFF_NORMED,  # 亮度不变性
        cv2.TM_SQDIFF_NORMED,  # 噪声鲁棒性
        cv2.TM_CCORR_NORMED  # 纹理匹配
    ]

    all_results = []
    for method in methods:
        res = cv2.matchTemplate(screen, template, method)
        _, confidence, _, max_loc = cv2.minMaxLoc(res)

        # 统一置信度方向（TM_SQDIFF需要取反）
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            confidence = 1 - confidence

        all_results.append((confidence, max_loc))

    # 加权投票（例如取平均置信度最高的结果）
    best_idx = np.argmax([r[0] for r in all_results])
    return all_results[best_idx][1], all_results[best_idx][0]


def pyramid_match(screen, template, levels=3):
    """
    核心思想：先降分辨率快速定位大致区域，再逐步细化。
    :param screen:
    :param template:
    :param levels:
    :return:
    """
    best_loc = None
    best_confidence = -1

    # 构建图像金字塔
    screen_pyramid = [screen]
    template_pyramid = [template]
    for _ in range(levels - 1):
        screen_pyramid.append(cv2.pyrDown(screen_pyramid[-1]))
        template_pyramid.append(cv2.pyrDown(template_pyramid[-1]))

    # 从粗到精搜索
    for level in reversed(range(levels)):
        current_screen = screen_pyramid[level]
        current_template = template_pyramid[level]

        if best_loc:  # 上一层的定位结果作为本层的ROI
            x, y = best_loc
            roi_size = 2 * current_template.shape[1]  # 扩大搜索范围
            roi = current_screen[
                  max(0, y - roi_size):min(y + roi_size, current_screen.shape[0]),
                  max(0, x - roi_size):min(x + roi_size, current_screen.shape[1])
                  ]
            res = cv2.matchTemplate(roi, current_template, cv2.TM_CCOEFF_NORMED)
            _, confidence, _, loc = cv2.minMaxLoc(res)
            best_loc = (x + loc[0] - roi_size, y + loc[1] - roi_size)
        else:
            res = cv2.matchTemplate(current_screen, current_template, cv2.TM_CCOEFF_NORMED)
            _, confidence, _, best_loc = cv2.minMaxLoc(res)

        best_confidence = max(confidence, best_confidence)

    return best_loc, best_confidence


def feature_match(screen, template, min_matches=10):
    """
    核心思想：用局部特征替代全局模板匹配。
    :param screen:
    :param template:
    :param min_matches:
    :return:
    """
    # 初始化ORB检测器（比SIFT更快，适合嵌入式设备）
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(screen, None)

    # 暴力匹配
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    if len(matches) < min_matches:
        return None, 0.0

    # 计算匹配点中心坐标
    src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    center = np.mean(dst_pts, axis=0)[0]
    confidence = len(matches) / len(kp1)  # 匹配点比例作为置信度

    return (int(center[0]), int(center[1])), confidence


def multi_scale_matchbak(screen, template, scales= [0.1,0.2,0.3,0.4,0.5,0.55,0.6,0.7,0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]):
    """
    这个方法，只有一种匹配方式
    :param screen:
    :param template:
    :param scales:
    :return:
    """
    best_confidence = -1
    best_center = None  # 改为存储中心坐标
    best_scale = None
    for scale in scales:
        # 缩放模板
        resized = cv2.resize(template, None, fx=scale, fy=scale)
        if resized.shape[0] > screen.shape[0] or resized.shape[1] > screen.shape[1]:
            continue  # 跳过比屏幕大的模板
        # 模板匹配
        res = cv2.matchTemplate(screen, resized, cv2.TM_CCOEFF_NORMED)

        _, confidence, _, max_loc = cv2.minMaxLoc(res)

        # 计算中心坐标
        h, w = resized.shape[:2]
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        center = (center_x, center_y)

        # 保留最佳结果
        if confidence > best_confidence:
            best_confidence = confidence
            best_center = center  # 存储中心坐标
            best_scale = scale

    return best_center, best_confidence, best_scale  # 返回中心坐标


def multi_scale_match(screen, template, scales= [0.6,0.7,0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6], method='hybrid'):
    """
    method 输入的参数是 hybrid，pyramid，feature
    method 默认值 hybrid

    hybrid: 优点：适应不同图像特性，减少单一方法失败风险。
    pyramid: 优点：速度更快，适合高分辨率图像。
    feature: 优点：对旋转、缩放、光照变化鲁棒。

    :param screen:
    :param template:
    :param scales:
    :param method:
    :return:
    """
    best_center, best_conf, best_scale = None, -1, None

    for scale in scales:
        resized = cv2.resize(template, None, fx=scale, fy=scale)
        if resized.shape[0] > screen.shape[0] or resized.shape[1] > screen.shape[1]:
            continue

        # 根据需求选择方法
        if method == 'hybrid':
            loc, conf = multi_method_match(screen, resized)
        elif method == 'pyramid':
            loc, conf = pyramid_match(screen, resized)
        elif method == 'feature':
            loc, conf = feature_match(screen, resized)

        if conf > best_conf:
            h, w = resized.shape[:2]
            best_center = (loc[0] + w // 2, loc[1] + h // 2)
            best_conf = conf
            best_scale = scale

    return best_center, best_conf, best_scale



def find_best_match_multi_scale(project, devicefolder, dataset, confidence_threshold=0.80):
    """
    openCv原生多尺度匹配
    :param project:
    :param devicefolder:
    :param dataset:
    :param confidence_threshold:
    :return:
    """
    template_paths = bbs.scan_for_images(project, devicefolder, dataset )
    # print("图片路径", template_paths)
    screen = G.DEVICE.snapshot()
    best_match = []
    for template_path in template_paths:
        try:
            template_img = cv2.imread(template_path)
            if template_img is None:
                print(f"警告: 无法读取图片 {template_path}")
                continue
            pos, confidence, scale = multi_scale_match(screen, template_img)
            if confidence >= confidence_threshold:
                best_match.append(pos)
            print(f"Best match at {pos} with confidence {confidence:.2f} (scale={scale:.2f})")
        except Exception as e:
            print(f"处理图片 {template_path} 时出错: {str(e)}")
            continue
    return best_match

if __name__ == '__main__':
    # from airtest.core.settings import Settings as ST
    # ST.CVSTRATEGY = ["sift","brisk"]

    # devices= "192.168.25.170:5555"
    # devices = "R28M405TJBX"
    # devices = "23728bca"
    devices = "c7602d9f7d23"
    connect_device('android://127.0.0.1:5037/{}?'.format(devices))
    ##提取 区域的颜色
    # extract_color((808,436,853,475))
    # extract_color((1044, 542, 1094, 567))
    # 将视频，分割横纵 区域块，按照 左上，右上，左下，右下，4块区域进行输出
    #rows:行 ，cols:列
    # blocks =  get_crop_by_block(27,57)
    # blocks = get_dot_by_color2(50, 34)
    # blocks = get_dot_by_color2(34, 34)

    # print(blocks)
    # print(blocks['top_right']) (101, 8, 140) (96, 6, 130)
    # 将区域块数据和期望的颜色进行对比，然后获取
    # blocks = get_dot_by_color2(20, 20)
    # blocks = get_dotall_by_color(70, 70)

    # res = get_block_by_color(blocks=blocks['top_right'], expected_rgb=(250, 250, 160), tolerance=20)
    # res = get_block_by_color(blocks=blocks, expected_rgb=(10, 90, 200), tolerance=20)
    # print(res)
    # for item in res:
    #     print("颜色及坐标", item['color'], item['coordinate'])
    #
    # if res:
    #     click(res[-1]['coordinate'])
    # time.sleep(1)

    # for i in range(5):
    #     time.sleep(2)
    #     click(res[-1]['coordinate'])


    # print(len(blocks['top_left']))
    # print(len(blocks['top_right']))
    # print(len(blocks['bottom_left']))
    # print(len(blocks['bottom_right']))

    # blocks =  get_dot_by_colorbak(100,100)
    # saved_files = save_blocks_to_directory(blocks['top_right'], "screen_blocks_output")
    # print(blocks)
    # saved_files = save_blocks_to_directory(blocks, "screen_blocks_output")
    # print(blocks)

    # res = find_best_filter('mania', 'R28M405TJBX', 'home')
    # print(res)
    res = find_best_match('mania', 'R28M405TJBX', 'home')
    print(res)
    # res = find_single_match('mania', 'R28M405TJBX', 'home','tpl1750657128210.png')
    # print(res)
    # res = find_best_match_multi_scalebak('mania', 'R28M405TJBX', 'home', confidence_threshold=0.7)
    # print(res)
    res = find_best_match_multi_scale('mania', 'R28M405TJBX', 'home',confidence_threshold=0.7)
    print(res)



