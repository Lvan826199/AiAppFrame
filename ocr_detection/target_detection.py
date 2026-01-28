# -*- coding: utf-8 -*-
"""
@Time : 2023/9/25 16:01
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : target_detection.py
"""
__author__ = "梦无矶小仔"

import re
import time
import logging
import numpy as np
from typing import List, Tuple, Union, Optional, Dict

import cv2
from PIL import Image
# from airtest.core.api import *
from paddleocr import PaddleOCR, draw_ocr

# 设置 PaddleOCR 的日志级别为 WARNING 或以上 这里我改完ERROR
# logging.getLogger("ppocr").setLevel(logging.ERROR)

# 禁用 PaddleOCR 的日志输出
logging.getLogger("ppocr").setLevel(logging.CRITICAL)


class OCRSingleton():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OCRSingleton, cls).__new__(cls, *args, **kwargs)
            #  use_gup 是否使用GPU，默认为True
            # det_db_thresh ，DB模型输出预测图的二值化阈值，只有大于此阈值的文本框才会被保留，默认值0.3
            # det_max_side_len，检测算法前向时图片长边的最大尺寸，当长边超出这个值时会将长边resize到这个大小，短边等比例缩放，默认值960
            cls._instance.ocr = PaddleOCR(use_gup=False, det_db_thresh=0.1, det_max_side_len=1860, gpu_mem=200)
        return cls._instance

    def posxy(self, line: List) -> Tuple:
        xmin = line[0][0][0]
        xmax = line[0][1][0]
        ymin = line[0][0][1]
        ymax = line[0][2][1]
        posx = (xmax - xmin) / 2 + xmin
        posy = (ymax - ymin) / 2 + ymin
        pos = (int(posx), int(posy))
        return pos

    def match_target(self, target_text, match_mode, per_ocr_text, line, rectangle, confidence, deep_res: list) -> List:
        """

        :param target_text: 所检测的文本
        :param match_mode: 匹配模式 [0:包含,1:精准,2:开头,3:结尾]
        :param per_ocr_text: 目标文本
        :param line: 所有文本整体
        :param rectangle: 目标坐标
        :param confidence: 目标信任值
        :param deep_res: 返回值 列表 [{target_text1: pos1},{target_text2: pos2}]
        :return: deep_res
        """
        # 匹配所有包含目标target_text
        if match_mode == 0:
            pattern = re.compile(f"{target_text}")
        # 精准匹配target_text
        elif match_mode == 1:
            pattern = re.compile(f"^{target_text}$")
        # 精准匹配target_text开头的
        elif match_mode == 2:
            pattern = re.compile(f"^{target_text}")
        # 精准匹配target_text结尾的
        elif match_mode == 3:
            pattern = re.compile(f"{target_text}$")
        else:
            print(f"error:请检查match_mode：{match_mode} 是否为int类型，且在适配范围内!")
            print(f"error:将match_mode:{match_mode}置为0！")
            pattern = re.compile(f"{target_text}")

        match = pattern.search(per_ocr_text)

        if match:
            pos = self.posxy(line)
            print(f"匹配【{target_text}】成功,坐标：{pos}")
            # print("目标文本:{}，".format(per_ocr_text), "检测文本坐标:{}，".format(pos), "rectangle：{}，".format(rectangle),
            #       "confidence:{}，".format(confidence))
            # text_pos_dict = {target_text: pos}
            # deep_res.append(text_pos_dict)
            deep_res.append({target_text: pos})
            return deep_res
        else:
            return deep_res

    def img_show_result(self, img, result):
        """
        在图像上显示结果
        :param img: 图片
        :param result: 传入解析的图像值
        :return:
        """
        result = result[0]
        # image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(img, boxes, txts, scores)
        im_show = Image.fromarray(im_show)
        im_show.save('imgs\\result01.jpg')

    def deep_ocr(self, img: Optional[Union[List, np.ndarray, str, bytes]], action_text: Dict[str, int]) -> List:
        """

        :param img:img for ocr, support ndarray, img_path and list or ndarray
        :param action_text : 目标文本，格式{"action_text":match_mode} {str:int}
        :return:
        """
        print("检测文本中.....")
        if not img:
            print("not img")
            # img = G.DEVICE.snapshot(quality=99)
        result = self.ocr.ocr(img)
        deep_res = list()

        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                per_ocr_text = line[1][0]
                confidence = line[1][1]
                rectangle = line[0]
                # 规定per_ocr_text为检测文本字符串，target_text为待目标检测文字
                print("检测文本:{}，".format(per_ocr_text), "rectangle：{}，".format(rectangle), "confidence:{}，".format(confidence))
                per_ocr_text = re.sub(r"\s+", "", per_ocr_text)
                for target_text, match_mode in action_text.items():
                    target_text = re.sub(r"\s+", "", target_text)
                    deep_res = self.match_target(target_text=target_text, match_mode=match_mode,
                                                 per_ocr_text=per_ocr_text, line=line, rectangle=rectangle,
                                                 confidence=confidence, deep_res=deep_res)

        # 在图像上显示结果 (不需要这一步，减少内存消耗和运行时间)
        # img_show_result(img, result)

        return deep_res

    def ocr_exist(self, img: Optional[Union[List, np.ndarray, str, bytes]], action_text: Dict[str, int]) -> List:
        """
        返回匹配目标元素的坐标列表
        :param img:
        :param action_text:
        :return: 坐标列表
        """
        deep_res = self.deep_ocr(img, action_text)
        print("deep_res", deep_res)
        position_xy_list = []
        if deep_res:
            for text in deep_res:
                for pos in text.values():
                    position_xy_list.append(pos)
        return position_xy_list

    # def ocr_click(self, img: Optional[Union[List, np.ndarray, str, bytes]], action_text: Dict[str, int], order: int = 0):
    #     """
    #
    #     :param img:
    #     :param action_text:
    #     :param order: 默认全部点击，否则点击指定，传入1表示点击第一个，传入2表示点击第二个
    #     :return:
    #     """
    #     # [{'0': (432, 104)}, {'0': (774, 349)}]
    #     try:
    #         position_xy_list = self.ocr_exist(img, action_text)
    #         if position_xy_list:
    #             if order:
    #                 click(position_xy_list[order - 1])
    #                 print("点击坐标", position_xy_list[order - 1])
    #             else:
    #                 for pos in position_xy_list:
    #                     print("获取到坐标", pos)
    #                     click(pos)
    #     except Exception as e:
    #         print(f"点击坐标失败，错误信息：{e}")


# if __name__ == '__main__':
#     # ios 186
#     devices = "00008030-001E19021A42802E"
#     # // 123
#     # devices = "00008101-001859DE1E38001E"
#     dev = connect_device(f"iOS:///http+usbmux://{devices}")
#     # screen = G.DEVICE.snapshot(quality=99)
#     # action_text = {"继续": 0}
#     action_text = {"Continue": 1}
#     # d = ocr_exist(screen, action_text)
#     # print("获取结果", d)
#     # image_array = dev.snapshot(quality=99)
#     # # 保存图像到指定路径，文件格式根据文件后缀自动确定
#     # image = Image.fromarray(image_array)
#     # image.save(r"D:\Y_PythonProject\AiAppFrame\ocr_detection\snapshot.png")
#     start_time = time.time()
#     OCRSingleton = OCRSingleton()
#     OCRSingleton.ocr_exist(img=None, action_text=action_text)
#     OCRSingleton.ocr_click(img=None, action_text=action_text)
#     # for i in range(10):
#     #     ocr_click(img=None, action_text=action_text)
#     #     # ocr_exist(img=None, action_text=action_text)
#     #     # deep_ocr(img=None, action_text=action_text)
#     #     print("============================")
#
#     print(time.time() - start_time)
