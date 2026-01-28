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
from common.MatchScapesImgs import *

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
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "--MatchScapes_067 ", *args, **kwargs)


from airtest.core.settings import Settings as ST

ST.FIND_TIMEOUT = 2
ST.FIND_TIMEOUT_TMP = 1
ST.SAVE_IMAGE = False
is_login_facebook = False


################# 游戏内操作
def playLevel1():
    # 首先先判断左上角的设置按钮是否存在，如果存在，则进行第一关的游戏操作
    for once in range(3):
        # if exists(settingButton):
        #     print("进行第一关的点击操作")
        x1 = [0.31, 0.5, 0.68]
        y1 = [0.38, 0.27]
        z = []
        for x in x1:
            for y in y1:
                z.append([x, y])
        z.append([0.5, 0.75])  # 继续按钮
        for i in range(5):
            for j in z:
                click(j)
        time.sleep(5)
    #     break
    # else:
    #     time.sleep(10)

def buy_charge(c, password):
    print("进行付费购买功能测试...")
    time.sleep(5)
    money_img_flag = False
    for i in range(20):
        if exists(moreButton):
            money_img_flag = True
            print("点击更多付费选项...")
            touch(moreButton)
        if exists(moneyButton):
            money_img_flag = True
            print("点击付费按钮...")
            touch(moneyButton)
            break
        if not money_img_flag:
            print("点击右上角的金币按钮")
            click([0.83, 0.045])  # 点击右上角的金币按钮

    while 1:
        try:
            if exists(moneyButton):  # 点击59.99购买按钮
                try:
                    touch(moneyButton)
                except:
                    pass
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
            if c.is_ready():
                print("输入密码")
                if c.xpath('//*[@label=""]').exists:
                    c.xpath('//*[@label=""]').set_text(password)
                    c.close()
                    sleep(3)
                if c.xpath('//*[@label="购买"]').exists:
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
                    if alert[-1] == '好':
                        print("点击接受弹窗按钮")
                        c.alert.accept()
                        c.close()
                        break
                    # if len(alert) > 0:
                    #     print("点击接受弹窗按钮")
                    #     # c.alert_click(alert)
                    #     c.alert.accept()
                    #     c.close()
        except:
            traceback.print_exc()

    ### 支付完成之后返回
    for i in range(10):
        try:
            touch(backButton)
            print("支付完成,退出支付界面")
            break
        except:
            pass

def theme_game(c, ios, n):
    print("游戏阶段")
    if exists(settingButton):
        print("存在设置按钮，确认可以开始进行关卡游玩...")

    ### 先完成第2关
    print("进行第二关关卡的游玩.....")
    click_list = [[0.31, 0.36], [0.5, 0.36], [0.68, 0.36],
                  [0.31, 0.31], [0.5, 0.31], [0.68, 0.31],
                  [0.31, 0.27], [0.5, 0.27], [0.68, 0.27]]
    for k in range(5):
        for j in click_list:
            click(j)
        if exists(continueButton):
            break
    print("进行第二关关卡的游玩结束.....")

    print("进入多线程阶段，开始进行关卡点击....")
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
    #### 这个线程用来坐标
    click_list2 = [[0.5, 0.75], [0.5, 0.85], [0.4, 0.85], [0.4, 0.85], [0.5, 0.85]]
    while 1:
        if avent.is_set():
            print("进行关卡点击")
            for click1 in click_list2:
                click(click1)
        else:
            break


def theme_game_click_2():
    #### 这个线程用来点击图片
    click_list2 = [buy450, confirm, buy450, useBackGround, buy450]
    while 1:
        if avent.is_set():
            for click1 in click_list2:
                try:
                    print("点击购买、好的、使用")
                    touch(click1)
                except:
                    pass
        else:
            break

def time_stop(n):
    print("启动时间监控")
    sleep(60 * n)
    print("时间到....灭霸打一下响指....")
    avent.clear()
    bvent.clear()


def loginAccount(c, ios):
    for i in range(30):
        print("进行FaceBook登录.....")
        click([0.053, 0.43])
        if exists(settingButton):
            touch(settingButton)
            print("点击了settings按钮....")
        if exists(save_and_read):
            touch(save_and_read)
            print("点击了保存与读取按钮....")
        if exists(facebook_sign_in):
            touch(facebook_sign_in)
            print("点击了FaceBook登录....")
            break

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
        if exists(fb_continue):
            touch(fb_continue)
            sleep(8)
        if exists(online_save):
            print("存在保存按钮，即登录成功，进行下一步数据保存与读取")
            break

    save_success_flag = False
    while True:
        try:
            print("点击保存到线上.....")
            touch(online_save)
            save_success_flag = True
        except:
            pass
        try:
            if save_success_flag:
                print("点击确认保存1...")
                touch(single_save)
                time.sleep(8)
                print("点击确认保存2...")
                touch(single_save)
                time.sleep(8)
                print("点击好的1...")
                touch(confirm)
                print("资源保存成功,进行读取.....")
                break
        except:
            pass

    while True:
        try:
            touch(single_save)
        except:
            pass
        try:
            print("点击好的2")
            touch(confirm)
        except:
            pass
        try:
            print("再次点击保存与读取......")
            touch(save_and_read)
            time.sleep(2)
        except:
            pass

        try:
            print("读取线上数据到本地.....")
            touch(read_to_local)
            time.sleep(8)
            touch(single_read)
            time.sleep(2)
            touch(single_read)
            print("数据读取成功......")
            break
        except:
            pass


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
