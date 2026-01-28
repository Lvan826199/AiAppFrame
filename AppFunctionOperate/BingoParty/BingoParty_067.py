# -*- coding: utf-8 -*-
'''
@Time : 2022/10/8 14:04
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : BingoParty_046.py
'''
__author__ = "梦无矶小仔"

import sys
import threading
import time
import traceback
from common.screenshot import iosScreenshot

sys.dont_write_bytecode = True
import logging
from common.imageElePath import *

event = threading.Event()
avent = threading.Event()
bvent = threading.Event()
cvent = threading.Event()
dvent = threading.Event()
wp = threading.Event()
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
_print = print

### 设置airtest的日志输出等级,调试时可以注释或者调为INFO
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--BingoParty_067 ", *args, **kwargs)


def login(devices, c, ios, facebook=True):
    print("开始登录的各种操作")
    sign = 0
    while True:
        sign += 1
        if sign > 5:
            break
        try:
            sleep(15)
            print(devices, "第一步")
            if exists(BP_gameOk):
                touch(BP_gameOk)
                print("----1点击OK成功---")
            if exists(BP_game_home):  # 判断主页面的左侧图片是否存在
                break
        except:
            traceback.print_exc()

    while True:
        sign += 1
        try:
            print(devices, "第二步")
            if exists(BP_gameOk):
                touch(BP_gameOk)
                # click([0.502,0.66])
                print("----2点击OK成功---")
            if exists(BP_alert):  # 网络重新连接的一个弹窗，如果存在，则点击确定
                touch(BP_alert)
                print("2.1")

            # if exists(BP_re_ct): #网络重新连接的一个弹窗，如果存在，则点击确定
            #     touch(BP_re_ct)
            #     print("2.2")
            # if exists(BP_claim): #网络重新连接的一个弹窗，如果存在，则点击确定
            #     touch(BP_claim)
            if exists(BP_fb_button_067):  # 点击首页的facebook登录按钮
                break
        except Exception as e:
            # print("报错的-------",e)
            traceback.print_exc()
    k_n = 0
    while True:
        k_n += 1
        if k_n > 2:
            break
        try:
            print(devices, "第三步")
            if exists(BP_alert):
                touch(BP_alert)
            if facebook == True:
                if exists(BP_game_home):
                    # 根据坐标进行登录
                    # click([576, 538]) ##### 0046
                    # click([1081, 1040]) #### 0192
                    # click([684, 631]) #### 0011 相对[0.52,0.849]  绝对[684, 631]
                    # click([0.578,0.869]) #### 0186 182 相对[0.578,0.869]  绝对[1102, 701]
                    click([0.578, 0.884])  #### 0100
                    print("点击facebook按钮")
                print("FB登录")
                if ios.alert_exists():
                    ios.alert_accept()
                    c.close()
                    sleep(5)

                if c(type='Link', name='使用 Facebook 应用登录').exists:
                    c(type='Link', name='使用 Facebook 应用登录').click()

                if c.xpath('//*[@label="打开"]').exists:
                    c.xpath('//*[@label="打开"]').click()
                    sleep(5)
                    c.close()
                    sleep(5)
                    break

                if c.xpath('//*[@label="继续"]').exists:
                    print("继续里")
                    c.xpath('//*[@label="继续"]').click()
                    c.close()
                    sleep(5)

            else:
                ####游客登录
                if exists(BP_game_home):
                    # click([857, 560])# ##### 0046
                    # click([1654, 1084])# #####0192
                    # click([987, 651])# #####0011 相对[0.747,0.879]  绝对[987, 651]
                    # click([0.809,0.857])# #####0186 0182 相对[0.809,0.857]  绝对[1431, 709]
                    click([0.809, 0.893])  # #####0100
                    print("------------点击游客登录--------")
                print("游客登录")
                if exists(BP_game_home) is False:
                    break
        except:
            traceback.print_exc()
    c.close()
    sleep(5)
    c_n = 0
    while 1:
        c_n += 1
        if c_n > 2:
            break
        try:
            if c.xpath('//*[@label="继续"]').exists:
                c.xpath('//*[@label="继续"]').click()
                break
        except:
            traceback.print_exc()
    c.close()


def alert_click_1():
    play_in_list = [BP_red_quit_1, BP_red_quit_2, BP_brown_quit_1, BP_red_quit_3, BP_red_quit_4, BP_red_quit_5, BP_red_quit_6, BP_red_quit_7]
    n = 0
    while True:
        try:
            print("----------准备点击游戏界面的关闭按钮-----------")
            print("alert_click_1")
            if avent.is_set():
                for i in play_in_list:
                    try:
                        print("----------点击关闭图标-----------")
                        if avent.is_set():
                            if exists(i):
                                touch(i)
                        else:
                            n = 1
                            break
                    except:
                        traceback.print_exc()
            else:
                break
            if n == 1:
                break
        except:
            traceback.print_exc()


def target():
    while 1:
        print("查找目标关卡BP_hawaii是否出现")
        if bvent.is_set():
            try:
                if exists(BP_hawaii):
                    touch(BP_hawaii)
                # if exists(BP_Venice):
                #     touch(BP_Venice)
                # if exists(BP_claim):
                #     touch(BP_claim)

            except:
                traceback.print_exc()
        else:
            break


def break_sign():
    import random
    while 1:
        print("查找目标关卡BP_hawaii，不存在则滑动")
        print("break_sign")
        x1 = random.randint(247, 929)
        y1 = random.randint(187, 412)
        # click([x1,y1])
        if exists(BP_hawaii):
            break
        elif exists(BP_update_level_button):
            break
        else:
            # swipe([433, 334], [778, 334])
            # swipe([433, 334], [778, 334])
            # for i in range(3):
            #     swipe([433, 334], [778, 334])

            # from poco.drivers.ios import iosPoco
            # # http+usbmux://4438650ca0ef0073a711ae68b7c5fdc629db9772
            # device_ios = connect_device("ios:///http+usbmux://{}".format(devices))
            # poco_ios = iosPoco(device_ios)
            # 如果HAWAII不在，则滑动
            for i in range(10):
                swipe([0.138, 0.5], [0.888, 0.5])

            # sroll = c(enabled="true", visible="true")
            # #print(sroll.exists)
            # sroll.scroll('left')
            # sroll.scroll('left')
            # sroll.scroll('left')

    avent.clear()
    bvent.clear()
    cvent.clear()
    dvent.clear()
    event.clear()


def player_in(devices):
    print("新手进入")
    print("进入游戏的阶段,线程起")
    avent.set()
    bvent.set()
    cvent.set()
    dvent.set()
    event.set()

    if exists(BP_red_quit_1):  # 如果存在红色的退出按钮，则点击
        touch(BP_red_quit_1)

    from threading import Thread
    t1 = Thread(target=alert_click_1, args=(devices,))  # 弹窗点击
    t2 = Thread(target=break_sign)
    t3 = Thread(target=target)
    t1.setDaemon(True)
    t1.start()
    t2.setDaemon(True)
    t2.start()
    t3.setDaemon(True)
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    # x1 = random.randint(75, 1326)
    # y1 = random.randint(1171, 2513)


def theme_game(n):
    print("游戏阶段")
    while True:
        if exists(BP_hawaii):
            print("点击了HAWAII关卡图标")
            touch(BP_hawaii)
        if exists(BP_update_level_button):
            print("屏幕中间的像减音量的按键存在则退出！")
            break
        else:
            # 如果HAWAII不在，则滑动
            for i in range(10):
                swipe([0.13, 0.5], [0.78, 0.5])

    while True:
        try:
            print("game in .....")
            ### 关卡的等级，多少张牌
            # click([254, 354]) #0046
            # click([888, 666]) ##0192
            # click([530, 401]) ##0011 相对[0.406,0.569] 绝对 [530, 401]
            # click([0.406,0.569]) ##0186 182 相对[0.406,0.569] 绝对 [746, 468]
            click([0.537, 0.4])  ##0100 067
            print("--------选择第二张卡牌--------------")
            if exists(BP_update_level) is False:
                print("等待进入")
                break
            else:
                continue
        except:
            traceback.print_exc()

    while True:
        try:
            print("game in .....")
            sleep(2)
            if exists(BP_round_1) is False:
                break
            else:
                continue
        except:
            traceback.print_exc()

    print("进入多线程阶段")
    avent.set()
    avent.set()
    bvent.set()
    cvent.set()
    dvent.set()
    event.set()
    wp.set()

    from threading import Thread
    t1 = Thread(target=theme_game_click_1)
    t2 = Thread(target=theme_game_click_2)
    t3 = Thread(target=time_stop, args=(n,))

    t1.setDaemon(True)
    t1.start()
    t2.setDaemon(True)
    t2.start()
    t3.setDaemon(True)
    t3.start()
    t1.join()
    t2.join()
    t3.join()


def theme_game_click_1():
    while 1:
        if avent.is_set():
            print("点击开始11111")
            # click([220,50])
            click([0.255, 0.189])
            click([0.255, 0.257])
            click([0.255, 0.329])
            click([0.255, 0.389])
            click([0.255, 0.457])
            click([0.402, 0.189])
            click([0.402, 0.257])
            click([0.402, 0.329])
            click([0.402, 0.389])
            click([0.402, 0.457])
            print("点击结束")
        else:
            break


def theme_game_click_2():
    while 1:
        if bvent.is_set():

            print("点击开始2222222222222")
            click([0.588, 0.189])
            click([0.588, 0.257])
            click([0.588, 0.329])
            click([0.588, 0.389])
            click([0.588, 0.457])
            click([0.688, 0.189])
            click([0.688, 0.257])
            click([0.688, 0.329])
            click([0.688, 0.389])
            click([0.688, 0.457])
            print("点击结束")
        else:
            break


def time_stop(n):
    print("启动时间监控")
    sleep(60 * n)
    avent.clear()
    bvent.clear()
    cvent.clear()
    dvent.clear()
    event.clear()


def buy_charge(c, password):
    # click([756, 42]) #点击购买0046
    # click([1044, 77]) #点击购买0192 相对坐标[0.471,0.06]
    # click([637, 50]) #点击购买0011 相对坐标[0.482,0.06]  绝对[637, 50]
    # click([0.477,0.066]) #点击购买0186 0182 相对坐标[0.477,0.066]  绝对[857, 46]
    print("----------------点击购买按钮------------------")
    for i in range(10):
        print("--------067--------准备点击购买按钮------------------")
        if exists(BP_account_bt) is False:
            print("--------067--------点击购买按钮------------------")
            click([0.285, 0.052])  # 点击购买 067
            break
        else:
            time.sleep(1)
    while 1:
        try:
            if exists(BP_account_bt):  # 如果存在USD付款按钮，则点击
                touch(BP_account_bt)
                print("点击购买按钮成功")
                break
        except:
            traceback.print_exc()
    while 1:
        try:
            print("状态：", c.status())
            if c.is_ready():
                print("---------------购买----------")
                # if c(type='Button',name='消费').exists:
                #     c(type='Button', name='消费').click()
                if c.xpath('//*[@label="购买"]').exists:
                    c.xpath('//*[@label="购买"]').click_exists(5)
                    c.close()
                    sleep(5)
                elif c.xpath('//*[@label="消费"]').exists:
                    c.xpath('//*[@label="消费"]').click_exists(5)
                    c.close()
                    sleep(5)
            if c.is_ready():
                print("---------------输入付款密码----------")
                if c.xpath('//*[@label=""]').exists:
                    c.xpath('//*[@label=""]').set_text(password)
                    c.close()
                    sleep(3)
            if c.is_ready():
                print("---------------点击登录并付款----------")
                if c.xpath('//*[@label="登录"]').exists:
                    c.xpath('//*[@label="登录"]').click_exists(5)
                    c.close()
                    sleep(2)
            print("屏幕会话", c.orientation)
            c.close()
            # c.close()
            if c.is_ready():
                print("----------------点击按钮弹框----------")
                if c.alert.exists:
                    print(c.alert.text)
                    alert = c.alert.buttons()
                    print("按钮弹框：", alert)
                    if len(alert) > 0:
                        print("----------------弹框点击接受----------")
                        # c.alert_click(alert)
                        c.alert.accept()
                        c.close()
                        break
        except:
            traceback.print_exc()
