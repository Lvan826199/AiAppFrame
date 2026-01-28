# -*- coding: utf-8 -*-
'''
@Time : 2023/4/24 14:22
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : HugeWinImgs.py
'''
__author__ = "梦无矶小仔"

from airtest.core.api import *

auto_setup(__file__)

#### 1、进入游戏步骤
#
# 1.1 授权操作（182封装模式）

# 1.2 判断首页面
HomePage_1 = Template(r"../imageFiles/HugeWin/tpl1685695459124.png", record_pos=(-0.002, -0.038), resolution=(2778, 1284))
HomePage_2 = Template(r"../imageFiles/HugeWin/tpl1685695530086.png", record_pos=(0.001, -0.045), resolution=(2778, 1284))
# 1.3 进入游戏的按钮操作
collect_1 = Template(r"../imageFiles/HugeWin/tpl1685695557851.png", record_pos=(-0.003, 0.185), resolution=(2778, 1284))
close_0 = Template(r"../imageFiles/HugeWin/tpl1686047911226.png", record_pos=(0.351, -0.176), resolution=(2778, 1284))
#### 2、付费操作
SALE_button = Template(r"../imageFiles/HugeWin/tpl1685695607554.png", record_pos=(0.009, -0.211), resolution=(2778, 1284))
BUY_button =Template(r"../imageFiles/HugeWin/tpl1686048078404.png", record_pos=(-0.001, -0.212), resolution=(2778, 1284))
Money_99_button = Template(r"../imageFiles/HugeWin/tpl1685695635662.png", record_pos=(0.252, -0.103), resolution=(2778, 1284))
Money_99_button_067 = Template(r"../imageFiles/HugeWin/tpl1686129625024.png", record_pos=(0.306, -0.126), resolution=(2224, 1668))

## 2.1 进行付费操作

## 2.2 付完之后进行收集关闭
collect_2 = Template(r"../imageFiles/HugeWin/tpl1685695775623.png", record_pos=(-0.002, 0.144), resolution=(2778, 1284))
collect_3 = Template(r"../imageFiles/HugeWin/tpl1685695811715.png", record_pos=(0.0, 0.114), resolution=(2778, 1284))
keep_going = Template(r"../imageFiles/HugeWin/tpl1685695903161.png", record_pos=(-0.006, 0.161), resolution=(2778, 1284))
### 2.2.1 红色关闭按钮
close_red = Template(r"../imageFiles/HugeWin/tpl1685695930042.png", record_pos=(0.337, -0.211), resolution=(2778, 1284))
check = Template(r"../imageFiles/HugeWin/tpl1685695971311.png", record_pos=(-0.004, 0.116), resolution=(2778, 1284))
check_big = Template(r"../imageFiles/HugeWin/tpl1685696007354.png", record_pos=(0.001, 0.117), resolution=(2778, 1284), threshold=0.55)
collect_4 = Template(r"../imageFiles/HugeWin/tpl1685697842114.png", record_pos=(0.001, 0.162), resolution=(2778, 1284))
close_1 = Template(r"../imageFiles/HugeWin/tpl1685696283465.png", record_pos=(0.364, -0.197), resolution=(2778, 1284))
close_2 = Template(r"../imageFiles/HugeWin/tpl1686126856593.png", record_pos=(0.374, -0.194), resolution=(2778, 1284))
# 如果能够识别到SALE按钮，则表示全部关闭完毕，可以直接退出关闭操作，进行下一个步骤

# 红叉放在最后一个检测，检测完一整轮再判断sale图标


##### 3、进行spin

##### 3.1 点击下载机台进入，点击后等待10秒，如果屏幕中没有这个下载按钮，则表示已经进入了机台

download_enter_game = Template(r"../imageFiles/HugeWin/tpl1685697995932.png", record_pos=(0.12, 0.121), resolution=(2778, 1284))
ok_button = Template(r"../imageFiles/HugeWin/tpl1685957241691.png", record_pos=(-0.005, 0.091), resolution=(2778, 1284))
##### 3.2 关闭机台的弹窗，依然是小红按钮
close_red_1 = Template(r"../imageFiles/HugeWin/tpl1685698102726.png", record_pos=(0.316, -0.198), resolution=(2778, 1284))
# spin20次左右
spin_button = Template(r"../imageFiles/HugeWin/tpl1685698826227.png", record_pos=(0.256, 0.186), resolution=(2778, 1284))
#### 3.3 spin过程中需要关闭，还需要点击屏幕
# click([0.5,0.745])
collect_5 = Template(r"../imageFiles/HugeWin/tpl1685698891361.png", record_pos=(0.0, 0.17), resolution=(2778, 1284))
#### 3.4 搞得差不多了就点击左上角的箭头，进行退出
back_button = Template(r"../imageFiles/HugeWin/tpl1685701644050.png", record_pos=(-0.293, -0.21), resolution=(2778, 1284))
big_red_jiantou = Template(r"../imageFiles/HugeWin/tpl1685957756030.png", record_pos=(0.003, -0.071), resolution=(2778, 1284))
green_close = Template(r"../imageFiles/HugeWin/tpl1685957879300.png", record_pos=(0.337, -0.189), resolution=(2778, 1284))
# 退出之后可能会有一些关闭操作，这里没遇到，后续补
# 已经知道的一个是红色的叉叉，可以加进来这里

#### 4、进行登录
### 4.1 点击右上角的
f_connect =Template(r"../imageFiles/HugeWin/tpl1686202990922.png", record_pos=(-0.342, -0.206), resolution=(2778, 1284))
settings_button = Template(r"../imageFiles/HugeWin/tpl1685701742101.png", record_pos=(0.389, -0.21), resolution=(2778, 1284))
swttings_text = Template(r"../imageFiles/HugeWin/tpl1685701930970.png", record_pos=(0.3, -0.044), resolution=(2778, 1284))
connect_facebook = Template(r"../imageFiles/HugeWin/tpl1685702014244.png", record_pos=(0.204, 0.153), resolution=(2778, 1284))
sign_in_facebook = Template(r"../imageFiles/HugeWin/tpl1685702036033.png", record_pos=(-0.144, 0.122), resolution=(2778, 1284))
sign_in_with_facebook = Template(r"../imageFiles/HugeWin/tpl1685702053430.png", record_pos=(0.003, 0.063), resolution=(2778, 1284))
### 后续就是正常登录了
# a = find_all(Template(r"../imageFiles/HugeWin/tpl1685698826227.png", record_pos=(0.256, 0.186), resolution=(2778, 1284)))
# print(a)
