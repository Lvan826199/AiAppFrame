# -*- coding: utf-8 -*-
'''
@Time : 2022/9/14 10:16
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : start.py
'''
__author__ = "梦无矶小仔"

import datetime
import os
import random
import shutil
import time

from myutils import index
# from ocr_detection.target_detection import OCRSingleton

index_print = print
# ocrScan = OCRSingleton()


def start():
    index.main()


def deleteUtilslog():
    try:
        shutil.rmtree("utils/log")
    except:
        pass


# 从根目录启动，确保相对路径调用正常
if __name__ == '__main__':
    # os.popen('adb start-server') #针对android设备
    deleteUtilslog()
    start()

### 测试分支
