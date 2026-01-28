# -*- coding: utf-8 -*-
"""
@Time : 2025/1/22 18:41
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : draft_test01.py
"""
__author__ = "梦无矶小仔"


# 示列使用 图像文字识别service
import time

import requests

url = "http://127.0.0.1:8666/ocr"
img = "test"
params = {"image_path": "D:\Y_PythonProject\AiAppFrame\ocr_detection\snapshot.png"}
start_time = time.time()
response = requests.get(url, params=params)
print(response.text)
end_time = time.time()
print("耗时：", end_time - start_time, "s")