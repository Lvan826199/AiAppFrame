# -*- coding: utf-8 -*-
'''
@Time : 2023/6/13 11:03
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : HarvestTownImgs.py
'''
__author__ = "梦无矶小仔"

from airtest.core.api import *

auto_setup(__file__)
# 1、进入游戏，进行授权操作

# 2、需要进行一定的等待时间，后面设备会弹出登录弹窗

'''
if exists(第三方登录)：
    = facebook登录)
else：
    = 点击进入游戏)
'''

facebook_icon = Template(r"../imageFiles/HarvestTown/tpl1686216310666.png", record_pos=(0.0, 0.037), resolution=(2778, 1284))
enter_game = Template(r"../imageFiles/HarvestTown/tpl1686206636996.png", record_pos=(0.001, 0.15), resolution=(2778, 1284))

###  2.1 进行正常的facebook登录操作

### 2.2 进行确认点击
confirm_button_common = Template(r"../imageFiles/HarvestTown/tpl1686206961845.png", record_pos=(-0.003, 0.159), resolution=(2778, 1284))
### 2.3 点击同意协议，这里使用坐标
# 123 、182 、 186
click([0.614,0.785])
# 046 、192
click([0.636,0.785])

# 100 、 67gam
click([0.636,0.838])

#### 2.4 点击进入游戏
# 登录完成
game_icon = Template(r"../imageFiles/HarvestTown/tpl1686207525052.png", record_pos=(-0.054, -0.14), resolution=(2778, 1284))

#### 进入游戏内部

## 3、 过新手教程
 ### 3.1 是否跳过剧情，点击确认
 ### 3.2 给角色命名，点击确认
 ### 3.3 点击加速、点击跳过
speed_up = Template(r"../imageFiles/HarvestTown/tpl1686208473370.png", record_pos=(-0.4, -0.198), resolution=(2778, 1284))
skip_button = Template(r"../imageFiles/HarvestTown/tpl1686208477310.png", record_pos=(-0.297, -0.198), resolution=(2778, 1284))

####  3.4 是否跳过剧情，选择确认
# = confirm_button_common)

####  3.5 出现老头剧情，点击我很熟悉
familiar_text = Template(r"../imageFiles/HarvestTown/tpl1686208671390.png", record_pos=(0.129, 0.191), resolution=(2778, 1284))

#### 3.6 点击屏幕中间
# click([0.5,0.5])

#### 3.7 游戏阶段，拿铲子
shovel = Template(r"../imageFiles/HarvestTown/tpl1686208766857.png", record_pos=(-0.128, 0.194), resolution=(2778, 1284))

#### 3.8 使用坐标记录铲子的位置
# a = find_all(Template(r"../imageFiles/HarvestTown/tpl1686208766857.png", record_pos=(-0.128, 0.194), resolution=(2778, 1284))
# print(a) # [{'result': (1033, 1182), 'rectangle': ((981, 1129), (981, 1235), (1086, 1235), (1086, 1129)), 'confidence': 0.93189936876297}, {'result': (2425, 1114), 'rectangle': ((2373, 1061), (2373, 1167), (2478, 1167), (2478, 1061)), 'confidence': 0.9097123146057129}]

# 上面数据取第二组，用[-1]取值，拿到坐标，之后操作点击就用这个

### 3.9 尝试跳过引导
skip_guide_common = Template(r"../imageFiles/HarvestTown/tpl1686209121040.png", record_pos=(-0.002, -0.212), resolution=(2778, 1284))

### 3.9.1 确认
# = confirm_button_common)

### 跳过了新手引导，进行后续操作

## 4.0.0 毛玉石篇 --》
click([0.5,0.5])
# = 加速)

## 4.1 被强制引导，需要点击菜单
menu_common = Template(r"../imageFiles/HarvestTown/tpl1686209427926.png", record_pos=(-0.466, -0.153), resolution=(2778, 1284))

### 4.1.1 067设备用下面这张图
menu_067 = Template(r"../imageFiles/HarvestTown/tpl1686221281870.png", record_pos=(-0.459, -0.282), resolution=(2224, 1668))


## 4.2 点击保存进度
save_data = Template(r"../imageFiles/HarvestTown/tpl1686209453406.png", record_pos=(-0.439, -0.099), resolution=(2778, 1284))


## 4.2.1 尝试跳过引导
# = skip_guide_common)

## 4.2.2 确认
# = confirm_button_common)

## 4.1 等到右上角出现shop
shop_icon = Template(r"../imageFiles/HarvestTown/tpl1686209307024.png", record_pos=(0.464, -0.207), resolution=(2778, 1284))

## 4.1.1 100 用下面这张
shop_icon_100 = Template(r"../imageFiles/HarvestTown/tpl1686221737734.png", record_pos=(0.455, -0.322), resolution=(2388, 1668))


## 4.2 点击钻石进行购买
diamond_img = Template(r"../imageFiles/HarvestTown/tpl1686210383365.png", record_pos=(-0.09, 0.128), resolution=(2778, 1284))

## 4.2.1 点击确认充值
# = confirm_button_common)

## 4.2.2 如果屏幕上出现了 购买 字眼 就可以进行充值的相关操作了

## 4.2.3 充值成功，点击 ['好']

## 4.3 出现充值成功，表示成功了，可以退出，然后卸载游戏了
buy_success = Template(r"../imageFiles/HarvestTown/tpl1686210596424.png", record_pos=(-0.002, -0.075), resolution=(2778, 1284))

### 补充
#### 注册账号流程
registerAccountButton = Template(r"../imageFiles/HarvestTown/tpl1686728991486.png", record_pos=(-0.002, -0.054), resolution=(2778, 1284))

##########  由于平板控件无法横版，只能用图片了 ！
### 点击邮箱，输入随机邮箱
email_field = Template(r"../imageFiles/HarvestTown/tpl1686896603909.png", record_pos=(-0.1, -0.017), resolution=(2778, 1284))
###  点击密码
pwd_field = Template(r"../imageFiles/HarvestTown/tpl1686896636288.png", record_pos=(-0.067, -0.124), resolution=(2778, 1284))
### 点击空白处
# click([0.2,0.2])
### 点击勾选同意
agree_button = Template(r"../imageFiles/HarvestTown/tpl1686896698322.png", record_pos=(-0.091, 0.156), resolution=(2778, 1284))
agree_button_100 = Template(r"../imageFiles/HarvestTown/tpl1686910022986.png", record_pos=(-0.072, 0.12), resolution=(2388, 1668))
agree_button_182 = Template(r"../imageFiles/HarvestTown/tpl1688373971075.png", record_pos=(-0.104, 0.177), resolution=(2436, 1125))
# 这个的坐标为（0.409,0.835）
# 最后点击注册
register_button = Template(r"../imageFiles/HarvestTown/tpl1686896749067.png", record_pos=(-0.003, 0.117), resolution=(2778, 1284))


