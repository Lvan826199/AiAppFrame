# -*- coding: utf-8 -*-

# @Time : 2022/9/19 16:08
# @Author : Vincent.xiaozai
# @Email : Lvan826199@163.com
# @File : imageElePath.py

from airtest.core.api import *

'''
imageElePath.py文件用于存储airtest中对图像识别的图片，其他文件可以直接引用此文件使用对应的图片
图片存储在项目根目录的imageFiles文件夹下
如果有多个项目,可以在imageFiles下创建对应项目文件夹,具体可以根据需求进行改进
此文件只做示例
'''
######################
############################            ###############################
############################  图片存储  ###############################
############################           ###############################
#######################


######################
############################            ###############################
############################  Demo     ###############################
############################           ###############################
#######################

facebook_continue = Template(r"../imageFiles/FaceBook/tpl1662538211709.png", record_pos=(0.171, 0.664), resolution=(1284, 2778))

######################
############################            ###############################
############################  BingoParty     ###############################
############################           ###############################
#######################
######################
BP_game_home = Template(r"../imageFiles/BingoParty/tpl1657106496371.png", record_pos=(-0.397, -0.025), resolution=(2208, 1242))
# gameOk = Template(r"../imageFiles/BingoParty/tpl1658485350354.png", record_pos=(0.006, 0.103), resolution=(2778, 1284))

## 平板 100 的
BP_gameOk = Template(r"../imageFiles/BingoParty/tpl1658910481053.png", record_pos=(-0.002, 0.116), resolution=(2388, 1668))
BP_alert = Template(r"../imageFiles/BingoParty/tpl1657106017316.png", record_pos=(0.031, 0.12), resolution=(2208, 1242))
BP_red_quit_1 = Template(r"../imageFiles/BingoParty/tpl1628843865964.png", record_pos=(0.381, -0.203), resolution=(1136, 640))
BP_red_quit_2 = Template(r"../imageFiles/BingoParty/tpl1628844261940.png", record_pos=(0.468, -0.251), resolution=(1136, 640))
BP_red_quit_3 = Template(r"../imageFiles/BingoParty/tpl1628844298979.png", record_pos=(0.371, -0.207), resolution=(1136, 640))
BP_red_quit_4 = Template(r"../imageFiles/BingoParty/tpl1628844508005.png", record_pos=(0.46, -0.251), resolution=(1136, 640))
BP_red_quit_5 = Template(r"../imageFiles/BingoParty/tpl1628844558366.png", record_pos=(0.291, -0.201), resolution=(1136, 640))
BP_red_quit_6 = Template(r"../imageFiles/BingoParty/tpl1628852838204.png", record_pos=(0.424, -0.23), resolution=(1136, 640))
BP_red_quit_7 = Template(r"../imageFiles/BingoParty/tpl1655452765064.png", record_pos=(0.46, -0.254), resolution=(1136, 640))
BP_brown_quit_1 = Template(r"../imageFiles/BingoParty/tpl1628844023718.png", threshold=0.85, record_pos=(0.357, -0.229), resolution=(1136, 640))
BP_update_level = Template(r"../imageFiles/BingoParty/tpl1655456660479.png", record_pos=(-0.148, 0.206), resolution=(1136, 640))
BP_update_level_button = Template(r"../imageFiles/BingoParty/tpl1658917612314.png", record_pos=(-0.21, 0.301), resolution=(2224, 1668))
BP_round_1 = Template(r"../imageFiles/BingoParty/tpl1628853825078.png", record_pos=(-0.295, -0.151), resolution=(1136, 640))
BP_public_set = Template(r"../imageFiles/BingoParty/tpl1628844428004.png", record_pos=(-0.459, -0.245), resolution=(1136, 640))
BP_hawaii = Template(r"../imageFiles/BingoParty/tpl1628847625396.png", threshold=0.85, record_pos=(-0.195, 0.026), resolution=(1136, 640))
BP_Venice = Template(r"../imageFiles/BingoParty/tpl1628847659740.png", record_pos=(0.021, -0.13), resolution=(1136, 640))
BP_claim = Template(r"../imageFiles/BingoParty/tpl1629184188588.png", record_pos=(0.015, 0.173), resolution=(1136, 640))
BP_account_bt = Template(r"../imageFiles/BingoParty/tpl1629268054272.png", threshold=0.80, record_pos=(-0.053, 0.154), resolution=(1136, 640))
## 067
BP_account_bt_067 = Template(r"../imageFiles/BingoParty/tpl1658915809321.png", record_pos=(-0.332, 0.163), resolution=(2224, 1668))
BP_fb_button_046 = Template(r"../imageFiles/BingoParty/tpl1629709405287.png", record_pos=(0.002, 0.194), resolution=(1136, 640))
BP_fb_button_067 = Template(r"../imageFiles/BingoParty/tpl1657249105250.png", record_pos=(0.053, 0.168), resolution=(1792, 828))
BP_re_ct = Template(r"../imageFiles/BingoParty/tpl1629709549774.png", record_pos=(0.032, 0.121), resolution=(1136, 640))

######################
############################            ###############################
############################  BingoJourney     ###############################
############################           ###############################
#######################

# BJ_game_home = Template(r"../imageFiles/BingoJourney/tpl1657616213332.png", record_pos=(-0.209, 0.05), resolution=(1136, 640))
BJ_game_home = Template(r"../imageFiles/BingoJourney/tpl1657616213332.png", record_pos=(0.246, 0.05), resolution=(2778, 1284))
BJ_game_ok = Template(r"../imageFiles/BingoJourney/tpl1657787167932.png", record_pos=(-0.004, 0.12), resolution=(2208, 1242))
BJ_alert = Template(r"../imageFiles/BingoJourney/tpl1657106017316.png", record_pos=(0.031, 0.12), resolution=(2208, 1242))
BJ_red_quit_1 = Template(r"../imageFiles/BingoJourney/tpl1657597041907.png", record_pos=(0.467, -0.252), resolution=(1136, 640))
BJ_red_quit_2 = Template(r"../imageFiles/BingoJourney/tpl1657597058813.png", record_pos=(0.467, -0.254), resolution=(1136, 640))
BJ_red_quit_3 = Template(r"../imageFiles/BingoJourney/tpl1657608628278.png", record_pos=(0.411, -0.238), resolution=(2208, 1242))
BJ_red_quit_4 = Template(r"../imageFiles/BingoJourney/tpl1657599450461.png", record_pos=(0.361, -0.201), resolution=(1136, 640))
BJ_red_quit_5 = Template(r"../imageFiles/BingoJourney/tpl1657597527559.png", record_pos=(0.467, -0.252), resolution=(1136, 640))
# 这三个在joureny里面没有
BJ_red_quit_6 = Template(r"../imageFiles/BingoJourney/tpl1628852838204.png", record_pos=(0.424, -0.23), resolution=(1136, 640))
BJ_red_quit_7 = Template(r"../imageFiles/BingoJourney/tpl1655452765064.png", record_pos=(0.46, -0.254), resolution=(1136, 640))
BJ_brown_quit_1 = Template(r"../imageFiles/BingoJourney/tpl1628844023718.png", threshold=0.85, record_pos=(0.357, -0.229), resolution=(1136, 640))
BJ_update_level = Template(r"../imageFiles/BingoJourney/tpl1657609737152.png", record_pos=(-0.209, 0.215), resolution=(2208, 1242))
BJ_update_level_067 = Template(r"../imageFiles/BingoJourney/tpl1658975837494.png", record_pos=(-0.174, 0.312), resolution=(2224, 1668))
BJ_round_1 = Template(r"../imageFiles/BingoJourney/tpl1628853825078.png", record_pos=(-0.295, -0.151), resolution=(1136, 640))
BJ_public_set = Template(r"../imageFiles/BingoJourney/tpl1628844428004.png", record_pos=(-0.459, -0.245), resolution=(1136, 640))
BJ_hawaii = Template(r"../imageFiles/BingoJourney/tpl1657597203799.png", record_pos=(0.136, 0.113), resolution=(1136, 640))
BJ_Venice = Template(r"../imageFiles/BingoJourney/tpl1657618631085.png", record_pos=(-0.199, -0.088), resolution=(2208, 1242))
BJ_claim = Template(r"../imageFiles/BingoJourney/tpl1657597240072.png", record_pos=(0.001, 0.058), resolution=(1136, 640))
BJ_continueImg = Template(r"../imageFiles/BingoJourney/tpl1657621909725.png", record_pos=(-0.002, 0.173), resolution=(1136, 640))
BJ_account_bt = Template(r"../imageFiles/BingoJourney/tpl1657597444647.png", record_pos=(-0.047, 0.152), resolution=(1136, 640))
BJ_account_bt_067 = Template(r"../imageFiles/BingoJourney/tpl1658975478341.png", record_pos=(0.189, 0.152), resolution=(2224, 1668))
BJ_fb_button = Template(r"../imageFiles/BingoJourney/tpl1657616618153.png", record_pos=(-0.007, 0.192), resolution=(1136, 640))
BJ_fb_button_192 = Template(r"../imageFiles/BingoJourney/tpl1657789993919.png", record_pos=(0.083, 0.16), resolution=(1792, 828))
BJ_re_ct = Template(r"../imageFiles/BingoJourney/tpl1629709549774.png", record_pos=(0.032, 0.121), resolution=(1136, 640))

######################
############################            ###############################
############################  DoubleWin  ###############################
############################           ###############################
#######################
DW_game_home = Template(r"../imageFiles/DoubleWin/tpl1685434443936.png", record_pos=(0.296, -0.071), resolution=(2778, 1284))
DW_fb_button = Template(r"../imageFiles/DoubleWin/tpl1685434463436.png", record_pos=(0.002, 0.151), resolution=(2778, 1284))
# DW_fb_button_123 = Template(r"../imageFiles/DoubleWin/tpl1685434463436.png", record_pos=(0.002, 0.151), resolution=(2778, 1284))
DW_fb_button_123 = Template(r"../imageFiles/DoubleWin/tpl1685435005509.png", record_pos=(0.081, 0.154), resolution=(2778, 1284))

################# 登录的一系列操作
DW_collect_and_play = Template(r"../imageFiles/DoubleWin/collect_and_play46.png", record_pos=(0.09, 0.164), resolution=(1136, 640))
DW_red_quit_1 = Template(r"../imageFiles/DoubleWin/tpl1660639236761.png", record_pos=(0.355, -0.217), resolution=(1136, 640))
################ 192
DW_red_quit_2 = Template(r"../imageFiles/DoubleWin/tpl1660639951971.png", record_pos=(0.446, -0.218), resolution=(2208, 1242))
DW_red_quit_3 = Template(r"../imageFiles/DoubleWin/tpl1660640004694.png", record_pos=(0.466, -0.252), resolution=(2208, 1242))
DW_red_quit_4 = Template(r"../imageFiles/DoubleWin/tpl1660640069332.png", record_pos=(0.385, -0.241), resolution=(2208, 1242))
DW_red_quit_5 = Template(r"../imageFiles/DoubleWin/tpl1660640089528.png", record_pos=(0.459, -0.24), resolution=(2208, 1242))
################################ 067
# 广告关闭
DW_ad_close_1 = Template(r"../imageFiles/DoubleWin/tpl1660715488483.png", record_pos=(0.474, -0.349), resolution=(2224, 1668))
# 购买按钮
DW_clear_buy = Template(r"../imageFiles/DoubleWin/tpl1660806234418.png", record_pos=(-0.045, -0.332), resolution=(2388, 1668))
DW_clear_buy_1 = Template(r"../imageFiles/DoubleWin/tpl1682408517506.png", record_pos=(-0.042, -0.213), resolution=(2778, 1284))
DW_buy_button = Template(r"../imageFiles/DoubleWin/tpl1660640873726.png", record_pos=(-0.045, -0.261), resolution=(2208, 1242))
DW_money_button = Template(r"../imageFiles/DoubleWin/tpl1660641043446.png", record_pos=(0.258, -0.173), resolution=(2208, 1242))
DW_money_Ok = Template(r"../imageFiles/DoubleWin/tpl1660641391406.png", record_pos=(0.002, 0.207), resolution=(2208, 1242))
DW_vip_YEAH = Template(r"../imageFiles/DoubleWin/tpl1660641509286.png", record_pos=(0.001, 0.217), resolution=(2208, 1242))
# 有vip_YEAH就会出现这个退出的按钮，点击叉掉
DW_money_quit = Template(r"../imageFiles/DoubleWin/tpl1660641952706.png", record_pos=(0.439, -0.226), resolution=(2208, 1242))
# 开始选游戏,选那个狮子头的
DW_lionIcon = Template(r"../imageFiles/DoubleWin/tpl1660642376739.png", record_pos=(0.106, -0.144), resolution=(2208, 1242))
# 点击了狮子头，选择玩的等级，选蓝色的，不管数字
DW_blueLevel = Template(r"../imageFiles/DoubleWin/tpl1660642545554.png", record_pos=(0.246, 0.16), resolution=(2208, 1242))
#### spin按钮
# 坐标 [0.87,0.88]
DW_spinButton = Template(r"../imageFiles/DoubleWin/tpl1660643040099.png", record_pos=(0.389, 0.221), resolution=(2208, 1242))
##### spin过程中会出现各种点击
# 升级
DW_levelUpClose = Template(r"../imageFiles/DoubleWin/tpl1660643309557.png", record_pos=(0.395, -0.202), resolution=(2208, 1242))
DW_levelUpClose_067 = Template(r"../imageFiles/DoubleWin/levelUpClose_067.png", record_pos=(0.394, -0.202), resolution=(2224, 1668))
# 是否快乐询问
DW_happyClose = Template(r"../imageFiles/DoubleWin/tpl1660644049110.png", record_pos=(0.401, -0.214), resolution=(2208, 1242))
# 小猪
DW_pigClose = Template(r"../imageFiles/DoubleWin/tpl1660645295994.png", record_pos=(0.394, -0.206), resolution=(2208, 1242))
# Felling Lucky
DW_LuckyClose = Template(r"../imageFiles/DoubleWin/tpl1660706907882.png", record_pos=(0.351, -0.249), resolution=(2208, 1242))
# ready to pick 关闭 067
DW_pickClose = Template(r"../imageFiles/DoubleWin/tpl1660716162383.png", record_pos=(0.292, -0.167), resolution=(2224, 1668))

# BLUESTART 046机器不会自动 过滤 蓝色的START按键进行FREE SPIN
DW_BLUESTART = Template(r"../imageFiles/DoubleWin/BLUESATRT_46.png", record_pos=(0.002, 0.173), resolution=(1136, 640))

# 123基准图片，其他各设备也出现了该问题 GET A PERSINALIZED EXPERIENCE
# 这个点击之后，会有一个ios的弹框，需要点取消
DW_continue_button = Template(r"../imageFiles/DoubleWin/tpl1661393332219.png", record_pos=(0.093, 0.107), resolution=(2778, 1284))
# 182基准图篇，spin过程中有个collect
DW_collect_free_spin = Template(r"../imageFiles/DoubleWin/tpl1661500068041.png", record_pos=(-0.001, 0.141), resolution=(2436, 1125))

######################
############################            ###############################
############################  Whispers  ###############################
############################           ###############################
#######################
# 登录 继续
WS_facebook_continue = Template(r"../imageFiles/Whispers/tpl1662538211709.png", record_pos=(0.171, 0.664), resolution=(1284, 2778))
WS_facebook_continue_067 = Template(r"../imageFiles/Whispers/tpl1663049664946.png", record_pos=(0.08, 0.101), resolution=(1668, 2224))
# 游戏首页
WS_gameHome = Template(r"../imageFiles/Whispers/tpl1662453736072.png", record_pos=(0.005, -0.543), resolution=(1284, 2778))
# 游戏首页那个男人的对话框
WS_LIBRARIAN = Template(r"../imageFiles/Whispers/tpl1662542754212.png", record_pos=(-0.227, 0.083), resolution=(1284, 2778))
# 进入主界面就有一个叉叉
WS_close_1_open = Template(r"../imageFiles/Whispers/tpl1662452681762.png", record_pos=(0.002, 0.364), resolution=(1284, 2778))

# 067 的叉叉
WS_close_2_open = Template(r"../imageFiles/Whispers/tpl1663048734911.png", record_pos=(0.001, 0.576), resolution=(1668, 2224))
# claim按钮
WS_claim = Template(r"../imageFiles/Whispers/tpl1662452780696.png", record_pos=(-0.002, 0.653), resolution=(1284, 2778))
# sexy lover img
WS_sexy_lover_img = Template(r"../imageFiles/Whispers/tpl1662454059646.png", record_pos=(-0.105, -0.067), resolution=(1284, 2778))
# continue button
WS_continue_img = Template(r"../imageFiles/Whispers/tpl1662454154333.png", record_pos=(-0.003, 0.731), resolution=(1284, 2778))
# 暂停按钮
WS_pause_button_img = Template(r"../imageFiles/Whispers/tpl1662458480326.png", record_pos=(-0.001, -0.991), resolution=(1284, 2778))
# Quit 按钮
WS_quit_button_img = Template(r"../imageFiles/Whispers/tpl1662458804748.png", record_pos=(-0.213, 0.918), resolution=(1284, 2778))
# my页面的homepage
WS_my_homepage = Template(r"../imageFiles/Whispers/tpl1662620757643.png", record_pos=(0.298, -0.433), resolution=(1284, 2778))

# 左上角logo
WS_whisper_logo = Template(r"../imageFiles/Whispers/tpl1662543456318.png", record_pos=(-0.34, -0.921), resolution=(1284, 2778))
# Settings这个文字图案
WS_settings_img = Template(r"../imageFiles/Whispers/tpl1662461138961.png", record_pos=(-0.358, 0.093), resolution=(1284, 2778))
# Logout
WS_logout_button_img = Template(r"../imageFiles/Whispers/tpl1662461662679.png", record_pos=(0.343, -0.322), resolution=(1284, 2778))
# Logout 确认按钮
WS_confirm_logout = Template(r"../imageFiles/Whispers/tpl1662461848917.png", record_pos=(0.199, 0.224), resolution=(1284, 2778))
WS_close_logout = Template(r"../imageFiles/Whispers/tpl1662461952198.png", record_pos=(-0.418, -0.926), resolution=(1284, 2778))
# log in 按钮
WS_login_img = Template(r"../imageFiles/Whispers/tpl1662462032499.png", record_pos=(0.315, -0.648), resolution=(1284, 2778))
# facebook 登录
WS_facebook_login = Template(r"../imageFiles/Whispers/tpl1662462146345.png", record_pos=(-0.175, 0.602), resolution=(1284, 2778))
WS_facebook_login_1 = Template(r"../imageFiles/Whispers/tpl1662718051277.png", record_pos=(-0.179, 0.412), resolution=(1242, 2208))  # 046
WS_facebook_login_2 = Template(r"../imageFiles/Whispers/tpl1663049467225.png", record_pos=(-0.162, 0.282), resolution=(1668, 2224))  # 067

# 付费模式，点击加号
WS_add_key_buy = Template(r"../imageFiles/Whispers/tpl1662531426821.png", record_pos=(0.075, -0.911), resolution=(1284, 2778))
# 点击美元符号
WS_money_img = Template(r"../imageFiles/Whispers/tpl1662531785211.png", record_pos=(-0.356, 0.179), resolution=(1284, 2778))
WS_money_img_1 = Template(r"../imageFiles/Whispers/tpl1662721309796.png", record_pos=(-0.336, 0.445), resolution=(640, 1136))
# LIBRARY
WS_LIBRARY_img = Template(r"../imageFiles/Whispers/tpl1662532680835.png", record_pos=(-0.129, 0.943), resolution=(1284, 2778))
## 小搜索按钮
WS_search_small = Template(r"../imageFiles/Whispers/tpl1662532934227.png", record_pos=(-0.422, -0.793), resolution=(1284, 2778))
WS_here_input_text = Template(r"../imageFiles/Whispers/tpl1662532979752.png", record_pos=(-0.213, -0.904), resolution=(1284, 2778))
WS_here_input_text_046 = Template(r"../imageFiles/Whispers/tpl1663037455944.png", record_pos=(-0.298, -0.786), resolution=(640, 1136))
WS_story_name_img = Template(r"../imageFiles/Whispers/tpl1662533268609.png", record_pos=(0.063, -0.744), resolution=(1284, 2778))
# 重置小说
WS_reset_button_img = Template(r"../imageFiles/Whispers/tpl1662533960226.png", record_pos=(0.432, 0.989), resolution=(1284, 2778))
WS_reset_story_img = Template(r"../imageFiles/Whispers/tpl1662534377027.png", record_pos=(0.004, 0.165), resolution=(1284, 2778))
WS_play_img = Template(r"../imageFiles/Whispers/tpl1662534632112.png", record_pos=(0.119, 0.855), resolution=(1284, 2778))
# 阅读完一章之后的操作
## 点击小claim
WS_claim_small_img = Template(r"../imageFiles/Whispers/tpl1662536997093.png", record_pos=(0.141, 0.213), resolution=(1284, 2778))
## next Chapter
WS_next_Chapter = Template(r"../imageFiles/Whispers/tpl1662537187406.png", record_pos=(0.216, 0.648), resolution=(1284, 2778))

######################
############################            ###############################
############################  Grand Cash Slots  ###############################
############################           ###############################
#######################

# 此版以123为准
############# 登录界面客服按钮
GC_gamein = Template(r"../imageFiles/GrandCashSlots/tpl1664174054092.png", record_pos=(0.459, -0.194), resolution=(2778, 1284))
# 网络重连 sh-100
GC_RETRY = Template(r"../imageFiles/GrandCashSlots/tpl1664184280268.png", record_pos=(-0.001, 0.142), resolution=(2388, 1668))
############# 游戏界面所有的关闭按钮
GC_close_purple = Template(r"../imageFiles/GrandCashSlots/tpl1664172715589.png", record_pos=(0.335, -0.201), resolution=(2778, 1284))
GC_close_deepPurple = Template(r"../imageFiles/GrandCashSlots/tpl1664172745817.png", record_pos=(0.37, -0.177), resolution=(2778, 1284))
GC_close_dark = Template(r"../imageFiles/GrandCashSlots/tpl1664172764245.png", record_pos=(0.339, -0.202), resolution=(2778, 1284))
GC_close_blue = Template(r"../imageFiles/GrandCashSlots/tpl1664172776609.png", record_pos=(0.375, -0.189), resolution=(2778, 1284))
GC_close_gray = Template(r"../imageFiles/GrandCashSlots/tpl1664172789906.png", record_pos=(0.307, -0.161), resolution=(2778, 1284))
GC_close_1 = Template(r"../imageFiles/GrandCashSlots/tpl1664173645973.png", record_pos=(0.37, -0.182), resolution=(2778, 1284))
GC_close_2 = Template(r"../imageFiles/GrandCashSlots/tpl1664175530235.png", record_pos=(0.37, -0.189), resolution=(2778, 1284))
GC_close_3 = Template(r"../imageFiles/GrandCashSlots/tpl1664273475279.png", record_pos=(0.303, -0.167), resolution=(2436, 1125))  # 182设备
GC_close_red = Template(r"../imageFiles/GrandCashSlots/tpl1664181008672.png", record_pos=(0.378, -0.143), resolution=(2778, 1284))
GC_close_smallred = Template(r"../imageFiles/GrandCashSlots/tpl1664261979389.png", record_pos=(0.269, -0.134), resolution=(2778, 1284))
GC_close_067 = Template(r"../imageFiles/GrandCashSlots/tpl1664344713914.png", record_pos=(0.423, -0.212), resolution=(2224, 1668))
# 购买之后的关闭
GC_close_buy1 = Template(r"../imageFiles/GrandCashSlots/tpl1664182658780.png", record_pos=(0.359, -0.201), resolution=(2778, 1284))
GC_close_buy2 = Template(r"../imageFiles/GrandCashSlots/tpl1664182738030.png", record_pos=(0.36, -0.2), resolution=(2778, 1284))
# 左侧三个点
GC_left_dot = Template(r"../imageFiles/GrandCashSlots/tpl1664181456937.png", record_pos=(-0.436, 0.0), resolution=(2778, 1284))
########### 通过TREASURE判断叉叉
GC_TREASURE = Template(r"../imageFiles/GrandCashSlots/tpl1664175920168.png", record_pos=(0.017, 0.178), resolution=(2778, 1284))
####################### 登录
## 右上角的菜单按钮
GC_menu = Template(r"../imageFiles/GrandCashSlots/tpl1664173233354.png", record_pos=(0.38, -0.211), resolution=(2778, 1284))
GC_menu_067 = Template(r"../imageFiles/GrandCashSlots/tpl1664345779879.png", record_pos=(0.464, -0.35), resolution=(2224, 1668))
##  f | Connect
GC_menu_fb_connect = Template(r"../imageFiles/GrandCashSlots/tpl1664173316166.png", record_pos=(0.307, 0.01), resolution=(2778, 1284))
GC_fb_connect = Template(r"../imageFiles/GrandCashSlots/tpl1664178173875.png", record_pos=(-0.006, 0.186), resolution=(2778, 1284))
GC_fb_continue = Template(r"../imageFiles/GrandCashSlots/tpl1664179191291.png", record_pos=(0.157, 0.666), resolution=(1284, 2778))
# 主界面的各个登录方式
GC_fb_login_logo = Template(r"../imageFiles/GrandCashSlots/tpl1664179388128.png", record_pos=(-0.035, 0.141), resolution=(2778, 1284))
GC_IOS_login_logo = Template(r"../imageFiles/GrandCashSlots/tpl1664179419815.png", record_pos=(-0.289, 0.137), resolution=(2778, 1284))
GC_guest_login_logo = Template(r"../imageFiles/GrandCashSlots/tpl1664179427366.png", record_pos=(0.226, 0.14), resolution=(2778, 1284))
## 设置里面进行查看
GC_menu_settings = Template(r"../imageFiles/GrandCashSlots/tpl1664173393779.png", record_pos=(0.297, -0.032), resolution=(2778, 1284))
##############  登录之后进入游戏
####### 收集按钮
GC_collect = Template(r"../imageFiles/GrandCashSlots/tpl1664180813010.png", record_pos=(0.002, 0.137), resolution=(2778, 1284))
####### 购买按钮
GC_buy = Template(r"../imageFiles/GrandCashSlots/tpl1664173481101.png", record_pos=(-0.045, -0.212), resolution=(2778, 1284))
# 购买的美元符号
# GC_money_button = Template(r"../imageFiles/GrandCashSlots/tpl1664173569169.png", record_pos=(0.254, -0.092), resolution=(2778, 1284))
GC_money_button = Template(r"../imageFiles/GrandCashSlots/tpl1667453363999.png", record_pos=(0.077, -0.039), resolution=(2778, 1284))
## 青蛙主题
GC_Frog_Theme = Template(r"../imageFiles/GrandCashSlots/tpl1664173803105.png", record_pos=(0.043, -0.094), resolution=(2778, 1284))
GC_choose_level = Template(r"../imageFiles/GrandCashSlots/tpl1664183858443.png", record_pos=(0.053, 0.068), resolution=(2778, 1284))
GC_choose_level_1 = Template(r"../imageFiles/GrandCashSlots/tpl1664262545422.png", record_pos=(0.022, 0.068), resolution=(2778, 1284))
GC_spin = Template(r"../imageFiles/GrandCashSlots/tpl1664184826705.png", record_pos=(0.32, 0.191), resolution=(2778, 1284))
GC_spin_close1 = Template(r"../imageFiles/GrandCashSlots/tpl1664185743515.png", record_pos=(0.376, -0.202), resolution=(2778, 1284))
GC_spin_close2 = Template(r"../imageFiles/GrandCashSlots/tpl1664185859702.png", record_pos=(0.37, -0.174), resolution=(2778, 1284))
# SH-100的
GC_START = Template(r"../imageFiles/GrandCashSlots/tpl1664186199226.png", record_pos=(0.003, 0.149), resolution=(2388, 1668))
GC_spin_collect = Template(r"../imageFiles/GrandCashSlots/tpl1664186442513.png", record_pos=(0.0, 0.126), resolution=(2778, 1284))
# SH-100
GC_spin_YES = Template(r"../imageFiles/GrandCashSlots/tpl1664186749685.png", record_pos=(0.121, 0.135), resolution=(2388, 1668))
# sh-123
GC_buy_SALE = Template(r"../imageFiles/GrandCashSlots/tpl1667445427599.png", record_pos=(-0.046, -0.204), resolution=(2778, 1284))
