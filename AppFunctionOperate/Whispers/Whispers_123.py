# -*- coding: utf-8 -*-
'''
@Time : 2022/10/8 13:53
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : Whispers_123.py
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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--Whispers_0123 ", *args, **kwargs)


########################## 游戏内操作


def enter_home_page():
    # 通过首页图标进行判断
    while True:
        if exists(WS_gameHome):
            time.sleep(10)
        else:
            break

    while True:
        if exists(WS_LIBRARIAN):
            click([0.5, 0.5])
            break
        else:
            time.sleep(10)
    ### 开始选择小说
    while True:
        if exists(WS_sexy_lover_img):
            touch(WS_sexy_lover_img)
            time.sleep(2)
            if exists(WS_continue_img):
                touch(WS_continue_img)
                time.sleep(10)
                #### 点击退出
                while True:
                    if exists(WS_pause_button_img):
                        touch(WS_quit_button_img)
                        break
                    else:
                        click([0.082, 0.076])
                break


def login(devices, c, ios):
    print("开始登录的各种操作")
    #### 通过坐标点击我的
    for i in range(5):
        click([0.874, 0.932])
        if exists(WS_my_homepage):
            break

    if not exists(WS_login_img):
        for i in range(10):
            if exists(WS_settings_img):
                touch(WS_settings_img)
                try:
                    touch(WS_logout_button_img)
                    time.sleep(2)
                    # 点击yes
                    touch(WS_confirm_logout)
                    time.sleep(10)
                    touch(WS_close_logout)
                    break
                except:
                    print("Logout失败")

            else:
                swipe([0.5, 0.7], [0.5, 0.45])  # 手势小幅度上滑
        # 一系列操作完，进行下滑，找到登录按钮
        for j in range(2):
            swipe([0.5, 0.2], [0.5, 0.8])

    ### 如果存在登录按钮的操作
    if exists(WS_login_img):
        touch(WS_login_img)
        time.sleep(2)

    while True:
        try:
            touch(WS_facebook_login)
            print(devices, "进行FB登录操作")
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
        except:
            traceback.print_exc()
    c.close()
    sleep(5)
    while 1:
        try:
            if c.xpath('//*[@label="继续"]').exists:
                print("点击继续")
                c.xpath('//*[@label="继续"]').click()
                sleep(8)
                c.close()
                break
            if exists(WS_facebook_continue):
                touch(WS_facebook_continue)
                break
        except:
            traceback.print_exc()
    c.close()

    if not exists(WS_login_img):
        print("Whisper登录成功")


def theme_game(n):
    print("游戏阶段")
    while True:
        if exists(WS_LIBRARY_img):
            print("点击了LIBRARY图标")
            touch(WS_LIBRARY_img)
        if exists(WS_search_small):
            break
    while True:
        try:
            print("基本功能运行中....")
            # 选择关卡
            if exists(WS_search_small):
                touch(WS_search_small)

            if exists(WS_here_input_text):
                touch(WS_here_input_text)
                time.sleep(2)
                text("Big Bad Brother", enter=True)
                time.sleep(3)

            if exists(WS_story_name_img):
                touch(WS_story_name_img)
                break
        except:
            traceback.print_exc()

    ##### 进入小说内容的前置操作
    while True:
        ### 判断重置按钮
        if exists(WS_reset_button_img):
            # play 按钮
            click([0.5, 0.712])
            touch(WS_reset_button_img)
        if exists(WS_reset_story_img):
            touch(WS_reset_story_img)
            time.sleep(2)
            if exists(WS_play_img):
                touch(WS_play_img)
                break

    print("进入多线程阶段开始点击")
    avent.set()
    bvent.set()
    cvent.set()
    dvent.set()
    event.set()

    from threading import Thread
    t1 = Thread(target=theme_game_click_1)
    t2 = Thread(target=theme_game_click_2)
    t3 = Thread(target=time_stop, args=(n,))
    t4 = Thread(target=theme_game_click_3)

    t1.setDaemon(True)
    t1.start()
    t2.setDaemon(True)
    t2.start()
    t4.setDaemon(True)
    t4.start()
    t3.setDaemon(True)
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()


def theme_game_click_1():
    #### 这个线程用来点击
    while 1:
        if avent.is_set():
            print("--------第一个------")
            # 中间偏下
            click([0.5, 0.6])
            # 选择衣服的那些
            click([0.5, 0.86])
            # 最终确认
            click([0.5, 0.69])
        else:
            break


def theme_game_click_2():
    ###  这个线程用来关闭spin过程中可能会出现的异常情况
    while 1:
        if bvent.is_set():
            print("--------第二个---------")
            # YES的按钮
            click([0.5, 0.43])
            # 菱形选物体
            click([0.2, 0.585])
            click([0.5, 0.84])
            click([0.5, 0.73])
            # 下一章
            click([0.738, 0.798])
        else:
            break


def theme_game_click_3():
    while True:
        if dvent.is_set():
            print("------第三个-----")
            try:
                if exists(WS_claim):
                    touch(WS_claim)

                if exists(WS_whisper_logo):
                    avent.clear()
                    bvent.clear()
                    cvent.clear()
                    dvent.clear()
                    event.clear()
            except:
                pass
        else:
            break


def time_stop(n):
    print("----启动时间监控-----")
    sleep(60 * n)
    print("---------时间到了，灭霸响指，啪----------")
    avent.clear()
    bvent.clear()
    cvent.clear()
    dvent.clear()
    event.clear()


def buy_charge(c, password):
    time.sleep(5)
    while True:
        if exists(WS_add_key_buy):
            touch(WS_add_key_buy)
            time.sleep(5)
            print("点击购买按钮成功")

        if exists(WS_money_img):
            break

    while 1:
        try:
            print("状态：", c.status())
            if exists(WS_money_img):  # 如果存在 $ 付款按钮，则点击
                touch(WS_money_img)
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
            try:
                print("屏幕会话", c.orientation)
            except:
                pass
            c.close()

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

    # 支付成功之后的操作
    quitFlag = 0
    while True:
        if quitFlag > 7:
            break
        if exists(WS_claim):
            try:
                touch(WS_claim)
            except:
                pass
            quitFlag += 1

        if exists(WS_close_1_open):
            touch(WS_close_1_open)
            quitFlag += 1

        if exists(WS_close_logout):
            touch(WS_close_logout)
            quitFlag += 1

        quitFlag += 1
