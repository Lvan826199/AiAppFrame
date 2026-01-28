# -*- coding: utf-8 -*-
'''
@Time : 2023/2/27 10:58
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : MatchScapesImgs.py
'''
__author__ = "梦无矶小仔"

from airtest.core.api import *

auto_setup(__file__)

homePageLogo = Template(r"../imageFiles/DoubleRich/tpl1681979232768.png", record_pos=(0.01, -0.107), resolution=(2778, 1284))
facebookLogin = Template(r"../imageFiles/DoubleRich/tpl1681979438195.png", record_pos=(0.133, 0.081), resolution=(2778, 1284))
appleIdLogin = Template(r"../imageFiles/DoubleRich/tpl1681979444154.png", record_pos=(-0.136, 0.084), resolution=(2778, 1284))
GotIt = Template(r"../imageFiles/DoubleRich/tpl1682320844322.png", record_pos=(-0.001, 0.102), resolution=(2436, 1125))
TAPTOCOLLECT = Template(r"../imageFiles/DoubleRich/tpl1682065407704.png", record_pos=(-0.003, 0.202), resolution=(2778, 1284))
close_1 = Template(r"../imageFiles/DoubleRich/tpl1681979902811.png", record_pos=(0.381, -0.204), resolution=(2778, 1284))
close_2 = Template(r"../imageFiles/DoubleRich/tpl1681979914961.png", record_pos=(0.381, -0.208), resolution=(2778, 1284))
close_3 = Template(r"../imageFiles/DoubleRich/tpl1681979949916.png", record_pos=(0.392, -0.213), resolution=(2778, 1284))
close_4 = Template(r"../imageFiles/DoubleRich/tpl1681979968500.png", record_pos=(0.371, -0.194), resolution=(2778, 1284))
close_5 = Template(r"../imageFiles/DoubleRich/tpl1682323448052.png", record_pos=(0.374, -0.198), resolution=(2436, 1125))
BuyButton = Template(r"../imageFiles/DoubleRich/tpl1681979985800.png", record_pos=(-0.045, -0.215), resolution=(2778, 1284))
money99 = Template(r"../imageFiles/DoubleRich/tpl1681980291437.png", record_pos=(-0.29, -0.034), resolution=(2778, 1284))
# 购买之后的关闭
Contact_Support = Template(r"../imageFiles/DoubleRich/tpl1681980420786.png", record_pos=(-0.001, 0.103), resolution=(2778, 1284))
close_buy_1 = Template(r"../imageFiles/DoubleRich/tpl1681980428775.png", record_pos=(0.232, -0.139), resolution=(2778, 1284))
close_buy_2 = Template(r"../imageFiles/DoubleRich/tpl1681981589254.png", record_pos=(0.37, -0.195), resolution=(2778, 1284))
awesome = Template(r"../imageFiles/DoubleRich/tpl1682069861050.png", record_pos=(0.006, 0.156), resolution=(2778, 1284))
collect = Template(r"../imageFiles/DoubleRich/tpl1681981607758.png", record_pos=(0.002, 0.17), resolution=(2778, 1284))
collect_1 = Template(r"../imageFiles/DoubleRich/tpl1682070295439.png", record_pos=(-0.003, 0.108), resolution=(2778, 1284))
Continue = Template(r"../imageFiles/DoubleRich/tpl1681981631111.png", record_pos=(0.003, 0.172), resolution=(2778, 1284))
close_buy_3 = Template(r"../imageFiles/DoubleRich/tpl1681981735268.png", record_pos=(0.269, -0.138), resolution=(2778, 1284))
close_push = Template(r"../imageFiles/DoubleRich/tpl1681981751136.png", record_pos=(0.0, 0.079), resolution=(2778, 1284))
close_great = Template(r"../imageFiles/DoubleRich/tpl1681981769843.png", record_pos=(-0.007, 0.15), resolution=(2778, 1284))
open_all = Template(r"../imageFiles/DoubleRich/tpl1681981789333.png", record_pos=(0.306, 0.187), resolution=(2778, 1284))
later = Template(r"../imageFiles/DoubleRich/tpl1681981819730.png", record_pos=(-0.124, 0.12), resolution=(2778, 1284))
spinButton = Template(r"../imageFiles/DoubleRich/tpl1681982187198.png", record_pos=(0.257, 0.181), resolution=(2778, 1284))
spin_close_1 = Template(r"../imageFiles/DoubleRich/tpl1681982250786.png", record_pos=(0.326, -0.163), resolution=(2778, 1284))

##############facebook登录
settingButton = Template(r"../imageFiles/DoubleRich/tpl1681983001864.png", record_pos=(0.387, -0.213), resolution=(2778, 1284))
settingClick = Template(r"../imageFiles/DoubleRich/tpl1681983098182.png", record_pos=(0.288, -0.066), resolution=(2778, 1284), threshold=0.9)
logoutButton = Template(r"../imageFiles/DoubleRich/tpl1681983220528.png", record_pos=(0.235, 0.01), resolution=(2778, 1284))
logooutConfirm = Template(r"../imageFiles/DoubleRich/tpl1681983243743.png", record_pos=(-0.111, 0.103), resolution=(2778, 1284))
connect = Template(r"../imageFiles/DoubleRich/tpl1681983334918.png", record_pos=(0.238, 0.009), resolution=(2778, 1284))
