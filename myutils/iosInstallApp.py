# -*- coding: utf-8 -*-
'''
@Time : 2023/1/4 10:35
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : iosInstallApp.py
'''
__author__ = "梦无矶小仔"

import os
import time
from airtest.core.api import *
from airtest.core.ios.ios import IOS, wda

devicesDict = {
    "SH-SJ-0046": "4438650ca0ef0073a711ae68b7c5fdc629db9772",
    "SH-SJ-0192": "27d62264ebf40fb3a9e4868590b62ff3b4de90ff",
    "SH-SJ-0049": "e455517036f9aabe3ceb7111a8eaf1c01d7de3f0",
    "SH-SJ-0123": "00008101-001859DE1E38001E",
    "SH-SJ-0182": "00008110-000275943EEB801E",
    "SH-SJ-0186": "00008030-001E19021A42802E",
    "SH-SJ-0100": "00008027-001968942140402E",
    "SH-SJ-0067": "49687f67a4c70fbd027e19b4a5e40218acdc06e4",
    # "SH-SJ-0190": "00008110-000629481145801E",
    # "SH-SJ-0163": "bba4ba579a9664eba4fc566ca6ef802ca36b71aa",
    # "SH-SJ-0019": "3af3b86fbcb03876b89cf55ca4b364c0fd7635c2",
    # "SH-SJ-0092": "ca10b9d68c0f34a1f172cf07d80fc5706aefe275",
    # "SH-SJ-0098": "f4865892438965021723a179972cab72807ce4de",
    # "SH-SJ-0184": "00008110-00067CCA1487801E",
}
# ipaPath = ''
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\\BingoIsland\\9.0.1602_发行测试服_22_dev.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\BingoParty\\BingoParty-AdHoc.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\whispers章节包\\Whispers-2.2.8-AdHocRelease.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\whispers.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\MatchScapes\\Development_MatchTileScenery_1.38.0_119_1119_IOS.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\WeedMania\\WeedMania_Debug.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\NorthTower.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\LuckyHit\LuckyHitSlots(2).ipa"
# ipaPath =r"D:\Y_PythonProject\AiAppFrame\myutils\apk\PW\AstroHero.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\纯白\SGame25121201(AD)_Publish(47).ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\DoubleWin\DoubleWin(2).ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\CashHoard\CashHoard_lucky_d3013.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\Hugwin\Trojan_3.50.0_1354_Release.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\WDA\iOS18-WDA.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\广告SDK\MSSDK-Admob-4.2.0.3.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\广告SDK\MSSDK-Ironsource-4.2.0.3.ipa"
# ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\广告SDK\MSSDK-Max-4.2.0.3.ipa"
ipaPath = r"D:\Y_PythonProject\AiAppFrame\myutils\apk\ASMR\asmr_202512301544_ios_debug_adhoc.ipa"

#

###
ipaPackageNameDict = {
    # "ipaPackageName1": "com.bingo.tour.party.crazy.free.ios.avidly",  # BingoParty
    # "ipaPackageName2":"com.bingo.scape.ios.free", #BingoJourney
    # "ipaPackageName3":"com.huge.slots.casino.vegas.ios.avidly", #Double Win
    # "ipaPackageName4":"com.twincat.stories", #Whispers
    # "ipaPackageName5":"com.grandcashslots.free.ios", #Grand Cash Slots
    # "ipaPackageName6": "com.bingo.island.ios",  # BingoIsland
    # "ipaPackageName7":"com.strategy.north.tower.ios", # NorthTower
    # "ipaPackageName8": "com.puzzle.matchscapes.apple",  # Match Tile Scenery
    # "ipaPackageName9":"com.bravo.slots.casino.ios", #Lucky Hit Classic Slots
    # "ipaPackageName10":"com.golden.fishing.ios.avidly", #黄金捕鱼
    # "ipaPackageName11":"com.newclassic.doublerich", #DoubleRich
    # "ipaPackageName12":"com.jackpot.fever.slots.ios", #CashHoard
    # "ipaPackageName13":"com.cjfafafa.trojan.ios", #HugeWin
    # "ipaPackageName14":"com.harvest.ios.grq", #奶牛
    # "ipaPackageName15":"com.anotherworld.ios", #福州卡牌
    # "ipaPackageName16": "com.yulong.sgame.ios",  # 纯白大作战
    # "ipaPackageName17" : "com.sfgh.weedmania.ios", # WeedMania
    # "ipaPackageName18" : "com.zymobile.match.tile.decor.ios" # MatchTileDecor
    "ipaPackageName19" : "com.zhgh.cannabis.weed.please.gp" # Weed inc 420
    # "ipaPackageName19" : "com.upltv.mssdk" # MSSDK
    # "ipaPackageName19" : "com.puzzle.satisgame2" # AMSR
}
ipaPackageNameList = [i for i in ipaPackageNameDict.values()]
print(ipaPackageNameList)
# 是否安装 0 表示不安装只卸载， 1 表示安装
isInstallApk = 1

for ipaPackageName in ipaPackageNameList:
    # 先卸载
    for name, device in devicesDict.items():
        # 指定设备卸载
        # $ tidevice --udid $UDID uninstall https://example.org/example.ipa
        try:
            # # 先停止应用再卸载8
            print(f"当前卸载 -- {name}")
            # os.system(f"tidevice --udid {device} kill {ipaPackageName}")
            # time.sleep(1)
            # try:
            #     dev = connect_device(f"iOS:///http+usbmux://{device}")
            #     c = wda.Client("http+usbmux://{udid}".format(udid=device))
            #     c.home()
            # except:
            #     pass

            os.system(f"tidevice --udid {device} uninstall {ipaPackageName}")
        except Exception as e:
            print("失败.......", e, f"当前卸载 -- {name} ")

    if not isInstallApk:
        print(f"isInstallApk为0,不进行安装，{ipaPackageName} - 全部卸载完毕")

    if isInstallApk:
        print("全部卸载完成......进行安装.....")
        # 再安装
        for name, device in devicesDict.items():
            # 指定设备安装
            # $ tidevice --udid $UDID install https://example.org/example.ipa
            try:
                print(f"当前安装 -- {name}")
                os.system(f"tidevice --udid {device} install {ipaPath}")
            except Exception as e:
                print("失败.......", e, f"当前安装 -- {name} ")

        print("全部安装完成......")

#
