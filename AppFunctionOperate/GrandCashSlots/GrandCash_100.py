# -*- coding: utf-8 -*-
'''
@Time : 2022/9/23 16:28
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : GrandCash_123.py
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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--GrandCash_0100 ", *args, **kwargs)


def login(device, packageName, c, ios):
    ################## 进入主界面需要进行授权点击
    print("-------------------进行第四个测试用例---------------------")
    c.app_start(packageName)
    sleep(10)
    ###判断app是否在运行
    app = ios.app_state(packageName)["value"]
    time.sleep(10)
    if app == 4:
        for i in range(8):
            print("点击接受")
            if ios.alert_exists():
                print("点击接受111111111")
                ios.alert_accept()
                time.sleep(0.5)
    if c.alert.exists:
        buttons = c.alert.buttons()
        c.alert.click(buttons)
        print("弹框关闭")
    print("开始登录的各种操作")
    ###############  等待资源更新
    while True:
        if exists(GC_gamein):
            if exists(GC_RETRY):
                touch(GC_RETRY)
            time.sleep(5)
        else:
            break
    ############# 进入游戏，点击关闭叉叉
    close_list = [GC_close_067, GC_close_red, GC_close_purple, GC_close_deepPurple, GC_close_dark, GC_close_blue, GC_close_gray, GC_close_1,
                  GC_close_2, GC_collect]
    quit_close_flag = 0
    while True:
        for close_button in close_list:
            if exists(close_button):
                touch(close_button)
                print("---------------点击叉叉-------------")
                time.sleep(1)
        for i in range(4):
            click([0.95, 0.03])  # 点击右上角空白处,跳过引导
        quit_close_flag += 1
        print(f"-------quit_close_flag--------{quit_close_flag}-------------")
        if quit_close_flag > 2:
            break
    ################# 进行游戏登录
    #### 先判断facebook是否登录，如果登录了，就进行退出
    # 点击菜单
    while True:
        print("点击menu中的facebook登录...")
        try:
            if exists(GC_menu_067):
                touch(GC_menu_067)
                time.sleep(5)
        except:
            pass
        # 如果存在logout,则点击，并进行登录
        # 如果存在 f | Connect 则直接点击登录
        if exists(GC_menu_fb_connect):
            touch(GC_menu_fb_connect)
            time.sleep(5)
        if exists(GC_fb_connect):
            touch(GC_fb_connect)
            time.sleep(2)
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
        if exists(GC_fb_login_logo):
            break
        if exists(GC_fb_continue):
            break

    while 1:
        print('--------进行跳转facebook登录-------')
        if exists(GC_fb_login_logo):
            break
        try:
            if c.xpath('//*[@label="继续"]').exists:
                print("点击继续")
                c.xpath('//*[@label="继续"]').click()
                sleep(8)
                c.close()
                break
            if exists(GC_fb_continue):
                touch(GC_fb_continue)
                break
        except:
            traceback.print_exc()
        finally:
            c.close()

    while True:
        print("------主界面进行facebook点击登录...")
        if exists(GC_fb_login_logo):
            touch(GC_fb_login_logo)
            print("GrandCashSlots - facebook登录成功")
            iosScreenshot(device, 'GrandCashSlots-facebook登录成功')
            time.sleep(5)
            break
        else:
            iosScreenshot(device, 'GrandCashSlots-facebook登录失败')
            time.sleep(10)


def pay(device, c, password):
    close_list = [GC_collect, GC_close_red, GC_close_purple, GC_close_deepPurple,
                  GC_close_dark, GC_close_blue, GC_close_gray, GC_close_1, GC_close_2]
    while True:
        for close in close_list:
            if exists(close):
                touch(close)
                time.sleep(1)
        if exists(GC_left_dot):
            time.sleep(1)
            if exists(GC_buy) or exists(GC_buy_SALE):
                print("--------------存在左边的三个小点和Buy按钮,退出叉叉点击操作---------------")
                break
    ################# 点击buy进行付款
    flag_pay = 0
    while True:
        try:
            print(f'----点击buy进行付款----{flag_pay}')
            if flag_pay:
                print("--------点击付款--------------")
                break
            if exists(GC_buy):
                touch(GC_buy)
                flag_pay = 1
            if exists(GC_buy_SALE):
                touch(GC_buy_SALE)
                flag_pay = 1
            time.sleep(3)
        except:
            iosScreenshot(device, 'GC_点击充值失败')

    while True:
        # 进行充值
        try:
            print('--------进行充值-----------')
            print("状态：", c.status())
            if exists(GC_money_button):  # 如果存在 $ 付款按钮，则点击
                touch(GC_money_button)
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
            # try:
            #     print("屏幕会话", c.orientation)
            # except:
            #     pass
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
    close_buy_list = [GC_collect, GC_close_buy1, GC_close_buy2, GC_close_purple, GC_close_smallred, GC_collect]
    # 支付成功之后的操作
    quitFlag = 0
    while True:
        for close in close_buy_list:
            try:
                touch(close)
                time.sleep(3)
            except:
                pass
        quitFlag += 1
        print('quitFlag：', quitFlag, '------------------')
        if quitFlag > 2:
            break
        if exists(GC_left_dot):
            break


def play_game_spin(n):
    # 前面已经付款了，付款成功之后，直接在主界面
    # 主界面我们需要手指朝左边滑动，找到青蛙主题的头像
    while True:
        if exists(GC_Frog_Theme):
            touch(GC_Frog_Theme)
            break
        else:
            swipe([0.7, 0.5], [0.5, 0.5])  # 屏幕内容朝左滚动

    while True:
        if exists(GC_choose_level):
            touch(GC_choose_level)
            time.sleep(5)
        if exists(GC_choose_level_1):
            touch(GC_choose_level_1)
            time.sleep(5)
        if exists(GC_spin):
            break
        else:
            print('没找到青蛙主题里面的等级选择...')
            time.sleep(5)

    print("进入多线程阶段开始点击spin")
    avent.set()
    bvent.set()

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
    #### 这个线程用来spin
    while 1:
        if avent.is_set():
            print("点击spin")
            if exists(GC_spin):
                touch(GC_spin)
            else:
                click([0.5, 0.5])
        else:
            break


def theme_game_click_2():
    ###  这个线程用来关闭spin过程中可能会出现的异常情况
    while 1:
        if bvent.is_set():
            print("点击关闭")
            if exists(GC_START):
                touch(GC_START)
            elif exists(GC_spin_collect):
                touch(GC_spin_collect)
            elif exists(GC_spin_close1):
                touch(GC_spin_close1)
            elif exists(GC_spin_close2):
                touch(GC_spin_close2)
            elif exists(GC_spin_close2):
                touch(GC_spin_close2)
            elif exists(GC_close_purple):
                touch(GC_close_purple)
            elif exists(GC_spin_YES):
                touch(GC_spin_YES)
            elif exists(GC_collect):
                touch(GC_collect)
        else:
            break


def time_stop(n):
    print("----启动时间监控-----")
    sleep(60 * n)
    print("---------时间到了，灭霸响指，啪----------")
    avent.clear()
    bvent.clear()
