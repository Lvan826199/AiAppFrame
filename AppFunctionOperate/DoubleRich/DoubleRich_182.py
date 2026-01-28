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
from common.DoubleRichImgs import *

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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--DoubleRich_0182 ", *args, **kwargs)


################# 游戏内操作
from airtest.core.settings import Settings as ST

ST.FIND_TIMEOUT = 3
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
            if isclick:
                click([0.5, 0.5])
            try:
                touch(close)
                print("正在关闭关闭页面......")
            except:
                pass
        quitFlag += 1
        print('quitFlag：', quitFlag, '------------------')
        if quitFlag > MaxNum:
            break


def loginFacebook(c, ios):
    print("进行FaceBook登录.....")
    for i in range(30):
        if exists(facebookLogin):
            touch(facebookLogin)
            print("点击了facebook登录按钮....")
            break
        if exists(connect):
            touch(connect)
            print("存在connet点击，点击完毕")
            break
        else:
            time.sleep(5)

    for i in range(40):
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
        if exists(homePageLogo):
            print("-----存在homepageLog----------")
            time.sleep(5)
            if exists(facebookLogin):
                print("存在facebook登录,进行facebook登录")
                loginFacebook(c, ios)
        else:
            print("主页面不存在logo,已经进入了游戏内部....")
            break
    closeList = [GotIt, close_1, TAPTOCOLLECT, collect, close_2, close_3, close_4, close_buy_1, close_buy_2, close_buy_3, close_5]
    closeOpera(closeList, MaxNum=3)
    print("进入游戏内部成功...")


def buy_charge(c, password):
    print("进行付费购买功能测试...")
    for i in range(20):
        time.sleep(1)
        if exists(BuyButton):
            touch(BuyButton)
        else:
            break
    is_click_money = True
    while 1:
        try:
            if is_click_money:
                if exists(money99):  # 点击99.99购买按钮
                    try:
                        touch(money99)
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
    closeList = [close_buy_1, close_buy_2, collect,
                 Continue, close_buy_3, awesome, collect_1, close_push, close_great, open_all,
                 later, spin_close_1]
    closeOpera(closeList, isclick=True, MaxNum=3)


def theme_game(c, ios, n):
    print("游戏阶段")
    spin_list = [spinButton, spin_close_1]
    for i in range(n * 5):
        print("进入spin")
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
            if exists(settingClick):
                touch(settingClick)
                print("点击了settings_text....")
            if exists(logoutButton):
                touch(logoutButton)
                print("点击了logoutButton....")
            if exists(logooutConfirm):
                touch(logooutConfirm)
                print("点击了logooutConfirm确认按钮....")
            if exists(connect):
                connectButton = True
                print("点击了connect按钮....")
        except:
            pass
        if connectButton:
            print("按钮点击完毕，进行facebook登录的操作")
            loginFacebook(c, ios)
            break
