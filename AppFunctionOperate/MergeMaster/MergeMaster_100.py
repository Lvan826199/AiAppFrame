# -*- coding: utf-8 -*-
"""
@Time : 2024/10/31 18:06
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : MergeMaster_049.py
"""
__author__ = "梦无矶小仔"

import sys
import threading
import time
import traceback
from common.screenshot import iosScreenshot

sys.dont_write_bytecode = True
import logging
from common.MergeMasterImgs import *
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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--MergeMaster_0100 ", *args, **kwargs)


from airtest.core.settings import Settings as ST

ST.FIND_TIMEOUT = 1
ST.FIND_TIMEOUT_TMP = 0.5
ST.SAVE_IMAGE = False
is_login_facebook = False

################# 游戏内操作
avent = threading.Event()
bvent = threading.Event()

ocrScan = OCRSingleton()

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

        # ocr_click(img=None, action_text={"继续": 0})
        ocrScan.ocr_click(img=None, action_text={"开始": 0})
        time.sleep(2)

        if ocrScan.ocr_exist(img=None, action_text={"点击继续": 0}):
            print("进入了游戏主页面！")
            ocrScan.ocr_click(img=None, action_text={"点击继续": 0})
            break


def player_in():
    print("进入游戏的阶段,线程起")
    avent.set()
    bvent.set()
    from threading import Thread
    t1 = Thread(target=playLevel1)  # 弹窗点击
    t2 = Thread(target=playLevel2)
    t3 = Thread(target=time_stop, args=(4,))
    t1.setDaemon(True)
    t1.start()
    t2.setDaemon(True)
    t2.start()
    t3.setDaemon(True)
    t3.start()
    t1.join()
    t2.join()
    t3.join()


def time_stop(n):
    print("启动时间监控")
    sleep(60 * n)
    print("时间到....灭霸打一下响指....")
    avent.clear()
    bvent.clear()


#


def playLevel1():
    while 1:
        ocrScan.ocr_click(img=None, action_text={"点击继续": 0})
        if ocrScan.ocr_exist(img=None, action_text={"退出": 0}):
            ocrScan.ocr_click(img=None, action_text={"退出": 0})
            break


def playLevel2():
    # boss战
    while 1:
        if bvent.is_set():
            ocrScan.ocr_click(img=None, action_text={"点击": 0})
            time.sleep(0.5)
            ocrScan.ocr_click(img=None, action_text={"取消": 0})
            # if ocr_exist(img=None, action_text={"猫猫机抽奖次数不足": 0}):
            #     for k in range(3):
            #         if ocr_exist(img=None, action_text={"点击": 0}):
            #             ocr_click(img=None, action_text={"点击": 0})
            #             break
        else:
            break


def buy_charge(c, password):
    pass
#     print("进行付费购买功能测试...")
#     time.sleep(5)
#     while True:
#         if exists(goPay):
#             touch(goPay)
#
#         if ocrScan.ocr_exist(img=None, action_text={"9.99": 0}):
#             print("成功点击了进入支付按钮...准备进行支付....")
#             break
#
#     if ocrScan.ocr_exist(img=None, action_text={"9.99": 0}):
#         time.sleep(1)
#         ocrScan.ocr_click(img=None, action_text={"9.99": 0})
#         print("点击9.99购买")
#
#     while 1:
#         try:
#             # ocr_click(img=None, action_text={"9.99": 0})
#             if c.is_ready():
#                 print("进行付款")
#                 if c.is_ready():
#                     print("输入密码")
#                     if c.xpath('//*[@label=""]').exists:
#                         c.xpath('//*[@label=""]').set_text(password)
#                         c.close()
#                         sleep(3)
#
#                 if c.xpath('//*[@label="购买"]').exists:
#                     c.xpath('//*[@label="购买"]').click_exists(5)
#                     c.close()
#                     sleep(20)
#                 elif c.xpath('//*[@label="消费"]').exists:
#                     c.xpath('//*[@label="消费"]').click_exists(5)
#                     c.close()
#                     sleep(5)
#             if c.is_ready():
#                 print("输入密码")
#                 if c.xpath('//*[@label=""]').exists:
#                     c.xpath('//*[@label=""]').set_text(password)
#                     c.close()
#                     sleep(3)
#                 if c.xpath('//*[@label="购买"]').exists:
#                     c.xpath('//*[@label="购买"]').click_exists(5)
#                     c.close()
#                     sleep(5)
#
#             if c.is_ready():
#                 print("登录付费")
#                 if c.xpath('//*[@label="登录"]').exists:
#                     c.xpath('//*[@label="登录"]').click_exists(5)
#                     c.close()
#                     sleep(2)
#             if c.is_ready():
#                 print("输入密码------")
#                 try:
#                     text(password)
#                     sleep(2)
#                     ocrScan.ocr_click(img=None, action_text={"登录": 0})
#                 except:pass
#                 c.close()
#
#             try:
#                 print("屏幕会话", c.orientation)
#             except:
#                 pass
#             c.close()
#
#             if c.is_ready():
#                 print("购买完成点击弹窗确认")
#                 if c.alert.exists:
#                     print(c.alert.text)
#                     alert = c.alert.buttons()
#                     print("按钮弹框：", alert)
#                     if ocrScan.ocr_exist(img=None, action_text={"好": 0}):
#                         time.sleep(2)
#                         ocrScan.ocr_click(img=None, action_text={"好": 0})
#                         break
#         except:
#             traceback.print_exc()


def loginAppleID(c, ios, password):
    # for i in range(30):
    #     print("进行Apple ID登录.....")
    #     if exists(loginIcon):
    #         touch(loginIcon)
    #         print("点击了右上角的登录按钮....")
    #         break

    for i in range(30):
        ocrScan.ocr_click(img=None, action_text={"Apple登录": 0})

        ocrScan.ocr_click(img=None, action_text={"使用密码继续": 0})

        if ocrScan.ocr_exist(img=None, action_text={"忘记密码": 0}):
            text(password)
            time.sleep(2)
            ocrScan.ocr_click(img=None, action_text={"继续": 0})
            print("Apple ID登录成功！")
            time.sleep(2)
            ocrScan.ocr_click(img=None, action_text={"登录": 0})
            print("游戏登录成功！")
            break
