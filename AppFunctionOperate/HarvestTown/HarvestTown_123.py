# -*- coding: utf-8 -*-
'''
@Time : 2022/10/8 13:56
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : DoubleWin_046.py
'''
__author__ = "梦无矶小仔"

import datetime
import sys
import threading
import time
import traceback
import random

from common.screenshot import iosScreenshot
from airtest.core.api import *

sys.dont_write_bytecode = True
import logging
from common.HarvestTownImgs import *

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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--奶牛小镇_123 ", *args, **kwargs)


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
    while True:
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
    print(f"facebook登录成功，进行协议勾选....")

def randomMailbox():
    '''
    生成随机邮箱
    '''
    randint_num = str(random.randint(1,666))
    now_time = str(int(time.time()))
    random_mailbox = str(randint_num+now_time[5:]) + "@gmail.com"
    print(f"注册的邮箱账号为：{random_mailbox}")
    return random_mailbox

def loginEmailAccount(ios_poco):
    while True:
        try:
            print("Account注册并登录ing......")
            ## 切换到注册
            ios_poco(name="用户注册").click()
            time.sleep(2)
            ## 点击注册邮箱
            ios_poco(name="TextField").click()
            time.sleep(2)
            text(randomMailbox()) # 输入随机邮箱进行注册
            ## 输入密码
            ios_poco(name="SecureTextField").click()
            time.sleep(2)
            text("123456")
            time.sleep(2)
            click([0.2, 0.2])
            # 点击同意Account用户服务协议
            aa = ios_poco(type="Button", name="unselect@3x")
            if aa.exists():
                aa.click()
            # 点击注册账号
            ios_poco(type="Button", name="注册").click()
            break
        except:
            traceback.print_exc()

    print(f"注册Account并登录成功，进行协议勾选....")

def loginEmailAccountByImg(ios_poco):
    while True:
        try:
            print("Account注册并登录ing......")
            agree_flag = False
            ## 点击注册邮箱
            if exists(email_field):
                touch(email_field)
                print("点击邮箱，输入  邮箱账号。。。。。")
                time.sleep(2)
                text(randomMailbox())  # 输入随机邮箱进行注册
            if exists(pwd_field):
                touch(pwd_field)
                print("点击密码，输入  邮箱密码。。。。。")
                time.sleep(1)
                text("123456")
                time.sleep(2)
                click([0.2, 0.2])
            if exists(agree_button):
                touch(agree_button)
                print("点击账号注册的   同意协议  置为True")
                time.sleep(1)
                agree_flag = True

            if not agree_flag and exists(agree_button_100):
                touch(agree_button_100)
                print("点击设备100 账号注册的   同意协议  置为True")
                time.sleep(1)
                agree_flag = True

            if agree_flag and exists(register_button):
                touch(register_button)
                print("点击注册按钮....................")
                time.sleep(2)
                break
        except:
            traceback.print_exc()

    print(f"注册Account并登录成功，进行协议勾选....")

def OpenGame(c, ios):
    while True:
        print("----------进入游戏---------")
        # 判断是否在homepage页面，如果在则等待
        if exists(game_icon):
            print("-----存在homeLoginPage----------")
            time.sleep(5)
            break


def buy_charge(c, password):
    print("进行付费购买功能测试...")
    while True:
        print("购买循环外面")
        time.sleep(1)
        shop_icon_final = exists(shop_icon)
        if not shop_icon_final:
            shop_icon_final = exists(shop_icon_100)
        print(f"获取到了 shop商店的坐标 {shop_icon_final}")

        try:
            click(shop_icon_final)
            print("点击了  商店shop  按钮")

        except:
            pass

        if exists(diamond_img):
            print("存在 钻石图片 代表商店进入成功")
            break

    while True:
        print("进行钻石购买.....")
        try:
            if exists(confirm_button_common):
                touch(confirm_button_common)
                print("点击了 确认购买")
                time.sleep(20)
                break

            elif exists(diamond_img):
                touch(diamond_img)
                print("点击了 钻石图片")

        except Exception as e:
            traceback.print_exc()

    while 1:
        print("进行付费。。。。。。。。。。。。。。")
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
                    time.sleep(5)
                    break

    click([0.5,0.5])
    time.sleep(5)

def enter_game_operate(pos:list):
    """
    param:pos 勾选服务协议的坐标点
    """
    while True:
        print("账号已经登录，当前正在勾选协议进入游戏。。。")
        if exists(confirm_button_common):
            # 点击确认按钮
            try:
                touch(confirm_button_common)
                print("点击确认登录按钮.....")
            except:
                pass

        if exists(enter_game):
            # 先点击坐标
            click(pos)
            touch(enter_game)
            print("勾选了协议，点击了进入游戏.....")

        if exists(confirm_button_common):
            # 点击确认按钮
            try:
                touch(confirm_button_common)
                print("点击确认登录按钮.....")
            except:
                pass


        if not exists(game_icon) and not exists(enter_game):
            print("游戏进入成功，进行新手引导。。。。。")
            time.sleep(15)
            break


def theme_game(c, ios, n):
    while True:
        click([0.5,0.5])

        if exists(confirm_button_common):
            try:
                touch(confirm_button_common)
                print("点击了  确认  按钮....")
            except:pass

        elif exists(skip_guide_common):
            touch(skip_guide_common)
            print("点击了 跳过引导  顶部按钮...")
            continue

        elif exists(menu_common):
            touch(menu_common)
            print("点击了  菜单    公共图图标")
            time.sleep(5)
            try:
                touch(save_data)
                print("点击了 保存数据   按钮")
            except:
                for i in range(3):
                    click([0.5,0.5])
                    time.sleep(1)


        elif exists(menu_067):
            touch(menu_067)
            print("点击了  菜单    067 图图标")
            time.sleep(5)
            try:
                touch(save_data)
                print("点击了 保存数据   按钮")
            except:
                for i in range(3):
                    click([0.5, 0.5])
                    time.sleep(1)



        elif exists(skip_button):
            print("点击了  跳过  按钮....")
            touch(skip_button)
            continue

        elif exists(speed_up):
            touch(speed_up)
            print("点击   加速   按钮.....")
            continue

        elif exists(familiar_text):
            touch(familiar_text)
            print("点击了  我很熟悉  文本对话....")
            # continue

        elif exists(shop_icon) or exists(shop_icon_100):
            print("存在shop商铺,可以直接进行购买操作....")
            break

def registerAccount(c, ios_poco,pos):
    while True:
        print("进行Account账号注册登录.....")
        connectButton = True

        if exists(registerAccountButton):
            touch(registerAccountButton)
            connectButton = False
            print("点击了 Account账户登录  按钮....")

        if connectButton and exists(enter_game):
            touch(enter_game)
            print("点击了enter_game按钮....")

        if not connectButton:
            print("Account账户按钮点击完毕，进行注册登录的操作")
            loginEmailAccount(ios_poco)
            break

    enter_game_operate(pos)

    print("Account账户注册并登录成功，测试结束...")


def registerAccountByImg(c, ios_poco,pos):
    while True:
        print("进行Account账号注册登录.....")
        connectButton = True

        if exists(registerAccountButton):
            touch(registerAccountButton)
            connectButton = False
            print("点击了 Account账户登录  按钮....")

        if connectButton and exists(enter_game):
            touch(enter_game)
            print("点击了enter_game按钮....")

        if not connectButton:
            print("Account账户按钮点击完毕，进行注册登录的操作")
            loginEmailAccountByImg(ios_poco)
            break

    enter_game_operate(pos)

    print("Account账户注册并登录成功，测试结束...")

def loginAccount(c, ios,pos):
    while True:
        print("进行FaceBook登录.....")
        connectButton = True

        if exists(facebook_icon):
            touch(facebook_icon)
            connectButton = False
            print("点击了facebook_icon按钮....")

        if connectButton and exists(enter_game):
            touch(enter_game)
            print("点击了enter_game按钮....")

        if not connectButton:
            print("按钮点击完毕，进行facebook登录的操作")
            loginFacebook(c, ios)
            break
    enter_game_operate(pos)

    print("facebook登录成功，测试结束...")
