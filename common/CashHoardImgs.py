# -*- coding: utf-8 -*-
'''
@Time : 2023/4/24 14:22
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : CashHoardImgs.py
'''
__author__ = "梦无矶小仔"

from airtest.core.api import *

auto_setup(__file__)

homeLoginPage = Template(r"../imageFiles/CashHoard/tpl1682588326851.png", record_pos=(-0.271, -0.096), resolution=(2778, 1284))
homeLogingGold = Template(r"../imageFiles/CashHoard/tpl1682588335004.png", record_pos=(-0.098, 0.185), resolution=(2778, 1284))

close_1 = Template(r"../imageFiles/CashHoard/tpl1682588458887.png", record_pos=(0.458, -0.207), resolution=(2778, 1284))
close_2 = Template(r"../imageFiles/CashHoard/tpl1682588477157.png", record_pos=(0.374, -0.202), resolution=(2778, 1284))
close_3 = Template(r"../imageFiles/CashHoard/tpl1682588490578.png", record_pos=(0.462, -0.189), resolution=(2778, 1284))
close_4 = Template(r"../imageFiles/CashHoard/tpl1682588505921.png", record_pos=(0.377, -0.202), resolution=(2778, 1284))
close_5 = Template(r"../imageFiles/CashHoard/tpl1682588557758.png", record_pos=(0.387, -0.199), resolution=(2778, 1284))
close_6 = Template(r"../imageFiles/CashHoard/tpl1684231741913.png", record_pos=(0.457, -0.193), resolution=(2778, 1284))
close_7 = Template(r"../imageFiles/CashHoard/tpl1684486245363.png", record_pos=(0.468, -0.185), resolution=(1792, 828))

# 支付 的 按钮
BuyCoins = Template(r"../imageFiles/CashHoard/tpl1682588581075.png", record_pos=(-0.044, -0.207), resolution=(2778, 1284))
BuyButton = Template(r"../imageFiles/CashHoard/tpl1682588776714.png", record_pos=(-0.05, -0.209), resolution=(2778, 1284))
Money49 = Template(r"../imageFiles/CashHoard/tpl1682588815705.png", record_pos=(-0.226, 0.131), resolution=(2778, 1284))
Money99 = Template(r"../imageFiles/CashHoard/tpl1682588833957.png", record_pos=(-0.198, 0.13), resolution=(2778, 1284))

##### 支付之后的关闭
OkButton = Template(r"../imageFiles/CashHoard/tpl1682589146739.png", record_pos=(-0.004, 0.174), resolution=(2778, 1284))
FillItToPlay = Template(r"../imageFiles/CashHoard/tpl1682589163697.png", record_pos=(-0.002, 0.189), resolution=(2778, 1284), threshold=0.82)
PressToPlay = Template(r"../imageFiles/CashHoard/tpl1682589709795.png", record_pos=(-0.003, 0.189), resolution=(2778, 1284))
SpinClose = Template(r"../imageFiles/CashHoard/tpl1682589195792.png", record_pos=(-0.001, 0.01), resolution=(2778, 1284))
collectButton = Template(r"../imageFiles/CashHoard/tpl1682589213256.png", record_pos=(-0.001, 0.166), resolution=(2778, 1284))
buy_close_1 = Template(r"../imageFiles/CashHoard/tpl1682589226361.png", record_pos=(0.382, -0.198), resolution=(2778, 1284))
buy_close_2 = Template(r"../imageFiles/CashHoard/tpl1682589434520.png", record_pos=(0.294, -0.169), resolution=(2778, 1284))
buy_close_3 = Template(r"../imageFiles/CashHoard/tpl1682589487529.png", record_pos=(0.37, -0.197), resolution=(2778, 1284))
buy_close_4 = Template(r"../imageFiles/CashHoard/tpl1682589306017.png", record_pos=(0.473, -0.21), resolution=(2778, 1284))

#### 一直关闭，直到出现如下按钮
settingButton = Template(r"../imageFiles/CashHoard/tpl1682589573480.png", record_pos=(0.472, -0.212), resolution=(2778, 1284))
settingsImg = Template(r"../imageFiles/CashHoard/tpl1682589801551.png", record_pos=(0.418, -0.161), resolution=(2778, 1284))
faceBookButton = Template(r"../imageFiles/CashHoard/tpl1682589828069.png", record_pos=(0.172, -0.087), resolution=(2778, 1284))
faceBookConnect = Template(r"../imageFiles/CashHoard/tpl1682589843945.png", record_pos=(-0.003, 0.127), resolution=(2778, 1284))

##### 登录之后的一波关闭
login_close_1 = Template(r"../imageFiles/CashHoard/tpl1682589921083.png", record_pos=(0.463, -0.211), resolution=(2778, 1284))
login_close_2 = Template(r"../imageFiles/CashHoard/tpl1682588477157.png", record_pos=(0.374, -0.202), resolution=(2778, 1284))
login_close_3 = Template(r"../imageFiles/CashHoard/tpl1682589226361.png", record_pos=(0.382, -0.198), resolution=(2778, 1284))
login_close_4 = Template(r"../imageFiles/CashHoard/tpl1682589306017.png", record_pos=(0.473, -0.21), resolution=(2778, 1284))
login_close_5 = Template(r"../imageFiles/CashHoard/tpl1682589434520.png", record_pos=(0.294, -0.169), resolution=(2778, 1284))
login_close_6 = Template(r"../imageFiles/CashHoard/tpl1682590026187.png", record_pos=(0.363, -0.212), resolution=(2778, 1284))

### 滑动进行关卡
GameLevelChose = Template(r"../imageFiles/CashHoard/tpl1682590121998.png", record_pos=(0.121, -0.104), resolution=(2778, 1284))

# 选择常规操作（不然钱不够）
RegularModel = Template(r"../imageFiles/CashHoard/tpl1682590404866.png", record_pos=(-0.108, -0.107), resolution=(2778, 1284))
playButton = Template(r"../imageFiles/CashHoard/tpl1682590188842.png", record_pos=(-0.083, -0.041), resolution=(2778, 1284))
play6000Yellow = Template(r"../imageFiles/CashHoard/tpl1682590430733.png", record_pos=(0.085, 0.053), resolution=(2778, 1284))
play6000Blue = Template(r"../imageFiles/CashHoard/tpl1682590484538.png", record_pos=(0.076, 0.066), resolution=(2778, 1284))

### 进入了spin，开始spin
Spin = Template(r"../imageFiles/CashHoard/tpl1682590216937.png", record_pos=(0.317, 0.194), resolution=(2778, 1284))
### 过程中会出现一些弹窗需要进行处理

spinClose_1 = Template(r"../imageFiles/CashHoard/tpl1682590282037.png", record_pos=(0.464, -0.209), resolution=(2778, 1284))
spinClose_2_no = Template(r"../imageFiles/CashHoard/tpl1682591418493.png", record_pos=(0.118, 0.099), resolution=(2778, 1284))
spinClose_2_Yes = Template(r"../imageFiles/CashHoard/tpl1682591423507.png", record_pos=(-0.115, 0.099), resolution=(2778, 1284))
spinClose_3 = Template(r"../imageFiles/CashHoard/tpl1682591500744.png", record_pos=(0.063, 0.128), resolution=(2778, 1284))
spinClose_4_letKittyChoose = Template(r"../imageFiles/CashHoard/tpl1682591606601.png", record_pos=(0.137, 0.189), resolution=(2778, 1284))
spinClose_5_LetsGo = Template(r"../imageFiles/CashHoard/tpl1682591610437.png", record_pos=(-0.144, 0.188), resolution=(2778, 1284))
spinClose_6 = Template(r"../imageFiles/CashHoard/tpl1682591636557.png", record_pos=(0.36, -0.181), resolution=(2778, 1284))
spinClose_7 = Template(r"../imageFiles/CashHoard/tpl1682589306017.png", record_pos=(0.473, -0.21), resolution=(2778, 1284))
