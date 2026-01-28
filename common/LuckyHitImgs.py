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
# 1、点击SALE
saleButton = Template(r"../imageFiles/LuckyHit/tpl1678958391277.png", record_pos=(0.001, -0.208), resolution=(2778, 1284))
# 2、点击任意金额，进行付款
moneyButton = Template(r"../imageFiles/LuckyHit/tpl1678958732305.png", record_pos=(-0.239, 0.147), resolution=(2778, 1284))
# 3、对付款之后获取的奖品进行确认
collect_1 = Template(r"../imageFiles/LuckyHit/tpl1678958908243.png", record_pos=(-0.002, 0.147), resolution=(2778, 1284), threshold=0.6)
close_red_1 = Template(r"../imageFiles/LuckyHit/tpl1678958950807.png", record_pos=(0.344, -0.203), resolution=(2778, 1284))
press_to_play = Template(r"../imageFiles/LuckyHit/tpl1678959674200.png", record_pos=(-0.003, 0.197), resolution=(2778, 1284))
collect_2 = Template(r"../imageFiles/LuckyHit/tpl1678960724095.png", record_pos=(-0.003, 0.119), resolution=(2778, 1284))
close_card_1 = Template(r"../imageFiles/LuckyHit/tpl1684832090567.png", record_pos=(-0.152, 0.039), resolution=(2778, 1284))
close_card_ok = Template(r"../imageFiles/LuckyHit/tpl1684834845898.png", record_pos=(-0.135, 0.2), resolution=(2778, 1284))
close_card_gold = Template(r"../imageFiles/LuckyHit/tpl1685345139603.png", record_pos=(-0.153, 0.037), resolution=(2778, 1284))
# 4、出现这个叉叉，就结束了，可以进行下一步操作了
close_purple_1 = Template(r"../imageFiles/LuckyHit/tpl1678960784655.png", record_pos=(0.326, -0.191), resolution=(2778, 1284))
close_red_2 = Template(r"../imageFiles/LuckyHit/tpl1678960837514.png", record_pos=(0.476, -0.099), resolution=(2778, 1284))
close_red_3 = Template(r"../imageFiles/LuckyHit/tpl1678960878701.png", record_pos=(0.299, -0.163), resolution=(2778, 1284))
close_purple_2 = Template(r"../imageFiles/LuckyHit/tpl1678961539284.png", record_pos=(0.302, -0.187), resolution=(2778, 1284))
close_blue_1 = Template(r"../imageFiles/LuckyHit/tpl1678961600877.png", record_pos=(0.362, -0.186), resolution=(2778, 1284))
collect_3 = Template(r"../imageFiles/LuckyHit/tpl1678961675685.png", record_pos=(-0.0, 0.176), resolution=(2778, 1284))
gold_setting_button = Template(r"../imageFiles/LuckyHit/tpl1678963644036.png", record_pos=(0.459, -0.21), resolution=(2778, 1284))
blue_setting_button = Template(r"../imageFiles/LuckyHit/tpl1679649602292.png", record_pos=(0.459, -0.21), resolution=(2778, 1284))
gold_settings_text = Template(r"../imageFiles/LuckyHit/tpl1678963676238.png", record_pos=(0.397, -0.043), resolution=(2778, 1284))
blue_settings_text = Template(r"../imageFiles/LuckyHit/tpl1679650117819.png", record_pos=(0.448, -0.256), resolution=(2208, 1242), threshold=0.6)
facebook_sign_in = Template(r"../imageFiles/LuckyHit/tpl1678963723488.png", record_pos=(0.174, 0.075), resolution=(2778, 1284))
play_button = Template(r"../imageFiles/LuckyHit/tpl1678964005996.png", record_pos=(0.176, 0.019), resolution=(2778, 1284))
spin_button = Template(r"../imageFiles/LuckyHit/tpl1679565588778.png", record_pos=(0.251, 0.192), resolution=(2778, 1284))
Keep_STAMPING = Template(r"../imageFiles/LuckyHit/tpl1679644419073.png", record_pos=(-0.003, 0.193), resolution=(2778, 1284))
ad_img = Template(r"../imageFiles/LuckyHit/tpl1679655126746.png", record_pos=(0.011, -0.045), resolution=(2436, 1125))
purple = Template(r"../imageFiles/LuckyHit/tpl1679655134542.png", record_pos=(0.369, -0.189), resolution=(2436, 1125), threshold=0.6)
