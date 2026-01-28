# -*- coding: utf-8 -*-
'''
@Time : 2022/10/8 14:22
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : TEST_DoubleWin_100.py
'''
__author__ = "梦无矶小仔"

import datetime
import sys
import threading
import time
import traceback

from tidevice import Device
from airtest.core.ios.ios import IOS, wda

sys.dont_write_bytecode = True
import unittest
import logging
from common.imageElePath import *
from common.IOSAppOperate import SH_123
# from tools.get_devices_log import ios_log
from common.ParameterizedTestCase import ParameterizedTestCase
from AppFunctionOperate.DoubleWin.DoubleWin_123 import *

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
_print = print


# ### 设置airtest的日志输出等级,调试时可以注释或者调为INFO
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)


controlparams = {'control': 1}  # 用作控制器


class Test_GrandCash_123(ParameterizedTestCase):
    u'''测试用例Demo的集合'''

    @classmethod
    def setUpClass(self):
        u''' 这里放需要在整个测试类之前执行的部分'''
        print("setUpClass，在整个测试类之前执行")

    @classmethod
    def tearDownClass(self):
        u'''这里放需要在整个测试类之后执行的部分'''
        controlparams['control'] = 1

    def setUp(self):
        u'''这里放需要在每条用例前执行的部分'''
        # 前段部分用于初始化连接设备，这个部分的作用就是避免设备多次重新连接，只会连接一次
        if controlparams['control'] == 1:
            self.ios = IOS("http+usbmux://" + self.device_id)
            self.c = wda.Client("http+usbmux://{udid}".format(udid=self.device_id))
            controlparams['ios'] = self.ios
            controlparams['c'] = self.c
            controlparams['control'] = 2
        # 每次执行用例前，需要从控制参数里面进行取出（但不会进行重新连接）
        self.ios = controlparams['ios']
        self.c = controlparams['c']

    def tearDown(self):
        u'''这里放需要在每条用例后执行的部分'''
        # self.c.close() #防止在线程中使用时端口阻塞

    ###################################  用例  ####################################
    # @Timeout.timeout(30)
    @unittest.skip
    def test_01_of_loginAppStore(self):
        u'''登录appstore'''
        print("---------开始进行第一个测试用例----------")
        # 每个函数里分别实例poco，否则容易出现pocoserver无限重启的情况
        # ###卸载
        Device(self.device_id).app_uninstall("com.huge.slots.casino.vegas.ios.avidly")  # 填入自己公司app的ios包名
        ###安装
        if self.c.locked():
            self.c.unlock()
        if self.ios.alert_exists():
            alert = self.ios.alert_buttons()
            print("检测：", alert)
        if self.c.alert.exists:
            buttons = self.c.alert.buttons()
            self.c.alert.click(buttons)
            print("弹框关闭")
        self.c.close()
        print("````````````````````````````````")
        ###########################
        # appstore 账号登录
        SH_123().loginAppStore(self.c, "jinlimei86@gmail.com", "Avidly1234")  # 填入用于app store登录的apple id

    @unittest.skip
    def test_02_of_checkAcount(self):
        '''检查AppleID'''
        # 沙盒账号登录
        print("-------------------进行第二个测试用例---------------------")
        SH_123().check_acount_ios14(self.c, "jinlimei86@gmail.com", "Avidly1234")  # 填入用于app充值的沙盒账号
        ###################################

    @unittest.skip
    def test_03_of_DownloadApp(self):
        u'''进入TestFlight进行下载App'''
        print("-------------------进行第三个测试用例---------------------")
        ##使用testflight下载对应的app,填入的是在testFlight显示的app全程
        SH_123().game_download(self.c, name="Double Win Slots Casino Game")
        print("DoubleWin 下载完毕！")
        print("测试开始")

    # @unittest.skip
    def test_04_of_loginApp(self):
        u'''检查登录功能'''
        packageName = "com.huge.slots.casino.vegas.ios.avidly"
        ##启动
        self.c.app_start(packageName)
        sleep(10)
        ###判断app是否在运行
        app = self.ios.app_state(packageName)["value"]

        ###########  进入游戏之后，会有权限弹窗，对权限弹窗点击确认，这里写的是三次
        if app == 4:
            for i in range(3):
                if self.ios.alert_exists():
                    self.ios.alert_accept()
                    time.sleep(0.5)
        login(self.device_id, self.c, self.ios)
        time.sleep(10)
        for i in range(3):
            if self.ios.alert_exists():
                self.ios.alert_accept()
                time.sleep(0.5)
        print("DoubleWin登录成功！")

    # @unittest.skip
    def test_05_of_enterApp(self):
        u'''进入游戏'''
        player_in()

    # @unittest.skip
    def test_06_of_pay(self):
        u'''充值功能检查'''
        from settings.account_pwd_config import get_pwd
        pwd = get_pwd("DoubleWin")
        print(f"输入的密码：{pwd}")
        buy_charge(self.c, password=pwd)

    # @unittest.skip
    def test_07_of_basicFunc(self):
        u'''基础功能流程操作'''
        theme_game(self.c, self.ios, n=3)
        stop_app("com.huge.slots.casino.vegas.ios.avidly")
