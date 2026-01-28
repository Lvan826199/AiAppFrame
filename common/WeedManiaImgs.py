# -*- coding: utf-8 -*-
"""
@Time : 2024/12/19 18:15
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : WeedManiaImgs.py
"""
__author__ = "梦无矶小仔"

from airtest.core.api import *

# 加号进入付费
goPay = Template(r"../imageFiles/WeedMania/tpl1735031570031.png", record_pos=(0.142, -0.198), resolution=(2778, 1284), threshold=0.7)
goPay_067 = Template(r"../imageFiles/WeedMania/tpl1735107485154.png", record_pos=(0.277, -0.337), resolution=(2224, 1668), threshold=0.7)