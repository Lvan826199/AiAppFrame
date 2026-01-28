# -*- coding: utf-8 -*-
'''
@Time : 2023/7/4 13:59
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : case.py
'''
__author__ = "梦无矶小仔"


# from airtest.core.api import connect_device
from tidevice import Device
# from airtest.core.ios.ios import IOS
# from poco.drivers.ios import iosPoco
from airtest.core.ios.ios import wda
from myutils.login_apple_id.IOSAppOperate import *
from myutils.login_apple_id.control_settings import *
from airtest.core.api import *

def case_run(devices):
    # ios = IOS("http+usbmux://" + devices)
    c = wda.Client("http+usbmux://{udid}".format(udid=devices))
    # ios_poco = iosPoco(device=connect_device(f"iOS:///http+usbmux://{devices}"))
    user_pwd_game_dict = user_pwd_game()
    user = user_pwd_game_dict["user"]
    pwd = user_pwd_game_dict["pwd"]
    game = user_pwd_game_dict["game"]
    package_name = user_pwd_game_dict["package_name"]
    is_tf_install_app_flag = user_pwd_game_dict["is_tf_install_app_flag"]

    #########################   以下为ios设备
    #### SH-SJ-0046
    if devices == "4438650ca0ef0073a711ae68b7c5fdc629db9772":
        SH_046().check_acount(c, acount=user, pwd=pwd)
        if is_tf_install_app_flag:
            Device(devices).app_uninstall(package_name)
            SH_046().game_download(c, name=game)
            print(f"{game} 下载完毕！")
        print("--------------------------------046    账号登录完毕  安装完毕------------------------")

    ###########SH-SJ-0123
    elif devices == "00008101-001859DE1E38001E":
        SH_123().loginAppStore(c, acount=user, pwd=pwd)
        SH_123().check_acount_ios14(c, acount=user, pwd=pwd)
        if is_tf_install_app_flag:
            Device(devices).app_uninstall(package_name)
            SH_123().game_download(c,name=game)
            print(f"{game} 下载完毕！")
        print("--------------------------------123    账号登录完毕  安装完毕------------------------")

    #### SH-SJ-0182
    elif devices == "00008110-000275943EEB801E":
        SH_182().loginAppStore(c, acount=user, pwd=pwd)
        SH_182().check_acount_ios14(c, acount=user, pwd=pwd)
        if is_tf_install_app_flag:
            Device(devices).app_uninstall(package_name)
            SH_182().game_download(c,name=game)
            print(f"{game} 下载完毕！")
        print("--------------------------------182    账号登录完毕  安装完毕------------------------")

    #### SH-SJ-0186
    elif devices == "00008030-001E19021A42802E":
        SH_186().loginAppStore(c, acount=user, pwd=pwd)
        SH_186().check_acount_ios14(c, acount=user, pwd=pwd)
        if is_tf_install_app_flag:
            Device(devices).app_uninstall(package_name)
            SH_186().game_download(c,name=game)
            print(f"{game} 下载完毕！")
        print("--------------------------------186    账号登录完毕  安装完毕------------------------")

    #### SH-SJ-0192
    elif devices == "27d62264ebf40fb3a9e4868590b62ff3b4de90ff":
        SH_192().check_acount(c, acount=user, pwd=pwd)
        if is_tf_install_app_flag:
            Device(devices).app_uninstall(package_name)
            SH_192().game_download(c,name=game)
            print(f"{game} 下载完毕！")
        print("--------------------------------192    账号登录完毕  安装完毕------------------------")

    #### SH-SJ-0100
    elif devices == "00008027-001968942140402E":
        SH_100().loginAppStore(c, acount=user, pwd=pwd)
        SH_100().check_acount_ios14(c, acount=user, pwd=pwd)
        if is_tf_install_app_flag:
            Device(devices).app_uninstall(package_name)
            SH_100().game_download(c,name=game)
            print(f"{game} 下载完毕！")
        print("--------------------------------100    账号登录完毕  安装完毕------------------------")

    #### SH-SJ-0067
    elif devices == "49687f67a4c70fbd027e19b4a5e40218acdc06e4":
        SH_067().loginAppStore(c, acount=user, pwd=pwd)
        SH_067().check_acount_ios14(c, acount=user, pwd=pwd)
        if is_tf_install_app_flag:
            Device(devices).app_uninstall(package_name)
            SH_067().game_download(c,name=game)
            print(f"{game} 下载完毕！")
        print("--------------------------------067    账号登录完毕  安装完毕------------------------")

if __name__ == '__main__':
    case_run("00008101-001859DE1E38001E")