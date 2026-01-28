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
from common.HugeWinImgs import *

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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--HugeWin_123 ", *args, **kwargs)


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


def isExistImg(exitImg: list):
    for breakImg in exitImg:
        if exists(breakImg):
            print(f"关闭页面完毕，存在{breakImg}")
            return True
    return False


def closeOpera(closeList: list, isclickList: list = None, MaxNum: int = 2, exitImg: list = None):
    '''

    :param closeList: 关闭的图片
    :param MaxNum: 大循环的次数
    :param isclickList: 点击屏幕的坐标，如果是空则不点击
    :param exitImg:退出条件
    :return:
    '''
    if isclickList is None:
        isclickList = []
    print("进行关闭.....")
    time.sleep(10)
    close_buy_list = closeList
    # 支付成功之后的操作
    quitFlag = 0
    while True:
        for close in close_buy_list:
            print(f"正在关闭关闭页面......{quitFlag + 1} / {MaxNum}")
            if isclickList:
                for clickPos in isclickList:
                    click(clickPos)
            try:
                touch(close)
                print(f"{quitFlag + 1} / {MaxNum} : 已关闭一个页面......{close}")
            except:
                pass
        quitFlag += 1
        print('quitFlag：', quitFlag, '------------------')
        if exitImg:
            if isExistImg(exitImg):
                break

        if quitFlag > MaxNum:
            break


def loginFacebook(c, ios):
    print("进行FaceBook登录.....")
    for i in range(30):
        if exists(sign_in_facebook):
            touch(sign_in_facebook)
            print("存在connet点击，点击完毕")

        if exists(sign_in_with_facebook):
            touch(sign_in_with_facebook)
            print("存在sign_in_with_facebook点击，点击完毕")
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
        if exists(HomePage_2):
            print("-----存在homeLoginPage----------")
            time.sleep(10)
        else:
            print("主页面不存在logo,已经进入了游戏内部....")
            break
    closeList = [collect_1, close_red, close_0, close_2]
    closeOpera(closeList)
    print("进入游戏内部成功...")


def buy_charge(c, password):
    print("进行付费购买功能测试...")
    for i in range(20):
        print("循环外面")
        time.sleep(1)
        if exists(SALE_button):
            print("存在SALE_button")
            touch(SALE_button)
            time.sleep(2)

        elif exists(Money_99_button):
            print("存在Money_99_button")
            touch(Money_99_button)
            time.sleep(10)
            break
        elif exists(Money_99_button_067):
            print("存在Money_99_button_067")
            touch(Money_99_button_067)
            time.sleep(10)
            break

        elif exists(BUY_button):
            print("存在BUY_button")
            touch(BUY_button)
            time.sleep(2)

        else:
            break

    is_click_money = True
    while 1:
        print("进行付费。。。。。。。。。。。。。。")
        try:
            if is_click_money:
                if exists(Money_99_button):  # 点击99.99购买按钮
                    try:
                        touch(Money_99_button)
                        is_click_money = False
                        time.sleep(10)
                    except:
                        pass

            time.sleep(2)

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
    # closeList = [collect_2, collect_3, keep_going, close_red, check, check_big, collect_4, close_1, close_red,close_2]
    closeList = [collect_2, collect_3, keep_going, close_red, check, check_big, collect_4,  close_red,close_2]
    closeOpera(closeList, MaxNum=3, exitImg=[SALE_button, BUY_button])


def enter_game():
    while True:
        if exists(download_enter_game):
            touch(download_enter_game)
            print("点击游戏下载按钮.........")
            time.sleep(10)

        if exists(ok_button):
            touch(ok_button)
            print("点击ok.....")
            time.sleep(10)

        if exists(close_red_1) or exists(spin_button):
            print("游戏关卡进入成功，进行spin阶段。。。。。")
            break


def theme_game(c, ios, n):
    print("游戏阶段")
    print("寻找游戏关卡，进入游戏.....")
    enter_game()
    spin_list = [close_red_1, spin_button, collect_5]
    for i in range(n * 5):
        print(f"进入spin,{n}")
        for j in spin_list:
            try:
                print("-----进行spin相关操作------")
                click([0.5, 0.65])
                touch(j)
            except:
                pass
    print("spin结束")


def back_to_home():
    while True:
        print("开始进行FaceBook登录，正在寻找FaceBook登录按钮.....")
        if exists(back_button):
            touch(back_button)
            print("点击了back按钮....")

        if exists(close_red_1):
            touch(close_red_1)
            print("点击了红色的关闭按钮....")

        if exists(big_red_jiantou):
            touch(big_red_jiantou)
            print("点击了大红色箭头")

        if exists(green_close):
            touch(green_close)
            print("点击了绿色关闭按钮")

        if exists(close_0):
            touch(close_0)
            print("点击了金色关闭按钮")

        if exists(f_connect):
            touch(f_connect)
            print("点击了左上角的facebook登录")

        if exists(sign_in_facebook):
            print("已找到SIGNIN按钮，进行FaceBook登录")
            break

        if exists(settings_button):
            touch(settings_button)
            print("点击了右上角的设置")

        if exists(swttings_text):
            touch(swttings_text)
            print("已找到settings按钮，进行FaceBook登录")
            break


def loginAccount(c, ios):
    back_to_home()
    for i in range(30):
        print("进行FaceBook登录.....")
        connectButton = False
        try:
            if exists(connect_facebook):
                touch(connect_facebook)
                print("点击了faceBookConnect确认按钮....")
                connectButton = True
                print("点击了connect按钮....")

            if exists(sign_in_facebook):
                print("已找到SIGNIN按钮，进行FaceBook登录。。。。。")
                connectButton = True
        except:
            pass
        if connectButton:
            print("按钮点击完毕，进行facebook登录的操作")
            loginFacebook(c, ios)
            break
    print("facebook登录成功，测试结束...")
