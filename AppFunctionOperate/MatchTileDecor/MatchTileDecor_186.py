# -*- coding: utf-8 -*-
"""
@Time : 2024/7/15 17:40
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : MatchTileDecor_186.py
"""
__author__ = "梦无矶小仔"

import sys
import threading
import time
import traceback
from common.screenshot import iosScreenshot

sys.dont_write_bytecode = True
import logging
from common.MatchTileDecorImgs import *
from ocr_detection.target_detection import *

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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--MatchTileDecor_0186 ", *args, **kwargs)


from airtest.core.settings import Settings as ST

ST.FIND_TIMEOUT = 1
ST.FIND_TIMEOUT_TMP = 0.5
ST.SAVE_IMAGE = False
is_login_facebook = False
ocrScan = OCRSingleton()


################# 游戏内操作

# 权限校验
def permission_click(c):
    print("进行授权")
    permissionTimes = 0
    for i in range(10):
        try:
            c(type="Button", name="无线局域网与蜂窝网络", timeout=3).click()
        except:
            time.sleep(1)

        print(f"----------{i}---------")
        if c(type="Button", name="允许").exists:
            c(type="Button", name="允许").click()
            time.sleep(1)

        if c(type="Button", name="继续").exists:
            c(type="Button", name="继续").click()
            time.sleep(1)

        if c(type="Button", name="下一步").exists:
            c(type="Button", name="下一步").click()
            time.sleep(1)

        if c(type="Button", name="开始测试").exists:
            c(type="Button", name="开始测试").click()
            time.sleep(1)

        ocrScan.ocr_click(img=None, action_text={"继续": 0})
        ocrScan.ocr_click(img=None, action_text={"开始": 0})

        if ocrScan.ocr_exist(img=None, action_text={"第1关": 0}):
            print("已经成功进入第一关！")
            break


def playLevel1():
    for i in range(10):
        try:
            touch(bingkuai)
        except:
            pass
        try:
            touch(yingtao)
        except:
            pass
        if ocrScan.ocr_exist(img=None, action_text={"继续": 0}):
            ocrScan.ocr_click(img=None, action_text={"继续": 0})
            print("第一关结束")
            break


def playLevel2():
    # 进行第二关
    guangka = 1
    openFlag = 1
    for i in range(20):
        try:
            for i in range(3):
                if exists(ningmeng):
                    touch(ningmeng)
            for i in range(3):
                if exists(yezi):
                    touch(yezi)
            for i in range(3):
                if exists(qiezi):
                    touch(qiezi)
            for i in range(3):
                if exists(bingkuai):
                    touch(bingkuai)
            for i in range(3):
                if exists(yingtao):
                    touch(yingtao)
            for i in range(3):
                if exists(yinghua):
                    touch(yinghua)
        except:
            pass
        if ocrScan.ocr_exist(img=None, action_text={"继续": 0}):
            time.sleep(1)
            ocrScan.ocr_click(img=None, action_text={"继续": 0})
            guangka += 1
            print(f"第{guangka}关结束")
            continue
        if ocrScan.ocr_exist(img=None, action_text={"选择您的礼物": 0}):
            time.sleep(1)
            if openFlag:
                ocrScan.ocr_click(img=None, action_text={"打开": 1})
                openFlag = 0
                time.sleep(2)
            ocrScan.ocr_click(img=None, action_text={"点击继续": 0})
            break

    for i in range(20):
        print("关闭评价弹框....")
        if ocrScan.ocr_exist(img=None, action_text={"HOME": 0}):
            time.sleep(3)
            ocrScan.ocr_click(img=None, action_text={"HOME": 0})
            time.sleep(3)


        if exists(redBack):
            try:
                touch(redBack)
            except:
                pass

        time.sleep(2)
        if ocrScan.ocr_exist(img=None, action_text={"评价": 0}):
            try:
                print("123点击白色关闭按钮")
                touch(whiteClose)
            except:
                pass

        try:
            touch(xiangzi)
        except:
            pass

        if ocrScan.ocr_exist(img=None, action_text={"9.99": 0}):
            break


def buy_charge(c, password):
    print("进行付费购买功能测试...")
    time.sleep(5)
    for i in range(20):

        try:
            print("尝试点击箱子....进入付费购买功能测试...")
            touch(xiangzi)
        except:
            pass

        if ocrScan.ocr_exist(img=None, action_text={"9.99": 0}):
            time.sleep(1)
            ocrScan.ocr_click(img=None, action_text={"9.99": 0})
            print("点击9.99购买")
            break

    while 1:
        try:
            ocrScan.ocr_click(img=None, action_text={"9.99": 0})
            if c.is_ready():
                print("进行付款")
                if c.is_ready():
                    print("输入密码")
                    if c.xpath('//*[@label=""]').exists:
                        c.xpath('//*[@label=""]').set_text(password)
                        c.close()
                        sleep(3)

                if c.xpath('//*[@label="购买"]').exists:
                    c.xpath('//*[@label="购买"]').click_exists(5)
                    c.close()
                    sleep(20)
                elif c.xpath('//*[@label="消费"]').exists:
                    c.xpath('//*[@label="消费"]').click_exists(5)
                    c.close()
                    sleep(5)

                elif c.xpath('//*[@label="购买"]').exists:
                    c.xpath('//*[@label="购买"]').click_exists(5)
                    c.close()
                    sleep(5)

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
                    if ocrScan.ocr_exist(img=None, action_text={"好": 0}):
                        time.sleep(2)
                        ocrScan.ocr_click(img=None, action_text={"好": 0})
                        break

            if ocrScan.ocr_exist(img=None, action_text={"购买错误": 0}):
                for i in range(5):
                    time.sleep(3)
                    ocrScan.ocr_click(img=None, action_text={"确认": 0})
                    print("购买错误！！！")
                    break

        except:
            traceback.print_exc()


def loginAppleID(c, ios, password):
    for i in range(30):
        print("进行Apple ID登录.....")
        if exists(settingImg):
            touch(settingImg)
            print("点击了settings按钮....")

        ocrScan.ocr_click(img=None, action_text={"Apple": 0})

        ocrScan.ocr_click(img=None, action_text={"使用密码继续": 0})

        if ocrScan.ocr_exist(img=None, action_text={"忘记密码": 0}):
            text(password)
            ocrScan.ocr_click(img=None, action_text={"继续": 0})
            print("Apple ID登录成功！")

        if ocrScan.ocr_exist(img=None, action_text={"点击领取": 0}):
            break


def homePageOperate():
    print("到了主界面的操作.....")
    print("进行各个页面的切换......")

    home_click_list = [
        [0.1, 0.92], [0.5, 0.92], [0.7, 0.92], [0.9, 0.92], [0.3, 0.92], [0.5, 0.5], [0.4, 0.9], [0.75, 0.9], [0.5, 0.5]
    ]
    for i in range(3):
        print("首页页面点击中,,,,,,,,,")
        for homePosition in home_click_list:
            click(homePosition)

    print("所有功能测试结束！")