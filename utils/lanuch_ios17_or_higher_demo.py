# -*- coding: utf-8 -*-
"""
@Time : 2024/9/13 17:57
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : lanuch_ios17_or_higher.py
"""
__author__ = "梦无矶小仔"

import os
import subprocess
import time
from airtest.core.api import connect_device, device, sleep, auto_setup, click, text
from poco.drivers.ios import iosPoco

WDA_Package_Name = 'xxx'
uuid = 'xxx'
WDA_ipa_path = r'tidevice install C:\xxx\xxxx\xxxx\xxxxx\xxxxx\wda.ipa'

def new_start_app_for_ios_17_and_18(appPackageName):
    kill_app_command = ['ios', 'kill',appPackageName]
    launch_app_command = ['ios', 'launch',appPackageName]
    # you need to kill the app firstly, and then start the app, otherwith it would fail to open the app after you open the app more than 188 times
    subprocess.run(kill_app_command, check=True)
    subprocess.run(launch_app_command, check=True)

os.system(WDA_ipa_path)
time.sleep(6)

run_wda_command = [
    'ios', 'runwda',
    f'--bundleid={WDA_Package_Name}',
    f'--testrunnerbundleid={WDA_Package_Name}',
    '--xctestconfig=WebDriverAgentRunner.xctest'
]
subprocess.Popen(run_wda_command)

time.sleep(6)


Bonding = connect_device("ios:///http+usbmux://"+uuid)
poco = iosPoco(device= Bonding)
dev = device()
width, height = dev.get_current_resolution()

auto_setup(logdir='./ios', compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
sleep(6)
Bonding.start_recording(fps=4,orientation=1)


new_start_app_for_ios_17_and_18("com.apple.AppStore")

poco(nameMatches=".*search").click()
poco(nameMatches="AppStore.searchField").click()
text("微信")
click([width*0.5,height*0.5])

Bonding.stop_recording()

os.system(f'tidevice uninstall {WDA_Package_Name}')