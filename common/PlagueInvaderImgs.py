# -*- coding: utf-8 -*-
'''
@Time : 2023/7/5 17:08
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : PlagueInvaderImgs.py
'''
__author__ = "梦无矶小仔"

from airtest.core.api import *

## 1、登录界面

#### 1-1 facebook登录图标
facebook_icon = Template(r"../imageFiles/PlagueInvader/tpl1688546774498.png", record_pos=(0.002, 0.082), resolution=(1284, 2778))
facebook_icon_182 = Template(r"../imageFiles/PlagueInvader/tpl1688716798846.png", record_pos=(-0.001, 0.095), resolution=(1125, 2436))
#### 1-1-1 通知页面的叉叉
close_button = Template(r"../imageFiles/PlagueInvader/tpl1688548401294.png", record_pos=(0.418, -0.565), resolution=(1284, 2778))
#### 1-1-2 继续
continue_login = Template(r"../imageFiles/PlagueInvader/tpl1688612011638.png", record_pos=(0.155, 0.661), resolution=(1284, 2778))
#### 1-2 START按钮
start_button = Template(r"../imageFiles/PlagueInvader/tpl1688546806688.png", record_pos=(0.0, 0.664), resolution=(1284, 2778))
#### 1-3 主界面C位的男主头
home_man = Template(r"../imageFiles/PlagueInvader/tpl1688546895450.png", record_pos=(0.016, 0.072), resolution=(1284, 2778))
#### 1-4 切换语言为中文，下拉按钮
change_language = Template(r"../imageFiles/PlagueInvader/tpl1688547024681.png", record_pos=(0.333, -0.855), resolution=(1284, 2778))
#### 1-5 切换为中文，简体中文
Chinese = Template(r"../imageFiles/PlagueInvader/tpl1688547061669.png", record_pos=(0.264, -0.795), resolution=(1284, 2778))
#### 1-6 出现中文的开始游戏
begin_game = Template(r"../imageFiles/PlagueInvader/tpl1688547139930.png", record_pos=(-0.003, 0.663), resolution=(1284, 2778))

#### 2、进入游戏内，支付
#### 2-1 钻石的加号点击
diamond = Template(r"../imageFiles/PlagueInvader/tpl1688547404048.png", record_pos=(0.28, -0.937), resolution=(1284, 2778))
diamond_067 = Template(r"../imageFiles/PlagueInvader/tpl1688977675526.png", record_pos=(0.206, -0.629), resolution=(1668, 2224))
#### 2-2 出现查看特权
view_privilege = Template(r"../imageFiles/PlagueInvader/tpl1688547467972.png", record_pos=(0.192, -0.583), resolution=(1284, 2778))
### 2-2 点击付钱
buy_button = Template(r"../imageFiles/PlagueInvader/tpl1688547485002.png", record_pos=(0.364, 0.396), resolution=(1284, 2778))
buy_button_067 = Template(r"../imageFiles/PlagueInvader/tpl1688978457538.png", record_pos=(0.262, -0.015), resolution=(1668, 2224))
### 2-3 支付确认
# click([0.5,0.85])

### 2-4 退出支付页面
quit_pay_page = Template(r"../imageFiles/PlagueInvader/tpl1688547587636.png", record_pos=(-0.44, 0.947), resolution=(1284, 2778))


### 3、切换主界面
# [0.1,0.94]
# [0.3,0.94]
# [0.5,0.94]
# [0.7,0.94]