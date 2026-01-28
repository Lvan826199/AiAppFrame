# -*- coding: utf-8 -*-
'''
@Time : 2022/10/8 13:56
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : DoubleWin_046.py
'''
__author__ = "梦无矶小仔"

import sys
import threading
import time
import traceback
from common.screenshot import iosScreenshot

sys.dont_write_bytecode = True
import logging
from common.LuckyHitImgs import *

avent = threading.Event()
bvent = threading.Event()
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
_print = print

### 设置airtest的日志输出等级,调试时可以注释或者调为INFO
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--GoldenFish_0123 ", *args, **kwargs)


################# 游戏内操作
from airtest.core.settings import Settings as ST

ST.FIND_TIMEOUT = 4


def permission_182(c):
    print("进行授权")
    permissionTimes = 0
    for i in range(10):
        print(f"----------{i}---------")
        if c(type="Button", name="允许").exists:
            c(type="Button", name="允许").click()
            time.sleep(1)

        try:
            c(type="Button", name="无线局域网与蜂窝网络", timeout=3).click()
        except:
            time.sleep(1)


def closeOpera(MaxNum: int = 2):
    print("进行关闭.....")
    ############ 付款成功之后需要关闭一些东西
    close_buy_list = [collect_1, close_red_1, press_to_play, Keep_STAMPING, collect_2, close_purple_1, close_red_2, close_red_3, close_purple_2,
                      close_blue_1,
                      collect_3]
    # 支付成功之后的操作
    quitFlag = 0
    while True:
        for close in close_buy_list:
            print("点击关闭按钮.....")
            click([0.5, 0.5])
            # import eventlet  # 导入eventlet这个模块
            # eventlet.monkey_patch()  # 必须加这条代码
            # with eventlet.Timeout(4, False):  # 设置超时时间为3秒
            #     touch(close)
            try:
                touch(close)
            except:
                pass
        quitFlag += 1
        print('quitFlag：', quitFlag, '------------------')
        if quitFlag > MaxNum:
            break


def buy_charge(c, password):
    print("进行付费购买功能测试...")
    time.sleep(10)
    closeOpera(MaxNum=0)
    for i in range(20):
        if exists(saleButton):
            break
        else:
            time.sleep(5)

    for i in range(10):
        if exists(saleButton):
            print("点击saleButton...")
            touch(saleButton)
            time.sleep(3)
        if exists(moneyButton):
            print("点击付费按钮...")
            touch(moneyButton)
            break

    is_click_money = True
    while 1:
        try:
            if is_click_money:
                if exists(moneyButton):  # 点击59.99购买按钮
                    try:
                        touch(moneyButton)
                        is_click_money = False
                    except:
                        pass
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
                    if len(alert) > 0 and alert[-1] == '好':
                        print("点击接受弹窗按钮")
                        # c.alert_click(alert)
                        c.alert.accept()
                        c.close()
                        break
        except:
            pass
    closeOpera()


def theme_game(c, ios, n):
    print("游戏阶段")
    while True:
        print("进入游戏ing...")
        click([0.5, 0.5])
        if exists(play_button):
            touch(play_button)
            break
        if exists(spin_button):
            break

    for i in range(n * 5):
        print("进入spin")
        if exists(spin_button):
            print("开始按spin_button")
            click([0.5, 0.5])
            touch(spin_button, times=5)
            click([0.5, 0.5])
        click([0.5, 0.5])
    print("spin结束")


def loginAccount(c, ios):
    setting_button = None
    for i in range(20):
        print("判断设置按钮是金色还是蓝色")
        if exists(gold_setting_button):
            setting_button = gold_setting_button
        if exists(blue_setting_button):
            setting_button = blue_setting_button
        if setting_button:
            break

    for i in range(30):
        print("进行FaceBook登录.....")
        if exists(setting_button):
            touch(setting_button)
            print("点击了settings按钮....")
        try:
            if exists(gold_settings_text):
                touch(gold_settings_text)
                print("点击了gold_settings_text....")
            if exists(blue_settings_text):
                touch(blue_settings_text)
                print("点击了blue_settings_text....")
        except:
            pass
        if exists(facebook_sign_in):
            touch(facebook_sign_in)
            print("点击了FaceBook登录....")
            break

    for i in range(3):
        print("facebook登录ing......")
        if ios.alert_exists():
            ios.alert_accept()
            c.close()
            sleep(15)
        if c.xpath('//*[@label="打开"]').exists:
            c.xpath('//*[@label="打开"]').click()
            sleep(8)
            c.close()
            sleep(8)
        if c.xpath('//*[@label="继续"]').exists:
            print("点击继续")
            c.xpath('//*[@label="继续"]').click()
            sleep(8)
            c.close()

    closeOpera()
