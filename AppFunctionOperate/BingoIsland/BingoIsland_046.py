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
from common.BingoIslandImgs import *
from airtest.core.api import *

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


# ### 设置airtest的日志输出等级,调试时可以注释或者调为INFO
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--BingoIsland_046 ", *args, **kwargs)


def login(device, packageName, c, ios):
    c.app_start(packageName)
    sleep(10)
    ###判断app是否在运行
    app = ios.app_state(packageName)["value"]
    if app == 4:
        for i in range(3):
            if ios.alert_exists():
                ios.alert_accept()
    print("进行facebook登录...")
    while True:
        if exists(BIS_homeReconnect):
            touch(BIS_homeReconnect)
        if exists(BIS_homeHaveAnCount):
            touch(BIS_homeHaveAnCount)
            time.sleep(1)
            try:
                touch(BIS_homeFacebook)
                break
            except:
                pass

    # 进行facebook登录
    while True:
        if c.xpath('//*[@label="继续"]').exists:
            print("继续里")
            c.xpath('//*[@label="继续"]').click()
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
    while True:
        print("facebook登录点击继续")
        if exists(BIS_facebookContinue):
            touch(BIS_facebookContinue)
            print("facebook登录成功")
            iosScreenshot(device, 'BingoIsland-facebook登录成功')
            break
    time.sleep(18)

    for i in range(3):
        if ios.alert_exists():
            ios.alert_accept()
            time.sleep(2)

    close_button_list = [BIS_close_046_1_red]
    while True:
        if exists(BIS_payGold):
            break
        else:
            for i in close_button_list:
                if exists(i):
                    try:
                        touch(i)
                    except:
                        pass


def theme_game(n):
    print("游戏阶段")
    while True:
        if exists(BIS_palyHouse):
            print("点击了游戏关卡的房子")
            touch(BIS_palyHouse)
        if exists(BIS_palyNow):
            break
        if exists(BIS_palyfree):
            break

    while True:
        try:
            print("game in .....")
            if exists(BIS_palyNow):
                touch(BIS_palyNow)
            if exists(BIS_paly2card):
                touch(BIS_paly2card)
                print("点击进行两个卡片的")
            if exists(BIS_palyfree):
                touch(BIS_palyfree)
                break
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
    x = [0.215, 0.272, 0.391, 0.455, 0.533, 0.577, 0.645, 0.701]
    y = [0.384, 0.518, 0.631, 0.75, 0.884]
    while 1:
        if avent.is_set():
            print("点击开始11111")
            for x_coordinate in x:
                for y_coordinate in y:
                    click([y_coordinate, x_coordinate])
            print("点击结束11111")
        else:
            break


def theme_game_click_2():
    x = [0.215, 0.272, 0.391, 0.455]
    y = [0.384, 0.518, 0.631, 0.75, 0.884]
    while 1:
        if avent.is_set():
            print("点击开始22222")
            for x_coordinate in x:
                for y_coordinate in y:
                    click([x_coordinate, y_coordinate])
            print("点击结束2222")
            if exists(BIS_PAYNoThanks):
                touch(BIS_PAYNoThanks)
            if exists(BIS_PlayAgain):
                touch(BIS_PlayAgain)
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


def pay(device, c, password):
    for i in range(3):
        try:
            if exists(BIS_PAYCLOSERED):
                touch(BIS_PAYCLOSERED)
        except:
            pass
    flag_pay = 0
    while True:
        try:
            print(f'----点击皇冠金币进行付款----{flag_pay}')
            if flag_pay:
                print("--------点击付款--------------")
                break
            if exists(BIS_payGold):
                touch(BIS_payGold)
                flag_pay = 1
            time.sleep(3)
        except:
            iosScreenshot(device, 'BIS_点击皇冠金币失败')

    while True:
        # 进行充值
        try:
            print('--------进行充值-----------')
            print("状态：", c.status())
            if exists(BIS_payMoney):  # 如果存在 $ 付款按钮，则点击
                touch(BIS_payMoney)
                time.sleep(5)
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
                    sleep(5)
            if c.is_ready():
                print("登录付费")
                if c.xpath('//*[@label="登录"]').exists:
                    c.xpath('//*[@label="登录"]').click_exists(5)
                    c.close()
                    sleep(2)
            c.close()
            if c.is_ready():
                print("购买完成点击弹窗确认")
                if c.alert.exists:
                    print(c.alert.text)
                    alert = c.alert.buttons()
                    print("按钮弹框：", alert)
                    if len(alert) > 0:
                        print("点击接受弹窗按钮")
                        c.alert.accept()
                        c.close()
                        break
        except:
            iosScreenshot(device, 'GC_充值付款失败')
            traceback.print_exc()
    ############ 付款成功之后需要关闭一些东西
    close_buy_list = [BIS_PAYCLAIM, BIS_PAYCLOSERED, BIS_PAYNoThanks]
    # 支付成功之后的操作
    quitFlag = 0
    while True:
        for close in close_buy_list:
            try:
                if close == BIS_PAYNoThanks:
                    touch(close)
                    break
                else:
                    touch(close)
                    time.sleep(2)
            except:
                pass
        quitFlag += 1
        print('quitFlag：', quitFlag, '------------------')
        if quitFlag > 2:
            break
