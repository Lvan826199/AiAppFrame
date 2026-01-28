# -*- coding: utf-8 -*-
'''
@Time : 2022/10/8 13:58
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : BingoJourney_046.py
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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--BingoJourney_0182 ", *args, **kwargs)


def login(devices, c, ios, facebook=True):
    print("开始登录的各种操作")
    sign = 0
    n = 0
    while True:
        sign += 1
        if sign > 15:
            break
        try:
            sleep(15)
            print(devices, "第一步")
            if exists(BJ_game_ok):  # 热更新下载的内容
                touch(BJ_game_ok)
            if exists(BJ_game_home):  # 判断主页面的左侧图片是否存在
                break
        except:
            # 点击ok
            print("点击ok进行下载")
            click([0.502, 0.71])  # 0186
            traceback.print_exc()

    while True:
        sign += 1
        try:
            print(devices, "第二步")
            if exists(BJ_game_ok):  # 热更新下载的内容
                touch(BJ_game_ok)
            if exists(BJ_alert):  # 网络重新连接的一个弹窗，如果存在，则点击确定
                touch(BJ_alert)
                print("2.1")
            if exists(BJ_fb_button_192):  # ios14以上是这个facebook登录按钮
                print("-----facebook登录按钮存在------")
                break
            if exists(BJ_fb_button):  # 点击首页的facebook登录按钮
                print("-----facebook登录按钮存在------")
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
            if exists(BJ_alert):
                touch(BJ_alert)
            if facebook == True:
                if exists(BJ_game_home):
                    # 根据相对坐标进行登录
                    click([0.535, 0.855])  #### 相对坐标0186
                    print("点击facebook登录")
                print("FB登录")
                if ios.alert_exists():
                    ios.alert_accept()
                    c.close()
                    sleep(15)
                if c.xpath('//*[@label="打开"]').exists:
                    c.xpath('//*[@label="打开"]').click()
                    sleep(8)
                    c.close()
                    sleep(8)
                    break
                if c.xpath('//*[@label="继续"]').exists:
                    print("点击继续")
                    c.xpath('//*[@label="继续"]').click()
                    c.close()
                    sleep(5)
            else:
                ####游客登录
                if exists(BJ_game_home):
                    click([0.76, 0.85])  # 相对 0186
                print("游客登录")
                if exists(BJ_game_home) is False:
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


def alert_click_1(devices):
    play_in_list = [BJ_red_quit_1, BJ_red_quit_2, BJ_brown_quit_1, BJ_red_quit_3, BJ_red_quit_4, BJ_red_quit_5, BJ_red_quit_6, BJ_red_quit_7]
    n = 0
    while True:
        try:
            print(devices, 11111)
            print(devices, "alert_click_1")
            if avent.is_set():
                for i in play_in_list:
                    try:
                        print(devices, 11111)
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
        print(3333333333)
        if bvent.is_set():
            try:
                if exists(BJ_hawaii):
                    touch(BJ_hawaii)
                if exists(BJ_claim):
                    touch(BJ_claim)
                if exists(BJ_continueImg):
                    touch(BJ_continueImg)
            except:
                traceback.print_exc()
        else:
            break


def break_sign(devices):
    while 1:
        print(devices, 22222222)
        print(devices, "break_sign")
        if exists(BJ_hawaii):
            break
        elif exists(BJ_update_level):
            break
        else:
            for i in range(3):
                swipe([0.5, 0.78], [0.5, 0.13])
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
    if exists(BJ_red_quit_1):  # 如果存在红色的退出按钮，则点击
        touch(BJ_red_quit_1)
    from threading import Thread
    t1 = Thread(target=alert_click_1, args=(devices,))  # 弹窗点击
    t2 = Thread(target=break_sign, args=(devices,))
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


def theme_game(n):
    print("游戏阶段")
    while True:
        if exists(BJ_hawaii):
            print("点击了HAWAII关卡图标")
            touch(BJ_hawaii)

        if exists(BJ_claim):
            touch(BJ_claim)

        if exists(BJ_update_level):
            print("屏幕中间的像减音量的按键存在则退出！")
            break
        else:
            for i in range(3):
                swipe([0.5, 0.78], [0.5, 0.13])

    while True:
        try:
            print("game in .....")
            click([0.407, 0.46])  ##0186
            if exists(BJ_update_level) is False:
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
            if exists(BJ_round_1) is False:
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
    import subprocess
    while 1:
        if avent.is_set():
            print("点击开始11111")
            # click([220,50])
            click([0.17, 0.312])
            click([0.17, 0.445])
            click([0.17, 0.528])
            click([0.17, 0.697])
            click([0.17, 0.804])
            print("点击结束")
        else:
            break


def theme_game_click_2():
    while 1:
        if bvent.is_set():
            print("点击开始2222222222222")
            click([0.618, 0.324])
            click([0.618, 0.445])
            click([0.618, 0.528])
            click([0.618, 0.697])
            click([0.618, 0.804])
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
    time.sleep(5)
    try:
        if exists(BJ_hawaii):
            touch(BJ_hawaii)

        if exists(BJ_claim):
            touch(BJ_claim)

        if exists(BJ_continueImg):
            touch(BJ_continueImg)

    except:
        traceback.print_exc()

    click([0.15, 0.157])  # 0186
    print("购买按钮")
    while 1:
        try:
            print("状态：", c.status())
            if exists(BJ_account_bt):  # 如果存在USD付款按钮，则点击
                touch(BJ_account_bt)
            if c.is_ready():
                print("进行付款")
                if c.xpath('//*[@label="购买"]').exists:
                    c.xpath('//*[@label="购买"]').click_exists(5)
                    c.close()
                    sleep(5)
                elif c.xpath('//*[@label="消费"]').exists:
                    c.xpath('//*[@label="消费"]').click_exists(5)
                    c.close()
                    sleep(5)
            if c.is_ready():
                print("输入密码")
                if c.xpath('//*[@label=""]').exists:
                    c.xpath('//*[@label=""]').set_text(password)
                    c.close()
                    sleep(3)
            if c.is_ready():
                print("登录付费")
                if c.xpath('//*[@label="登录"]').exists:
                    c.xpath('//*[@label="登录"]').click_exists(5)
                    c.close()
                    sleep(2)
            print("屏幕会话", c.orientation)
            c.close()
            # c.close()
            if c.is_ready():
                print("购买完成点击弹窗确认")
                if c.alert.exists:
                    print(c.alert.text)
                    alert = c.alert.buttons()
                    print("按钮弹框：", alert)
                    if len(alert) > 0:
                        print("点击接受弹窗按钮")
                        # c.alert_click(alert)
                        c.alert.accept()
                        c.close()
                        break
        except:
            traceback.print_exc()
