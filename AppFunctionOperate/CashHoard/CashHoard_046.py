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
from common.CashHoardImgs import *

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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--CashHoard_046 ", *args, **kwargs)


################# 游戏内操作
from airtest.core.settings import Settings as ST

ST.FIND_TIMEOUT = 2
ST.FIND_TIMEOUT_TMP = 1
ST.SAVE_IMAGE = False
is_login_facebook = False


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


def closeOpera(closeList: list, MaxNum: int = 2, isclick=False):
    print("进行关闭.....")
    time.sleep(10)
    close_buy_list = closeList
    # 支付成功之后的操作
    quitFlag = 0
    while True:
        for close in close_buy_list:
            print(f"正在关闭关闭页面......{quitFlag + 1} / {MaxNum}")
            if isclick:
                click([0.5, 0.5])
            try:
                touch(close)
                print(f"{quitFlag + 1} / {MaxNum} : 已关闭一个页面......{close}")
            except:
                pass
        quitFlag += 1
        print('quitFlag：', quitFlag, '------------------')
        if quitFlag > MaxNum:
            break


def loginFacebook(c, ios):
    print("进行FaceBook登录.....")
    for i in range(30):
        if exists(faceBookConnect):
            touch(faceBookConnect)
            print("存在connet点击，点击完毕")
            break
        else:
            time.sleep(1)

    for i in range(10):
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
            break
    is_login_facebook = True
    print(f"facebook登录成功,is_login_facebook:{is_login_facebook}")


def enterGame(c, ios):
    while True:
        print("----------进入游戏---------")
        # 判断是否在homepage页面，如果在则等待
        if exists(homeLoginPage):
            print("-----存在homeLoginPage----------")
            time.sleep(5)
            if exists(faceBookConnect):
                print("存在facebook登录,进行facebook登录")
                loginFacebook(c, ios)
        else:
            print("主页面不存在logo,已经进入了游戏内部....")
            break
    closeList = [close_7, close_1, close_2, close_3, close_4, close_5, collectButton, close_6]
    closeOpera(closeList, MaxNum=5)
    print("进入游戏内部成功...")


def buy_charge(c, password):
    print("进行付费购买功能测试...")
    for i in range(20):
        time.sleep(1)
        if exists(BuyCoins):
            touch(BuyCoins)
        elif exists(BuyButton):
            touch(BuyButton)
        else:
            break

    is_click_money = True
    while 1:
        print("进行付费。。。。。。。。。。。。。。")
        try:
            if is_click_money:
                if exists(Money99):  # 点击99.99购买按钮
                    try:
                        touch(Money99)
                        is_click_money = False
                        time.sleep(10)
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
                    sleep(8)
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
    closeList = [OkButton, FillItToPlay, PressToPlay, SpinClose, collectButton, buy_close_1, buy_close_2, buy_close_3, buy_close_4]
    closeOpera(closeList, MaxNum=5)


def enter_game():
    while True:
        if exists(GameLevelChose):
            touch(GameLevelChose)
            break
        else:
            print("滑动查找...")
            swipe([0.5, 0.5], [0.3, 0.5])
            time.sleep(3)

    while True:
        print("查找游戏成功，进入正常模式...")
        if exists(RegularModel):
            touch(RegularModel)
            time.sleep(1)
            try:
                touch(play6000Yellow)
                break
            except:
                pass
            try:
                touch(play6000Blue)
                break
            except:
                pass
    print("游戏关卡进入成功，进行spin阶段。。。。。")


def theme_game(c, ios, n):
    print("游戏阶段")
    print("寻找游戏关卡，进入游戏.....")
    enter_game()
    spin_list = [Spin, spinClose_1, Spin, spinClose_2_no, Spin, spinClose_2_Yes, Spin, spinClose_3
        , Spin, spinClose_4_letKittyChoose, Spin, spinClose_5_LetsGo, Spin, spinClose_6, Spin, spinClose_7, Spin, login_close_5]
    for i in range(n * 5):
        print(f"进入spin,{n}")
        for j in spin_list:
            try:
                print("-----进行spin相关操作------")
                touch(j)
            except:
                pass
    print("spin结束")


def loginAccount(c, ios):
    if is_login_facebook:
        print("已经登录过了facebook哦.....")
        return 1
    connectButton = False
    for i in range(30):
        print("进行FaceBook登录.....")
        if exists(settingButton):
            touch(settingButton)
            print("点击了settings按钮....")
        try:
            if exists(settingsImg):
                touch(settingsImg)
                print("点击了settings_text....")
            if exists(faceBookButton):
                touch(faceBookButton)
                print("点击了faceBookButton....")
            if exists(faceBookConnect):
                touch(faceBookConnect)
                print("点击了faceBookConnect确认按钮....")
                connectButton = True
                print("点击了connect按钮....")
        except:
            pass
        if connectButton:
            print("按钮点击完毕，进行facebook登录的操作")
            loginFacebook(c, ios)
            break
    print("facebook登录成功，等待进入主界面,进行页面关闭操作......")
    time.sleep(20)
    closeList = [close_7, login_close_4, login_close_3, login_close_4, login_close_5, login_close_6, login_close_1, login_close_2, ]
    closeOpera(closeList, MaxNum=5)
