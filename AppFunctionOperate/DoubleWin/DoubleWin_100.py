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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--DoubleWin_0100 ", *args, **kwargs)


################# 游戏内操作
def login(devices, c, ios, facebook=True):
    print("开始登录的各种操作")
    sign = 0
    while True:
        sign += 1
        if sign > 15:
            break
        try:
            sleep(15)
            print(devices, "第一步，判断主页面的左侧图片是否存在")
            if exists(DW_game_home):  # 判断主页面的左侧图片是否存在
                break
        except:
            # 点击ok
            print("点击ok进行下载")
            # click([0.502, 0.71])  # 0186
            traceback.print_exc()

    while True:
        sign += 1
        try:
            print(devices, "第二步,准备点击首页的facebook登录按钮")
            if exists(DW_fb_button_123):  # 判断首页的facebook登录按钮
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
            print(devices, "第三步,进行登录操作")
            if facebook == True:
                if exists(DW_game_home):
                    # 根据相对坐标进行登录
                    try:
                        touch(DW_fb_button_123)
                        print("点击facebook登录")
                        time.sleep(2)
                    except:
                        pass

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

                # if c.xpath('//*[@label="继续"]').exists:
                #     print("继续里")
                #     c.xpath('//*[@label="继续"]').click()
                #     c.close()
                #     sleep(5)

            else:
                ####游客登录
                if exists(DW_game_home):
                    # click([0.76, 0.85])  # 相对 ios14以下
                    click([0.69, 0.84])  ### 相对坐标，ios14以上
                print("游客登录")

                if exists(DW_game_home) is False:
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
                print("点击继续")
                c.xpath('//*[@label="继续"]').click()
                break
        except:
            traceback.print_exc()
    c.close()


def alert_click_1():
    play_in_list = [DW_red_quit_1, DW_red_quit_2, DW_red_quit_3, DW_red_quit_4, DW_red_quit_5,
                    DW_ad_close_1, DW_collect_and_play]
    n = 0
    while True:
        try:
            if avent.is_set():
                for i in play_in_list:
                    try:
                        if avent.is_set():
                            if i == DW_collect_and_play:
                                if exists(i):
                                    touch(i)
                                    click([0.9, 0.1])  # 叉叉点完都要点一下[0.9,0.1]的位置的相对坐标

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


def break_sign():
    while 1:
        print("判断buy是否存在", 22222222)
        print("break_sign")
        if exists(DW_clear_buy):
            break
        if exists(DW_clear_buy_1):
            break
    avent.clear()
    bvent.clear()
    cvent.clear()
    dvent.clear()
    event.clear()


def player_in():
    print("进入游戏的阶段,线程起")
    avent.set()
    bvent.set()
    cvent.set()
    dvent.set()
    event.set()

    if exists(DW_red_quit_1):  # 如果存在红色的退出按钮，则点击
        touch(DW_red_quit_1)

    from threading import Thread
    t1 = Thread(target=alert_click_1)  # 弹窗点击
    t2 = Thread(target=break_sign)
    t1.setDaemon(True)
    t1.start()
    t2.setDaemon(True)
    t2.start()

    t1.join()
    t2.join()


def theme_game(c, ios, n):
    print("游戏阶段")
    while True:
        if exists(DW_lionIcon):
            print("点击了狮子头关卡图标")
            touch(DW_lionIcon)
            time.sleep(30)
            try:
                touch(DW_lionIcon)
            except:
                pass
            print("----------进入了狮子头关卡------------")
            break
        elif exists(DW_spinButton):
            break
        else:
            # swipe([0.5, 0.78], [0.5, 0.13])
            print("---------------------向左滑动！-------------------------")
            # swipe([0.3, 0.5], [0.85, 0.5])  # 左滑
            swipe([0.85, 0.5], [0.3, 0.5])  # 右滑

    while True:
        try:
            print("game in 点击蓝色块.....")
            # 选择关卡
            if exists(DW_blueLevel):
                touch(DW_blueLevel)
            elif exists(DW_spinButton):
                break
            else:
                try:
                    touch(DW_lionIcon)
                except:
                    pass

            if exists(DW_lionIcon) is False:
                print("开始玩耍游戏了")
                break
            else:
                continue
        except:
            traceback.print_exc()

    print("进入多线程阶段开始spin")
    avent.set()
    avent.set()
    bvent.set()
    cvent.set()
    dvent.set()
    event.set()
    # wp.set()

    from threading import Thread
    t1 = Thread(target=theme_game_click_1)
    t2 = Thread(target=theme_game_click_2, args=(c, ios,))
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
            if exists(DW_spinButton):
                try:
                    touch(DW_spinButton)
                except:
                    pass

            if exists(DW_levelUpClose):
                touch(DW_levelUpClose)
                continue

            if exists(DW_levelUpClose_067):
                touch(DW_levelUpClose_067)
                continue

            if exists(DW_BLUESTART):
                touch(DW_BLUESTART)


        else:
            break


def theme_game_click_2(c, ios):
    ###  这个线程用来关闭spin过程中可能会出现的异常情况
    while 1:
        if bvent.is_set():
            print("点击关闭")

            if exists(DW_continue_button):
                touch(DW_continue_button)
                try:
                    if ios.alert_exists():
                        ios.alert_accept()
                        c.close()
                except:
                    pass
                continue

            if exists(DW_levelUpClose):
                touch(DW_levelUpClose)
                continue

            elif exists(DW_levelUpClose_067):
                touch(DW_levelUpClose_067)
                continue

            elif exists(DW_happyClose):
                touch(DW_happyClose)
                continue

            elif exists(DW_pigClose):
                touch(DW_pigClose)
                continue

            elif exists(DW_LuckyClose):
                touch(DW_LuckyClose)
                continue

            elif exists(DW_pickClose):
                touch(DW_pickClose)
                continue

            elif exists(DW_collect_free_spin):
                touch(DW_collect_free_spin)
                continue

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
        if exists(DW_clear_buy):
            touch(DW_clear_buy)
            print("点击购买按钮成功")

        if exists(DW_buy_button):
            touch(DW_buy_button)
            print("点击购买按钮成功")

    except:
        traceback.print_exc()

    while 1:
        try:
            print("状态：", c.status())
            if exists(DW_money_button):  # 如果存在USD付款按钮，则点击
                touch(DW_money_button)
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
        if quitFlag > 8:
            break
        if exists(DW_money_Ok):
            touch(DW_money_Ok)
            quitFlag += 1

        if exists(DW_vip_YEAH):
            touch(DW_vip_YEAH)
            quitFlag += 1

        if exists(DW_money_quit):
            touch(DW_money_quit)
            quitFlag += 1

        quitFlag += 1
