# -*- coding: utf-8 -*-
'''
@Time : 2023/1/11 16:29
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : NorthTowerImgs.py
'''
__author__ = "梦无矶小仔"

from airtest.core.api import *

# 进入游戏按钮
NT_BeginGame = Template(r"../imageFiles/NorthTower/tpl1675409756896.png", threshold=0.9, record_pos=(0.016, 0.657), resolution=(1284, 2778))
# 挑战按钮
NT_Challenge = Template(r"../imageFiles/NorthTower/tpl1675409958351.png", threshold=0.9, record_pos=(-0.004, 0.712), resolution=(1284, 2778))

# 设置按钮
NT_SettingButton = Template(r"../imageFiles/NorthTower/tpl1675410163947.png", record_pos=(-0.424, -0.912), resolution=(1284, 2778))

# 右下角的关卡奖励
NT_levelReward = Template(r"../imageFiles/NorthTower/tpl1675410576030.png", record_pos=(0.347, 0.695), resolution=(1284, 2778))

# 点击加号进行付款
NT_addButton = Template(r"../imageFiles/NorthTower/tpl1675410706500.png", threshold=0.8, record_pos=(0.46, -0.952), resolution=(1284, 2778))
NT_addButton_100 = Template(r"../imageFiles/NorthTower/tpl1675420906551.png", record_pos=(0.466, -0.612), resolution=(1668, 2388))

# 支付钻石的黑白图片
NT_D = Template(r"../imageFiles/NorthTower/tpl1675410996109.png", record_pos=(-0.416, -0.483), resolution=(1284, 2778))
# 067 100 金币的黑白图片
NT_Gold = Template(r"../imageFiles/NorthTower/tpl1675421040004.png", record_pos=(-0.436, -0.128), resolution=(1668, 2388))

# 付款 99
NT_Money99 = Template(r"../imageFiles/NorthTower/tpl1675411203198.png", threshold=0.8, record_pos=(0.036, -0.109), resolution=(1284, 2778))
NT_Money99_100 = Template(r"../imageFiles/NorthTower/tpl1675421050447.png", record_pos=(0.026, -0.237), resolution=(1668, 2388))

# 付款成功后点击领取
NT_accept = Template(r"../imageFiles/NorthTower/tpl1675411380976.png", threshold=0.9, record_pos=(0.0, 0.924), resolution=(1284, 2778))

# 红房子
NT_redHouse = Template(r"../imageFiles/NorthTower/tpl1675411523893.png", record_pos=(-0.41, 0.986), resolution=(1284, 2778))
NT_redHouse_100 = Template(r"../imageFiles/NorthTower/tpl1675663178826.png", record_pos=(-0.424, 0.64), resolution=(1668, 2388))

# 领取奖励
NT_getReward = Template(r"../imageFiles/NorthTower/tpl1675412017245.png", record_pos=(-0.205, 0.916), resolution=(1284, 2778))

# 下一关
NT_NextLevel = Template(r"../imageFiles/NorthTower/tpl1675412170077.png", threshold=0.9, record_pos=(0.219, 0.912), resolution=(1284, 2778))

# 登录AppleID
NT_sign = Template(r"../imageFiles/NorthTower/tpl1675667458568.png", record_pos=(-0.168, 0.281), resolution=(1668, 2224))

# 绑定AppleID确定按钮
NT_confirm = Template(r"../imageFiles/NorthTower/tpl1675668058839.png", record_pos=(0.186, 0.215), resolution=(1668, 2224))
