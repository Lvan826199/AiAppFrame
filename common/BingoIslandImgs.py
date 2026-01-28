# -*- coding: utf-8 -*-
'''
@Time : 2022/12/8 15:17
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : BingoIslandImgs.py
'''
__author__ = "梦无矶小仔"

from airtest.core.api import *

# 刚进游戏的主页面logo图标
BIS_homePageLogo = Template(r"../imageFiles/BingoIsland/tpl1670484669653.png", record_pos=(0.003, -0.138), resolution=(2778, 1284))

# 刚进游戏的主页面 的 play 图标
BIS_homePlay = Template(r"../imageFiles/BingoIsland/tpl1670484817583.png", record_pos=(0.0, 0.179), resolution=(2778, 1284))

# 刚进游戏的主页面 的 facebook登录 图标
BIS_homeHaveAnCount = Template(r"../imageFiles/BingoIsland/tpl1670484830348.png", record_pos=(-0.001, 0.107), resolution=(2778, 1284))

# facebook
BIS_homeFacebook = Template(r"../imageFiles/BingoIsland/tpl1670485045213.png", record_pos=(-0.041, -0.023), resolution=(2778, 1284))

# apple id
BIS_homeAppleID = Template(r"../imageFiles/BingoIsland/tpl1670485063516.png", record_pos=(-0.034, 0.032), resolution=(2778, 1284))

# 网络重连
BIS_homeReconnect = Template(r"../imageFiles/BingoIsland/tpl1670485110578.png", record_pos=(0.001, 0.088), resolution=(2778, 1284))

# facebook继续
BIS_facebookContinue = Template(r"../imageFiles/BingoIsland/tpl1670486681675.png", record_pos=(0.176, 0.662), resolution=(1284, 2778))

######## 付款
# 皇冠金币按钮
BIS_payGold = Template(r"../imageFiles/BingoIsland/tpl1670489736176.png", record_pos=(-0.117, -0.195), resolution=(2778, 1284))
#  钱的符号
BIS_payMoney = Template(r"../imageFiles/BingoIsland/tpl1670489801752.png", record_pos=(-0.165, 0.183), resolution=(2778, 1284), threshold=0.65)
BIS_payMoney_100_67 = Template(r"../imageFiles/BingoIsland/tpl1671005323013.png", record_pos=(-0.213, 0.191), resolution=(2388, 1668), threshold=0.65)

# 购买完成后的
BIS_PAYCLAIM = Template(r"../imageFiles/BingoIsland/tpl1670490229527.png", record_pos=(-0.002, 0.122), resolution=(2778, 1284))
BIS_PAYCLOSERED = Template(r"../imageFiles/BingoIsland/tpl1670490271503.png", record_pos=(0.476, -0.206), resolution=(2778, 1284))
BIS_PAYNoThanks = Template(r"../imageFiles/BingoIsland/tpl1670490398225.png", record_pos=(-0.179, 0.118), resolution=(2778, 1284))

## 游戏关卡
# 房子
# BIS_palyHouse = Template(r"../imageFiles/BingoIsland/tpl1670491421192.png", record_pos=(-0.149, 0.033), resolution=(2778, 1284))
# dev包用play
BIS_palyHouse = Template(r"../imageFiles/BingoIsland/tpl1672824692178.png", record_pos=(0.001, 0.203), resolution=(2778, 1284))

# 游戏关卡内
BIS_palyNow = Template(r"../imageFiles/BingoIsland/tpl1670491548425.png", record_pos=(-0.316, 0.106), resolution=(2778, 1284))
BIS_paly2card = Template(r"../imageFiles/BingoIsland/tpl1670491645355.png", record_pos=(-0.257, 0.182), resolution=(2778, 1284), threshold=0.9)
# 白嫖按钮
BIS_palyfree = Template(r"../imageFiles/BingoIsland/tpl1670491723888.png", record_pos=(-0.278, -0.045), resolution=(2778, 1284), threshold=0.9)

# play again
BIS_PlayAgain = Template(r"../imageFiles/BingoIsland/tpl1670492918877.png", record_pos=(0.103, 0.175), resolution=(2778, 1284))

### 进入游戏关闭页面的按钮
# 046
BIS_close_046_1_red = Template(r"../imageFiles/BingoIsland/tpl1670568376426.png", record_pos=(0.404, -0.233), resolution=(1136, 640))

# 0182 Appid 登录
BIS_LoginAppleID_0182 = Template(r"../imageFiles/BingoIsland/tpl1670919085383.png", record_pos=(-0.03, 0.032), resolution=(2436, 1125))
