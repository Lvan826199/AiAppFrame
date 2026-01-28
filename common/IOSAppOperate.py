# -*- coding: utf-8 -*-
'''
@Time : 2022/9/19 11:48
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : IOSAppOperate.py
'''
__author__ = "梦无矶小仔"

import sys

sys.dont_write_bytecode = True
from airtest.core.api import *

'''
ios设备的所有登录等操作
'''


########################### 046  账号登录，App下载等步骤
class SH_046():
    #########  账号登录，App下载等步骤
    def check_acount(self, c, acount=None, pwd=None):
        ###ios版本 14以下
        c.close()
        c.app_stop("com.apple.Preferences")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.Preferences")
                App_Store = c(type="Cell", name="iTunes Store 与 App Store", label="iTunes Store 与 App Store",
                              enabled="true")
                e = c(enabled="true", visible="true")
                App_Store_sign = 0
                while 1:
                    print("寻找iTunes Store 与 App Store.....")
                    swipe([0.5, 0.6], [0.5, 0.45])
                    if App_Store.visible:
                        print("iTunes Store 与 App Store寻找到了1111")
                        App_Store.click()
                        break
            c(type="Cell", enabled="true", visible="true").wait(timeout=280)
            if c(type="Cell", enabled="true", visible="true").exists:
                aount = c(type="Cell", enabled="true", visible="true").label
                if aount == "登录":
                    c(type="Cell", enabled="true", visible="true").click()
                    c(value="Apple ID", label="").set_text(acount)  ##账号
                    c(value="密码", label="").set_text(pwd)  ##密码
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    sleep(15)
                else:
                    if len(aount.split('ID：')) > 0:
                        test_aount = aount.split('ID：')[1]
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            c(type="Cell", enabled="true", visible="true").click()  ##点击账号处，弹出退出页面
                            c(type="Button", name="退出登录", label="退出登录", enabled="true",
                              visible="true").click()  ##点击退出登录按钮
                            c(type="Cell", enabled="true", visible="true").click()
                            c(value="Apple ID", label="").set_text(acount)  ##账号
                            c(value="密码", label="").set_text(pwd)  ##密码
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            sleep(15)
            ### 如果没有双重认证的,则需要进行确认
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    print("认证完毕或不需要认证，退出！")
                    break
            c.app_stop("com.apple.Preferences")
            c.close()
        except Exception as e:
            print(e)
        sleep(15)

    def game_download(self, c, name):
        c.app_stop("com.apple.TestFlight")
        c.app_start("com.apple.TestFlight")
        sleep(3)
        if c(type='Button', name='Continue Button').exists:
            c(type='Button', name='Continue Button').click()

        game = c(type="Cell", name=name)
        n = 0
        while 1:
            n += 1
            if n <= 6:
                if game.exists:
                    print("已找到")
                    break
                else:
                    swipe([0.5, 0.78], [0.5, 0.33])
                    print("向下滑")
            if 5 < n < 13:
                if game.exists:
                    break
                else:
                    swipe([0.5, 0.33], [0.5, 0.78])
                    print("向上滑")
            if n > 10:
                n = 0
        install_Button = c(type="Button", name="安装")
        install_Button_2 = c(type="Button", name="INSTALL")
        open_Button = c(type="Button", name="打开")
        open_Button_2 = c(type="Button", name="OPEN")
        while 1:
            ##点击目标App
            print("安装中...")
            if game.exists:
                game.click()
            if install_Button.exists is True:
                ##点击安装按钮
                print("如果安装按钮在则点击", install_Button.exists)
                install_Button.click()
                time.sleep(15)
            if install_Button_2.exists is True:
                ##点击安装按钮
                print("如果英文按钮在则点击", install_Button_2.exists)
                install_Button_2.click()
                time.sleep(15)
            if open_Button_2.exists:
                print("已经安装成功")
                break
            if open_Button.exists:
                print("已经安装成功")
                break
            time.sleep(5)
        c.app_stop("com.apple.TestFlight")
        c.close()


########################### 123  账号登录，App下载等步骤
class SH_123():

    ##### 123
    def check_acount_ios14(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        c.close()
        c.app_stop("com.apple.Preferences")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.Preferences")
                App_Store = c(type="Cell", name="App Store", label="App Store",
                              enabled="true")
                e = c(enabled="true", visible="true")
                App_Store_sign = 0
                while 1:
                    print("寻找iTunes Store 与 App Store.....")
                    swipe([0.5, 0.6], [0.5, 0.45])
                    if App_Store.visible:
                        print("iTunes Store 与 App Store寻找到了1111")
                        App_Store.click()
                        break

            for i in range(3):
                print('滑到底部')
                swipe([0.5, 0.7], [0.5, 0.3])
                time.sleep(2)
            time.sleep(3)
            print("判断111111111111111111")
            c(type="Cell", enabled="true", visible="true")[-3].wait(timeout=280)
            print("判断完毕2222222222222222222222")
            if c(type="Cell", enabled="true", visible="true")[-3].exists:
                aount = c(type="Cell", enabled="true", visible="true")[-3].label
                print("=======================================")
                print("=================", aount, "============")
                print("=======================================")
                if aount == "登录":
                    c(type="Cell", name="登录", enabled="true", visible="true").click()
                    c(type='TextField', value='电子邮件或电话').set_text(acount)  ##账号
                    # 点击登录再输入密码
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    time.sleep(2)
                    c(value="密码", label="").set_text(pwd)  ##密码
                    time.sleep(1)
                    # 再次点击登录
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    sleep(20)
                else:
                    if len(aount.split('ID：')) > 0:
                        test_aount = aount.split('ID：')[1]
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            c(type="Cell", enabled="true", visible="true")[-3].click()  ##点击账号处，弹出退出页面
                            c(type="Button", name="退出登录", label="退出登录", enabled="true",
                              visible="true").click()  ##点击退出登录按钮
                            time.sleep(8)
                            c(type="Cell", name="登录", enabled="true", visible="true").click()
                            c(type='TextField', value='电子邮件或电话').set_text(acount)  ##账号
                            # 点击登录再输入密码
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            time.sleep(2)
                            c(value="密码", label="").set_text(pwd)  ##密码
                            time.sleep(1)
                            # 再次点击登录
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            sleep(20)
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    print("认证完毕或不需要认证，退出！")
                    break
            c.app_stop("com.apple.Preferences")
            print("---------------SH_123--------登录成功--------------------")
            c.close()
        except Exception as e:
            print(e)

    # 123
    def loginAppStore(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        print("----")
        c.close()
        c.app_stop("com.apple.AppStore")
        print("---------------SH_123--------------------")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.AppStore")
                time.sleep(5)
                continueButton = c(type='Button', name='继续', label='继续', enabled='true')
                continueButton_182 = c(type='StaticText', name='继续', label='继续', enabled='true')
                sayAfterButton_182 = c(type='Button', name='以后再说', label='以后再说', enabled='true')

                if sayAfterButton_182.exists:
                    print('----------点击以后再说-----------')
                    sayAfterButton_182.click()

                if continueButton.exists:
                    print('----------点击继续-----------')
                    continueButton.click()

                if continueButton_182.exists:
                    print('----------点击 SH_123设备 继续-----------')
                    continueButton_182.click()
                print("--------------点击我的账户--------------")
                # myAccountButton = c(type="Button",nameContains='我的账户', visible='true',
                #               enabled="true")
                # myAccountButton.click()
                ### 用坐标
                time.sleep(10)
                click([0.908, 0.128])
                print("--------点击我的账户完毕-----")
                time.sleep(3)
                e = c(enabled="true", visible="true")[0]
            # 判断是否登录
            c(type="StaticText", enabled="true", visible="true").wait(timeout=280)
            if c(type="StaticText", enabled="true", visible="true").exists:
                AppleID = c(type="Cell", enabled="true", visible="true").label
                print("=======================================")
                print("=================", AppleID, type(AppleID), "============")
                print("=======================================")
                if AppleID == None:
                    # 进行登录
                    c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(acount)  ##账号
                    c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(pwd)  ##密码
                    c(type="Cell", label="登录", enabled="true", visible="true").click()  # 点击登录
                    sleep(20)
                else:
                    if len(AppleID.split(',')) > 0:
                        test_aount = AppleID.split(',')[1].strip()
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print(f"账号不正确，退出重新登录：{test_aount}")
                            while True:
                                print('--------检查退出登录是否存在-------')
                                try:
                                    try:
                                        c(type='StaticText', name='登出', visible='true').click()
                                        time.sleep(5)
                                        print("--------------------点击登出成功----------------")
                                        break
                                    except:
                                        pass
                                    c(type='StaticText', name='退出登录', visible='true').click()
                                    time.sleep(5)
                                    print("--------------------点击退出登录成功----------------")
                                    break
                                except:
                                    print("---------滑动查找退出登录-----------")
                                    swipe([0.5, 0.7], [0.5, 0.3])
                                    time.sleep(1)

                            for i in range(2):
                                print("---------向上滑动-----------")
                                swipe([0.5, 0.3], [0.5, 0.7])
                                time.sleep(1)
                            # 进行登录
                            c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(
                                acount)  ##账号
                            c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(
                                pwd)  ##密码
                            c(type="Cell", label="登录", enabled="true",
                              visible="true").click()  # 点击登录
                            sleep(20)
                ### 如果没有双重认证的,则需要进行确认
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    break

            c.app_stop("com.apple.AppStore")
            c.close()
        except Exception as e:
            print(e)

    def game_download(self, c, name):
        c.app_stop("com.apple.TestFlight")
        c.app_start("com.apple.TestFlight")
        if c(type='Button', name='Continue Button').exists:
            c(type='Button', name='Continue Button').click()
        sleep(8)
        game = c(type="Cell", name=name)
        n = 0
        while 1:
            n += 1
            if n <= 6:
                if game.exists:
                    print("已找到")
                    break
                else:
                    swipe([0.5, 0.6], [0.5, 0.4])
                    print("向下滑")
            if 5 < n < 13:
                if game.exists:
                    break
                else:
                    swipe([0.5, 0.4], [0.5, 0.6])
                    print("向上滑")
            if n > 10:
                n = 0

        install_Button = c(type="Button", name="安装")
        install_Button_2 = c(type="Button", name="INSTALL")
        open_Button = c(type="Button", name="打开")
        open_Button_2 = c(type="Button", name="OPEN")
        while 1:
            ##点击目标App
            print("SH_123 安装中...")
            if game.exists:
                game.click()
            if install_Button.exists is True:
                ##点击安装按钮
                print("如果安装按钮在则点击", install_Button.exists)
                install_Button.click()
                time.sleep(15)
            if install_Button_2.exists is True:
                ##点击安装按钮
                print("如果英文按钮在则点击", install_Button_2.exists)
                install_Button_2.click()
                time.sleep(15)
            if open_Button_2.exists:
                print("SH_123已经安装成功")
                break
            if open_Button.exists:
                print("SH_123已经安装成功")
                break
            time.sleep(5)
        c.app_stop("com.apple.TestFlight")
        c.close()


########################### 186  账号登录，App下载等步骤
class SH_186():
    #########  账号登录，App下载等步骤
    def check_acount_ios14(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        c.close()
        c.app_stop("com.apple.Preferences")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.Preferences")
                App_Store = c(type="Cell", name="App Store", label="App Store",
                              enabled="true")
                e = c(enabled="true", visible="true")
                App_Store_sign = 0
                while 1:
                    print("寻找iTunes Store 与 App Store.....")
                    swipe([0.5, 0.6], [0.5, 0.45])
                    if App_Store.visible:
                        print("iTunes Store 与 App Store寻找到了1111")
                        App_Store.click()
                        break

            for i in range(3):
                print('滑到底部')
                swipe([0.5, 0.7], [0.5, 0.3])
                time.sleep(2)
            c(type="Cell", enabled="true", visible="true").wait(timeout=280)
            if c(type="Cell", enabled="true", visible="true").exists:
                aount = c(type="Cell", enabled="true", visible="true")[-1].label
                print("=======================================")
                print("=================", aount, "============")
                print("=======================================")
                if aount == "登录":
                    print("-------------186进行apple id 登录---------")
                    c(type="Cell", enabled="true", visible="true")[-1].click()
                    c(value="电子邮件或电话", label="").set_text(acount)  ##账号
                    time.sleep(3)
                    print("输入账号完毕")
                    c(type="SecureTextField", value="密码", enabled="true", visible="true").set_text(pwd)  ##密码
                    c(type="Button", name="登录", label="登录").click()
                    sleep(20)
                else:
                    if len(aount.split('ID：')) > 0:
                        test_aount = aount.split('ID：')[1]
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            c(type="Cell", enabled="true", visible="true")[-1].click()  ##点击账号处，弹出退出页面
                            c(type="Button", name="退出登录", label="退出登录", enabled="true",
                              visible="true").click()  ##点击退出登录按钮
                            time.sleep(8)
                            c(type="Cell", enabled="true", visible="true")[-1].click()  # 再次点击登录进行登录
                            c(value="电子邮件或电话", label="").set_text(acount)  ##账号
                            time.sleep(3)
                            c(value="密码", label="").set_text(pwd)  ##密码
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()  # 点击登录
                            sleep(20)
            c.app_stop("com.apple.Preferences")
            c.close()
        except Exception as e:
            print(e)

    def loginAppStore(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        print("----")
        c.close()
        c.app_stop("com.apple.AppStore")
        print("-----------------------------------")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.AppStore")
                time.sleep(5)
                continueButton = c(type='Button', name='继续', label='继续', enabled='true')
                if continueButton.exists:
                    print('----------点击继续-----------')
                    continueButton.click()
                print("--------------点击我的账户--------------")
                time.sleep(10)
                # myAccountButton = c(type="Button", name="我的帐户", label="我的帐户",
                #                     enabled="true")
                # myAccountButton.click()
                for i in range(10):
                    click([0.909, 0.128])
                    time.sleep(1)
                    if c(type='Button', name='完成').exists:
                        break
                time.sleep(3)
            # 判断是否登录
            c(type="StaticText", enabled="true", visible="true").wait(timeout=280)
            if c(type="StaticText", enabled="true", visible="true").exists:
                AppleID = c(type="Cell", enabled="true", visible="true").label
                print("=======================================")
                print("=================", AppleID, type(AppleID), "============")
                print("=======================================")
                if AppleID == None:
                    # 进行登录
                    c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(acount)  ##账号
                    c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(pwd)  ##密码
                    c(type="Cell", name="登录", label="登录", enabled="true", visible="true").click()  # 点击登录
                    sleep(20)
                else:
                    if len(AppleID.split(',')) > 0:
                        test_aount = AppleID.split(',')[1].strip()
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            while True:
                                print('--------检查退出登录是否存在-------')
                                try:
                                    c(type='Cell', name='退出登录', visible='true').click()
                                    time.sleep(5)
                                    break
                                except:
                                    print("---------滑动查找退出登录-----------")
                                    swipe([0.5, 0.7], [0.5, 0.3])
                                    time.sleep(1)

                            for i in range(2):
                                print("---------向上滑动-----------")
                                swipe([0.5, 0.3], [0.5, 0.7])
                                time.sleep(1)

                            # 进行登录
                            c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(
                                acount)  ##账号
                            c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(
                                pwd)  ##密码
                            c(type="Cell", name="登录", label="登录", enabled="true",
                              visible="true").click()  # 点击登录
                            sleep(20)
            ### 如果没有双重认证的,则需要进行确认
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    print("认证完毕或不需要认证，退出！")
                    break
            c.app_stop("com.apple.AppStore")
            c.close()
        except Exception as e:
            print(e)

    def game_download(self, c, name):
        c.app_stop("com.apple.TestFlight")
        c.app_start("com.apple.TestFlight")
        if c(type='Button', name='Continue Button').exists:
            c(type='Button', name='Continue Button').click()
        sleep(8)
        sroll = c(enabled="true", visible="true")

        game = c(type="Cell", name=name)
        n = 0
        while 1:
            n += 1
            if n <= 6:
                if game.exists:
                    print("已找到")
                    break
                else:
                    swipe([0.5, 0.6], [0.5, 0.4])
                    print("向下滑")
            if 5 < n < 13:
                if game.exists:
                    break
                else:
                    swipe([0.5, 0.4], [0.5, 0.6])
                    print("向上滑")
            if n > 10:
                n = 0

        install_Button = c(type="Button", name="安装")
        install_Button_2 = c(type="Button", name="INSTALL")
        open_Button = c(type="Button", name="打开")
        open_Button_2 = c(type="Button", name="OPEN")
        while True:
            ##点击目标App
            print("安装中...")
            try:
                if game.exists:
                    game.click()
                if install_Button.exists is True:
                    ##点击安装按钮
                    print("如果安装按钮在则点击", install_Button.exists)
                    install_Button.click()
                    time.sleep(15)

                if install_Button_2.exists is True:
                    ##点击安装按钮
                    print("如果英文按钮在则点击", install_Button_2.exists)
                    install_Button_2.click()
                    time.sleep(15)

                if open_Button_2.exists:
                    print("已经安装成功")
                    break

                if open_Button.exists:
                    print("已经安装成功")
                    break
            except Exception:
                print("-----------186下载应用出错-------", Exception)
            time.sleep(5)
        c.app_stop("com.apple.TestFlight")
        c.close()


########################### 182  账号登录，App下载等步骤
class SH_182():
    def check_acount_ios14(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        c.close()
        c.app_stop("com.apple.Preferences")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.Preferences")
                App_Store = c(type="Cell", name="App Store", label="App Store",
                              enabled="true")
                App_Store_sign = 0
                while 1:
                    print("寻找iTunes Store 与 App Store.....")
                    swipe([0.5, 0.6], [0.5, 0.45])
                    if App_Store.visible:
                        print("iTunes Store 与 App Store寻找到了1111")
                        App_Store.click()
                        break
            for i in range(3):
                print('滑到底部')
                swipe([0.5, 0.7], [0.5, 0.3])
                time.sleep(2)
            c(type="Cell", enabled="true", visible="true")[-3].wait(timeout=280)
            if c(type="Cell", enabled="true", visible="true")[-3].exists:
                aount = c(type="Cell", enabled="true", visible="true")[-3].label
                print("=======================================")
                print("=================", aount, "============")
                print("=======================================")
                if aount == "登录":
                    c(type="Cell", enabled="true", visible="true")[-3].click()
                    c(value="电子邮件或电话", label="").set_text(acount)  ##账号
                    # 点击登录再输入密码
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    c(value="密码", label="").set_text(pwd)  ##密码
                    time.sleep(1)
                    # 再次点击登录
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    sleep(20)
                else:
                    if len(aount.split('ID：')) > 0:
                        test_aount = aount.split('ID：')[1]
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            c(type="Cell", enabled="true", visible="true")[-3].click()  ##点击账号处，弹出退出页面
                            c(type="Button", name="退出登录", label="退出登录", enabled="true",
                              visible="true").click()  ##点击退出登录按钮
                            time.sleep(8)
                            c(type="Cell", enabled="true", visible="true")[-3].click()  # 再次点击登录进行登录
                            c(value="电子邮件或电话", label="").set_text(acount)  ##账号
                            # 点击登录再输入密码
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            c(value="密码", label="").set_text(pwd)  ##密码
                            time.sleep(1)
                            # 再次点击登录
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            sleep(20)
                        ### 如果没有双重认证的,则需要进行确认
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    print("认证完毕或不需要认证，退出！")
                    break
            c.app_stop("com.apple.Preferences")
            c.close()
        except Exception as e:
            print(e)

    def loginAppStore(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        print("----")
        c.close()
        c.app_stop("com.apple.AppStore")
        print("-----------------------------------")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.AppStore")
                time.sleep(5)
                continueButton = c(type='Button', name='继续', label='继续', enabled='true')
                continueButton_182 = c(type='StaticText', name='继续', label='继续', enabled='true')
                sayAfterButton_182 = c(type='Button', name='以后再说', label='以后再说', enabled='true')

                if sayAfterButton_182.exists:
                    print('----------点击以后再说-----------')
                    sayAfterButton_182.click()

                if continueButton.exists:
                    print('----------点击继续-----------')
                    continueButton.click()

                if continueButton_182.exists:
                    print('----------点击 sh-sj-182设备 继续-----------')
                    continueButton_182.click()
                print("--------------点击我的账户--------------")
                # myAccountButton = c(type="Button", label="我的帐户",
                #                     enabled="true")
                # myAccountButton.click()
                for i in range(10):
                    click([0.909, 0.128])
                    time.sleep(1)
                    if c(type='Button', name='完成').exists:
                        break
                time.sleep(3)
                # e = c(enabled="true", visible="true")[0]
            # 判断是否登录
            c(type="StaticText", enabled="true", visible="true").wait(timeout=280)
            if c(type="StaticText", enabled="true", visible="true").exists:
                AppleID = c(type="Cell", enabled="true", visible="true").label
                print("=======================================")
                print("=================", AppleID, type(AppleID), "============")
                print("=======================================")
                if AppleID == None:
                    # 进行登录
                    c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(acount)  ##账号
                    c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(pwd)  ##密码
                    c(type="Cell", label="登录", enabled="true", visible="true").click()  # 点击登录
                    sleep(20)
                else:
                    if len(AppleID.split(',')) > 0:
                        test_aount = AppleID.split(',')[1].strip()
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print(f"账号不正确，退出重新登录：{test_aount}")
                            while True:
                                print('--------检查退出登录是否存在-------')
                                try:
                                    c(type='StaticText', name='退出登录', visible='true').click()
                                    time.sleep(5)
                                    print("--------------------点击退出登录成功----------------")
                                    break
                                except:
                                    print("---------滑动查找退出登录-----------")
                                    swipe([0.5, 0.7], [0.5, 0.3])
                                    time.sleep(1)

                            for i in range(4):
                                print("---------向上滑动-----------")
                                swipe([0.5, 0.3], [0.5, 0.7])
                                time.sleep(1)
                            # 进行登录
                            c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(
                                acount)  ##账号
                            c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(
                                pwd)  ##密码
                            c(type="Cell", label="登录", enabled="true",
                              visible="true").click()  # 点击登录
                            sleep(20)

            ### 如果没有双重认证的,则需要进行确认
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    print("认证完毕或不需要认证，退出！")
                    break
            c.app_stop("com.apple.AppStore")
            c.close()
        except Exception as e:
            print(e)

    def game_download(self, c, name):
        c.app_stop("com.apple.TestFlight")
        c.app_start("com.apple.TestFlight")
        if c(type='Button', name='Continue Button').exists:
            c(type='Button', name='Continue Button').click()
        sleep(8)
        game = c(type="Cell", name=name)
        if name == "Harvest Town - Pixel Sim RPG":
            print("奶牛朝下滑")
            swipe([0.5, 0.6], [0.5, 0.4])
            print("向下滑")
        n = 0
        while 1:
            n += 1
            if n <= 6:
                if game.exists:
                    print("已找到")
                    break
                else:
                    swipe([0.5, 0.6], [0.5, 0.4])
                    print("向下滑")
            if 5 < n < 13:
                if game.exists:
                    break
                else:
                    swipe([0.5, 0.4], [0.5, 0.6])
                    print("向上滑")
            if n > 10:
                n = 0

        install_Button = c(type="Button", name="安装")
        install_Button_2 = c(type="Button", name="INSTALL")
        open_Button = c(type="Button", name="打开")
        open_Button_2 = c(type="Button", name="OPEN")
        while 1:
            ##点击目标App
            print("--182---安装中...")
            if game.exists:
                game.click()
            # print("验证安装按钮在不在", install_Button.exists)
            # print("验证英文安装按钮在不在", install_Button_2.exists)
            if install_Button.exists is True:
                ##点击安装按钮
                print("如果安装按钮在则点击", install_Button.exists)
                install_Button.click()
                time.sleep(15)

            if install_Button_2.exists is True:
                ##点击安装按钮
                print("如果英文按钮在则点击", install_Button_2.exists)
                install_Button_2.click()
                time.sleep(15)

            if open_Button_2.exists:
                print("--182---已经安装成功")
                break

            if open_Button.exists:
                print("--182---已经安装成功")
                break
            time.sleep(5)
        c.app_stop("com.apple.TestFlight")
        c.close()


########################### 192  账号登录，App下载等步骤
class SH_192():
    def check_acount(self, c, acount=None, pwd=None):
        ###ios版本 14以下
        c.close()
        c.app_stop("com.apple.Preferences")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.Preferences")
                App_Store = c(type="Cell", name="iTunes Store 与 App Store", label="iTunes Store 与 App Store",
                              enabled="true")
                App_Store_sign = 0
                while 1:
                    print("寻找iTunes Store 与 App Store.....")
                    swipe([0.5, 0.7], [0.5, 0.3])
                    time.sleep(1)
                    if App_Store.visible:
                        print("iTunes Store 与 App Store寻找到了1111")
                        App_Store.click()
                        break

            # for i in range(3):
            #     print('滑到底部')
            #     swipe([0.5, 0.7], [0.5, 0.3])
            #     time.sleep(2)
            #### 以下的print别删，删了就会报错
            print("———————0192————————等待cell元素出现———————————————————")
            c(type="Cell", enabled="true", visible="true").wait(timeout=280)
            print("———————0192————————cell元素已出现出现———————————————————")
            if c(type="Cell", enabled="true", visible="true").exists:
                print("———————0192————————cell元素信息读取———————————————————")
                time.sleep(2)
                aount = c(type="Cell", enabled="true", visible="true").label
                print("=======================================")
                print("=================", aount, "============")
                print("=======================================")
                if aount == "登录":
                    c(type="Cell", enabled="true", visible="true").click()
                    c(value="Apple ID", label="").set_text(acount)  ##账号
                    time.sleep(1)
                    print("———————0192————————点击密码框———————————————————")
                    c(value="密码", label="").click()
                    print("———————0192————————输入密码———————————————————")
                    c(value="密码", label="").set_text(pwd)
                    print("———————0192————————输入密码成功———————————————————")
                    # text(pwd)
                    try:
                        c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    except:
                        pass
                    sleep(20)
                else:
                    if len(aount.split('ID：')) > 0:
                        test_aount = aount.split('ID：')[1]
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            c(type="Cell", enabled="true", visible="true").click()  ##点击账号处，弹出退出页面
                            time.sleep(2)
                            c(type="Button", name="退出登录", label="退出登录", enabled="true",
                              visible="true").click()  ##点击退出登录按钮
                            c(type="Cell", enabled="true", visible="true").click()
                            c(value="Apple ID", label="").set_text(acount)  ##账号
                            c(value="密码", label="").click()  ##密码
                            time.sleep(1)
                            text(pwd)
                            try:
                                c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            except:
                                pass
                            sleep(20)

            ### 如果没有双重认证的,则需要进行确认
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    print("认证完毕或不需要认证，退出！")
                    break
            c.app_stop("com.apple.Preferences")
            c.close()
        except Exception as e:
            print(e)

    def game_download(self, c, name):
        c.app_stop("com.apple.TestFlight")
        c.app_start("com.apple.TestFlight")
        sleep(3)
        sroll = c(enabled="true", visible="true")
        if c(type='Button', name='Continue Button').exists:
            c(type='Button', name='Continue Button').click()

        time.sleep(2)

        game = c(type="Cell", name=name)
        n = 0
        while 1:
            n += 1
            if n <= 6:
                if game.exists:
                    print("已找到")
                    break
                else:
                    swipe([0.5, 0.78], [0.5, 0.43])
                    print("向下滑")
            if 5 < n < 13:
                if game.exists:
                    break
                else:
                    swipe([0.5, 0.4], [0.5, 0.6])
                    print("向上滑")
            if n > 10:
                n = 0

        install_Button = c(type="Button", name="安装")
        install_Button_2 = c(type="Button", name="INSTALL")
        open_Button = c(type="Button", name="打开")
        open_Button_2 = c(type="Button", name="OPEN")
        while 1:
            ##点击目标App
            print("安装中...")
            if game.exists:
                game.click()
            if install_Button.exists is True:
                ##点击安装按钮
                print("如果安装按钮在则点击", install_Button.exists)
                install_Button.click()
                time.sleep(15)

            if install_Button_2.exists is True:
                ##点击安装按钮
                print("如果英文按钮在则点击", install_Button_2.exists)
                install_Button_2.click()
                time.sleep(15)

            if open_Button_2.exists:
                print("已经安装成功")
                break

            if open_Button.exists:
                print("已经安装成功")
                break

            time.sleep(5)
        c.app_stop("com.apple.TestFlight")
        c.close()


###################################################################   平板
########################### 067  账号登录，App下载等步骤
class SH_067():
    #########  账号登录，App下载等步骤

    @classmethod
    def check_acount_ios14(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        c.close()
        c.app_stop("com.apple.Preferences")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.Preferences")
                App_Store = c(type="Cell", name="iTunes Store与App Store", label="iTunes Store与App Store",
                              enabled="true")

                App_Store_sign = 0
                while 1:
                    print("寻找设备的iTunes Store 与 App Store.....")
                    for i in range(2):
                        time.sleep(1)
                        if App_Store.visible:
                            App_Store_sign = 1
                            print("设备的iTunes Store 与 App Store 寻找到了")
                            break
                        print("开始滑动")
                        swipe([0.175, 0.842], [0.175, 0.299])  # 手上滑
                    if App_Store.visible:
                        App_Store_sign = 1
                        print("设备的iTunes Store 与 App Store 寻找到了")
                        break
                    if App_Store_sign == 1:
                        pass
                    else:
                        for i in range(1):
                            swipe([0.175, 0.299], [0.175, 0.842])  # 手下滑
                            if App_Store.visible:
                                App_Store_sign = 1
                                print("iTunes Store 与 App Store寻找到了")
                                break
                App_Store.click()

            for i in range(3):
                print('滑到底部')
                swipe([0.5, 0.7], [0.5, 0.3])
                time.sleep(2)

            time.sleep(3)
            print("判断111111111111111111")
            # c(type="Cell", enabled="true", visible="true")[0].wait(timeout=280)
            # print("判断完毕2222222222222222222222")

            if c(type="Cell", enabled="true", visible="true")[0].exists:
                aount = c(type="Cell", enabled="true", visible="true")[-1].label
                print("=======================================")
                print("=================", aount, "============")
                print("=======================================")
                if aount == "登录":
                    c(type="Cell", name="登录", enabled="true", visible="true").click()
                    time.sleep(5)
                    c(type='TextField', value='电子邮件或电话').set_text(acount)  ##账号
                    time.sleep(1)
                    c(type='SecureTextField', value="密码").set_text(pwd)  ##密码
                    # 再次点击登录
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    sleep(20)
                else:
                    if len(aount.split('ID：')) > 0:
                        test_aount = aount.split('ID：')[1]
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            c(type="Cell", enabled="true", visible="true")[-1].click()
                            time.sleep(3)
                            c(type='Button', name='退出登录').click()
                            c(type="Cell", name="登录", enabled="true", visible="true").click()
                            #### 登录

                            time.sleep(5)
                            c(type='TextField', value='电子邮件或电话').set_text(acount)  ##账号
                            time.sleep(1)
                            c(type='SecureTextField', value="密码").set_text(pwd)  ##密码
                            # 再次点击登录
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            sleep(20)
            c.app_stop("com.apple.Preferences")
            c.close()
        except Exception as e:
            print(e)

    @classmethod
    def loginAppStore(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        print("----")
        c.close()
        c.app_stop("com.apple.AppStore")
        print("-----------------------------------")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动App Store")
                time.sleep(5)
                c.app_start("com.apple.AppStore")
                time.sleep(10)
                continueButton = c(type='Button', name='继续', label='继续', enabled='true')
                continueButton_182 = c(type='StaticText', name='继续', label='继续', enabled='true')
                sayAfterButton_182 = c(type='Button', name='以后再说', label='以后再说', enabled='true')

                if sayAfterButton_182.exists:
                    print('----------点击以后再说-----------')
                    sayAfterButton_182.click()

                if continueButton.exists:
                    print('----------点击继续-----------')
                    continueButton.click()

                if continueButton_182.exists:
                    print('----------点击 sh-sj-067设备 继续-----------')
                    continueButton_182.click()
                print("--------------点击我的账户--------------")
                # myAccountButton = c(type="Button",nameContains='我的账户', visible='true',
                #               enabled="true")
                # myAccountButton.click()
                ### 用坐标
                time.sleep(3)
                for i in range(10):
                    click([0.914, 0.08])
                    time.sleep(1)
                    if c(type='Button', name='完成').exists:
                        break
                print("--------点击我的账户完毕-----")
                time.sleep(3)
                e = c(type='CollectionView', name='CollectionView', enabled="true", visible="true")
            # 判断是否登录
            c(type="StaticText", enabled="true", visible="true").wait(timeout=280)
            if c(type="StaticText", enabled="true", visible="true").exists:
                AppleID = c(type="Cell", enabled="true", visible="true")[0].label
                print("=======================================")
                print("=================", AppleID, type(AppleID), "============")
                print("=======================================")
                if AppleID == None:
                    # 进行登录
                    time.sleep(3)
                    c(type="TextField", name="Apple ID").set_text(acount)  ##账号
                    c(type="SecureTextField", name="密码").set_text(pwd)  ##密码
                    c(type="StaticText", label="登录").click()  # 点击登录
                    sleep(20)
                else:
                    if len(AppleID.split(',')) > 0:
                        test_aount = AppleID.split(',')[1].strip()
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print(f"账号不正确，退出重新登录：{test_aount}")
                            while True:
                                print('--------检查退出登录是否存在-------')
                                try:
                                    c(type='Cell', label='退出登录', visible='true').click(timeout=10)
                                    time.sleep(5)
                                    print("--------------------点击退出登录成功----------------")
                                    break
                                except:
                                    print("---------滑动查找退出登录-----------")
                                    # 上点 [0.5,0.3]  下点[0.5,0.7]
                                    # 向下滑动
                                    swipe([0.5, 0.7], [0.5, 0.3])
                                    swipe([0.5, 0.7], [0.5, 0.3])
                                    swipe([0.5, 0.7], [0.5, 0.3])

                            for i in range(3):
                                print("---------向上滑动-----------")
                                swipe([0.5, 0.3], [0.5, 0.7])

                            time.sleep(3)
                            # 进行登录
                            c(type="TextField", name="Apple ID").set_text(acount)  ##账号
                            c(type="SecureTextField", name="密码").set_text(pwd)  ##密码
                            c(type="StaticText", label="登录").click()  # 点击登录
                            sleep(20)

            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    break
            c.app_stop("com.apple.AppStore")
            c.close()
        except Exception as e:
            print(e)

    @classmethod
    def game_download(self, c, name):
        c.app_stop("com.apple.TestFlight")
        c.app_start("com.apple.TestFlight")
        if c(type='Button', name='Continue Button').exists:
            c(type='Button', name='Continue Button').click()
        sleep(8)
        # c(type='Button', name='App').click()  # 点击左上角的 <APP
        c(type='Button', visible='true').click(timeout=15)  # 点击左上角的 <APP
        game = c(type="Cell", name=name)
        n = 0
        while 1:
            n += 1
            if n <= 6:
                if game.exists:
                    print("已找到")
                    break
                else:
                    swipe([0.183, 0.751], [0.183, 0.153])
                    print("手向上滑,找下面的内容")
            if 5 < n < 13:
                if game.exists:
                    break
                else:
                    swipe([0.183, 0.153], [0.183, 0.751])
                    print("手向下滑,找上面的内容")
            if n > 10:
                n = 0
        install_Button = c(type="Button", name="安装")
        install_Button_2 = c(type="Button", name="INSTALL")
        open_Button = c(type="Button", name="打开")
        open_Button_2 = c(type="Button", name="OPEN")
        while 1:
            ##点击目标App
            print("安装中...")
            if game.exists:
                game.click()
            if install_Button.exists is True:
                ##点击安装按钮
                print("如果安装按钮在则点击", install_Button.exists)
                install_Button.click()
                time.sleep(15)
            if install_Button_2.exists is True:
                ##点击安装按钮
                print("如果英文按钮在则点击", install_Button_2.exists)
                install_Button_2.click()
                time.sleep(15)
            if open_Button_2.exists:
                print("已经安装成功")
                break
            if open_Button.exists:
                print("已经安装成功")
                break
            time.sleep(5)
        c.app_stop("com.apple.TestFlight")
        c.close()


########################### 100  账号登录，App下载等步骤
class SH_100():
    #########  账号登录，App下载等步骤
    def check_acount_ios14(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        c.close()
        c.app_stop("com.apple.Preferences")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动设置")
                c.app_start("com.apple.Preferences")
                App_Store = c(type="Cell", name="App Store", label="App Store",
                              enabled="true")
                App_Store_sign = 0
                while 1:
                    print("寻找ios14设备+的App Store.....")
                    if App_Store.visible:
                        App_Store_sign = 1
                        print("寻找ios14设备+ 的  App Store寻找到了")
                        break

                    for i in range(2):
                        print("开始滑动")
                        swipe([0.175, 0.842], [0.175, 0.299])  # 手上滑
                        if App_Store.visible:
                            App_Store_sign = 1
                            print("ios14设备+ 的  App Store寻找到了")
                            break
                    if App_Store.visible:
                        App_Store_sign = 1
                        print("寻找ios14设备+ 的  App Store寻找到了")
                        break
                    if App_Store_sign == 1:
                        pass
                    else:
                        for i in range(1):
                            swipe([0.175, 0.299], [0.175, 0.842])  # 手下滑
                            if App_Store.visible:
                                App_Store_sign = 1
                                print("iTunes Store 与 App Store寻找到了")
                                break
                App_Store.click()
            for i in range(3):
                print('滑到底部')
                swipe([0.5, 0.7], [0.5, 0.3])
                time.sleep(2)
            time.sleep(3)
            c(type="Cell", enabled="true", visible="true")[-3].wait(timeout=280)
            if c(type="Cell", enabled="true", visible="true")[-3].exists:
                aount = c(type="Cell", enabled="true", visible="true")[-3].label
                print("=======================================")
                print("=================", aount, "============")
                print("=======================================")
                if aount == "登录":
                    c(type="Cell", name="登录", enabled="true", visible="true").click()
                    c(type='TextField', value='电子邮件或电话').set_text(acount)  ##账号
                    # 点击登录再输入密码
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    time.sleep(3)
                    c(type='SecureTextField', value="密码").set_text(pwd)  ##密码
                    time.sleep(5)
                    # 再次点击登录
                    c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                    sleep(20)
                else:
                    if len(aount.split('ID：')) > 0:
                        test_aount = aount.split('ID：')[1]
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print("账号不正确，退出重新登录")
                            c(type="Cell", enabled="true", visible="true")[-3].click()  ##点击账号处，弹出退出页面
                            time.sleep(2)
                            c(type="Button", name="退出登录", label="退出登录", enabled="true",
                              visible="true").click()  ##点击退出登录按钮
                            print("-------------------------")
                            time.sleep(5)
                            c(type="Cell", name="登录", enabled="true", visible="true").click()
                            c(type='TextField', value='电子邮件或电话').set_text(acount)  ##账号
                            # 点击登录再输入密码
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            time.sleep(3)
                            c(type='SecureTextField', value="密码").set_text(pwd)  ##密码
                            time.sleep(5)
                            # 再次点击登录
                            c(type="Button", name="登录", label="登录", enabled="true", visible="true").click()
                            sleep(20)
            c.app_stop("com.apple.Preferences")
            c.close()
        except Exception as e:
            print(e)

    def loginAppStore(self, c, acount=None, pwd=None):
        ###ios版本 14以上
        print("----")
        c.close()
        c.app_stop("com.apple.AppStore")
        print("-----------------------------------")
        try:
            if acount is None:
                print("请输入账号密码")
                return "error"
            else:
                print("启动App Store")
                time.sleep(5)
                c.app_start("com.apple.AppStore")
                time.sleep(10)
                continueButton = c(type='Button', name='继续', label='继续', enabled='true')
                continueButton_182 = c(type='StaticText', name='继续', label='继续', enabled='true')
                sayAfterButton_182 = c(type='Button', name='以后再说', label='以后再说', enabled='true')

                if sayAfterButton_182.exists:
                    print('----------点击以后再说-----------')
                    sayAfterButton_182.click()

                if continueButton.exists:
                    print('----------点击继续-----------')
                    continueButton.click()

                if continueButton_182.exists:
                    print('----------点击 sh-sj-100设备 继续-----------')
                    continueButton_182.click()
                print("--------------点击我的账户--------------")
                # myAccountButton = c(type="Button",nameContains='我的账户', visible='true',
                #               enabled="true")
                # myAccountButton.click()
                ### 用坐标
                time.sleep(15)
                for i in range(10):
                    click([0.936, 0.075])
                    time.sleep(1)
                    if c(type='Button', name='完成').exists:
                        break
                print("--------点击我的账户完毕-----")
                time.sleep(3)
            # 判断是否登录
            c(type="StaticText", enabled="true", visible="true").wait(timeout=280)
            if c(type="StaticText", enabled="true", visible="true").exists:
                AppleID = c(type="Cell", enabled="true", visible="true")[0].label
                print("=======================================")
                print("=================", AppleID, type(AppleID), "============")
                print("=======================================")
                if AppleID == None:
                    # 进行登录
                    c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(acount)  ##账号
                    # c(type="SecureTextField", name="密碼", enabled="true", visible="true").set_text(pwd)  ##密码
                    c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(pwd)  ##密码
                    # c(type="StaticText", label="登入", enabled="true", visible="true").click()  # 点击登录
                    c(type="StaticText", label="登录", enabled="true", visible="true").click()  # 点击登录
                    sleep(20)
                else:
                    if len(AppleID.split(',')) > 0:
                        test_aount = AppleID.split(',')[1].strip()
                        if test_aount == acount:
                            print("账号正确", test_aount)
                        else:
                            print(f"账号不正确，退出重新登录：{test_aount}")
                            while True:
                                print('--------检查退出登录是否存在-------')
                                try:
                                    # c(type='Cell', label='登出', visible='true').click()
                                    c(type='Cell', label='退出登录', visible='true').click()
                                    time.sleep(5)
                                    print("--------------------点击退出登录成功----------------")
                                    break
                                except:
                                    print("---------滑动查找退出登录-----------")
                                    for i in range(5):
                                        swipe([0.5, 0.65], [0.5, 0.35])
                                        time.sleep(1)

                            for i in range(6):
                                print("---------滑到上面-----------")
                                swipe([0.5, 0.35], [0.5, 0.65])
                                time.sleep(1)
                            # 进行登录
                            c(type="TextField", name="Apple ID", enabled="true", visible="true").set_text(
                                acount)  ##账号
                            c(type="SecureTextField", name="密码", enabled="true", visible="true").set_text(pwd)  ##密码
                            # c(type="SecureTextField", name="密碼", enabled="true", visible="true").set_text(pwd)  ##密码
                            # c(type="StaticText", label="登入", enabled="true", visible="true").click()  # 点击登录
                            c(type="StaticText", label="登录", enabled="true", visible="true").click()  # 点击登录
                            sleep(20)
                        ### 如果没有双重认证的,则需要进行确认
            while True:
                print("---------------------------双重认证，点击继续------------------------")
                if c(type='Button', name="继续", label="继续").exists:
                    # 点击其他选项
                    c(type="Button", name="其他选项", label="其他选项").click()
                    time.sleep(3)
                    # 点击不升级
                    c(type="Button", name="不升级", label="不升级").click()
                    time.sleep(10)
                    print("---------------双重认证账号登录成功-----------------")
                else:
                    print("认证完毕或不需要认证，退出！")
                    break
            c.app_stop("com.apple.AppStore")
            c.close()
        except Exception as e:
            print(e)

    def game_download(self, c, name):
        try:
            c.app_stop("com.apple.TestFlight")
        except:
            pass
        c.app_start("com.apple.TestFlight")
        if c(type='Button', name='Continue Button').exists:
            c(type='Button', name='Continue Button').click()
        time.sleep(5)
        # if not c(type='Button', name='设置').exists:
        #     print("点击侧边栏")
        #     c(type='Button', name='ToggleSidebar', label='隐藏边栏').click()
        # sleep(8)
        c(type='Button', name='BackButton').click()  # 点击左上角的 <APP
        # sroll = c(enabled="true", visible="true")
        game = c(type="Cell", name=name)
        n = 0
        while 1:
            n += 1
            if n <= 6:
                if game.exists:
                    print("已找到")
                    break
                else:
                    swipe([0.183, 0.751], [0.183, 0.153])
                    print("手向上滑,找下面的内容")
            if 5 < n < 13:
                if game.exists:
                    break
                else:
                    swipe([0.183, 0.153], [0.183, 0.751])
                    print("手向下滑,找上面的内容")
            if n > 10:
                n = 0

        install_Button = c(type="Button", name="安装")
        install_Button_2 = c(type="Button", name="INSTALL")
        open_Button = c(type="Button", name="打开")
        open_Button_2 = c(type="Button", name="OPEN")
        ToggleSidebar_Button = c(type='Button', name='ToggleSidebar')
        while 1:
            ##点击目标游戏
            print("SH-SJ-100-安装中...")
            if game.exists:
                game.click()
                try:
                    ToggleSidebar_Button.click(timeout=2)
                    print("点击隐藏侧边栏成功")
                except:
                    pass
            else:
                print("SH-SJ-100-游戏不在游戏不在游戏不在")
            print("验证1_1", install_Button.exists)
            print("验证1_2", install_Button_2.exists)
            if install_Button.exists is True:
                ##点击安装按钮
                print("SH-SJ-100-验证2_1", install_Button.exists)
                install_Button.click()
                time.sleep(15)

            if install_Button_2.exists is True:
                ##点击安装按钮
                print("SH-SJ-100-验证2_2", install_Button_2.exists)
                install_Button_2.click()
                time.sleep(15)

            if open_Button_2.exists:
                print("SH-SJ-100-已经安装成功")
                break

            if open_Button.exists:
                print("SH-SJ-100-已经安装成功")
                break
            time.sleep(5)
        c.app_stop("com.apple.TestFlight")
        c.close()


def SH_049():
    return None