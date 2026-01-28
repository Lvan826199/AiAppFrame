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
from common.NorthTowerImgs import *
from airtest.core.api import *

avent = threading.Event()
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
_print = print


# ### 设置airtest的日志输出等级,调试时可以注释或者调为INFO
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--NorthTower_0046 ", *args, **kwargs)


def playGame():
    for i in range(6):
        print(f"进行第{i + 1}轮游戏挑战----")
        if exists(NT_Challenge):
            print("点击了挑战")
            touch(NT_Challenge)
            for i in range(3):
                print(f"点击打怪第{i + 1}轮")
                for i in range(18):
                    click([0.40 + i * 0.01, 0.38])

        if exists(NT_getReward):
            touch(NT_getReward)
            time.sleep(1)
            touch(NT_accept)

        if exists(NT_SettingButton):
            break


def login(packageName, c, ios):
    c.app_start(packageName)
    sleep(10)
    ###判断app是否在运行
    app = ios.app_state(packageName)["value"]
    try:
        c(type="Button", name="下一步").click()
        time.sleep(2)
        c(type="Button", name="开始测试").click()
        time.sleep(15)
    except:
        print("点击下一步失败....")
        traceback.print_exc()
    time.sleep(15)
    if app == 4:
        for i in range(3):
            if ios.alert_exists():
                ios.alert_accept()
    print("授权完毕...")

    #### 进行挑战
    while True:
        print("进入游戏界面....")
        if ios.alert_exists():
            ios.alert_accept()
        if exists(NT_BeginGame):
            try:
                touch(NT_BeginGame)
            except:
                pass
        if exists(NT_Challenge):
            print("进入游戏界面成功")
            break

    #### 判断是否登录appleID
    while True:
        print("判断是否已登录AppleID")
        if exists(NT_SettingButton):
            break
        else:
            print("未登录AppleID，进行游戏...")
            # 进行游戏
            playGame()


def skillsLocation():
    skillsLocationList = []
    y1 = 0.862  # 上排技能
    y2 = 0.947  # 下排技能
    x1 = 0.089  # 左 1
    x2 = 0.232  # 左 2
    x3 = 0.376  # 左 3
    x4 = 0.525  # 左 4

    # 上面第一排技能坐标
    skillsLocationList.append([x1, y1])
    skillsLocationList.append([x2, y1])
    skillsLocationList.append([x3, y1])
    skillsLocationList.append([x4, y1])
    # 第二排技能坐标
    skillsLocationList.append([x1, y2])
    skillsLocationList.append([x2, y2])
    skillsLocationList.append([x3, y2])
    skillsLocationList.append([x4, y2])
    print(skillsLocationList)
    return skillsLocationList


def theme_game(n):
    print("游戏阶段")
    # [0.075,0.943]
    redHouseFlag = 0
    while True:
        try:
            print("game in .....")
            redHouseFlag += 1
            if redHouseFlag == 3:
                print("进入游戏3次失败，点击红房子")
                click([0.075, 0.943])
            if exists(NT_Challenge):
                print("点击了挑战")
                touch(NT_Challenge)
                break
        except:
            traceback.print_exc()

    print("进入多线程阶段")
    avent.set()

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
    skillsLocationList = skillsLocation()
    while 1:
        if avent.is_set():
            print("点击开始11111")
            if exists(NT_NextLevel):
                touch(NT_NextLevel)
            for skillLocaltion in skillsLocationList:
                print(f"点击技能--{skillsLocationList.index(skillLocaltion) + 1}")
                click(skillLocaltion)
            print("点击结束")
        else:
            break


def theme_game_click_2():
    while 1:
        if avent.is_set():
            if exists(NT_getReward):
                touch(NT_getReward)
                print("线程2，点击领取奖励")
            if exists(NT_Challenge):
                touch(NT_Challenge)
                print("线程2，点击下一关")
        else:
            break


def time_stop(n):
    print("启动时间监控")
    sleep(60 * n)
    avent.clear()


def pay(c, password):
    for i in range(3):
        try:
            if exists(NT_levelReward):
                touch(NT_levelReward)
                break
        except:
            pass

    flag_pay = 0
    while True:
        try:
            print(f'----点击加号进行付款----{flag_pay}')
            if exists(NT_addButton):
                touch(NT_addButton)
                flag_pay = 1
            time.sleep(3)
            if exists(NT_D):
                break
            if flag_pay:
                print("--------准备充值--------------")
                break
        except:
            iosScreenshot(device, '点击加号进行付款失败')

    while True:
        # 进行充值
        try:
            print('--------进行充值-----------')
            if exists(NT_Money99):  # 如果存在 99 付款按钮，则点击
                touch(NT_Money99)
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
                    sleep(20)
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
            iosScreenshot(device, 'NT_充值付款失败')

    ############ 付款成功之后需要关闭一些东西
    for i in range(5):
        print("准备领东西....")
        try:
            touch(NT_accept)
        except:
            pass

        # 最后返回到主界面
    redHouseFlag = 0
    for i in range(5):
        print("返回到主界面")
        if redHouseFlag == 3:
            print("返回主界面3次失败，点击红房子")
            click([0.075, 0.943])
        if exists(NT_redHouse):
            touch(NT_redHouse)
        if exists(NT_levelReward):
            break
