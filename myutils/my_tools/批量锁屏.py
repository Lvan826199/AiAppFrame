# -*- coding: utf-8 -*-
"""
@Time : 2023/10/18 15:09
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 批量锁屏.py
"""
__author__ = "梦无矶小仔"

import re
import time

from airtest.core.api import *
from airtest.core.ios.ios import IOS, wda
import tidevice

# 获取所有连接设备的信息
device_list = tidevice.Usbmux().device_list()

# 将所有的设备udid加入一个列表里面
device_udid_list = []
for device in device_list:
    device_udid_list.append(device.udid)


### 批量解锁
def unlock_device():
    for device_udid in device_udid_list:
        print(device_udid)
        try:
            dev = connect_device(f"iOS:///http+usbmux://{device_udid}")
            c = wda.Client("http+usbmux://{udid}".format(udid=device_udid))

            # 判断屏幕是否锁定,锁定为True,未锁定为False
            if c.locked():
                # 如果锁定了,则解锁
                try:
                    c.unlock()
                except:
                    pass
                print(f"{device_udid}屏幕已解锁")
            else:
                print((f"{device_udid}屏幕原本就是解锁状态"))
        except:
            print(f"{device_udid},设备WDA服务未启动...")


### 批量锁屏
def lock_device():
    for device_udid in device_udid_list:
        print(device_udid)
        try:
            dev = connect_device(f"iOS:///http+usbmux://{device_udid}")
            c = wda.Client("http+usbmux://{udid}".format(udid=device_udid))
            # 判断屏幕是否锁定,锁定为True,未锁定为False
            if not c.locked():
                # 如果锁定了,则解锁
                try:
                    c.lock()
                except:
                    pass
                print(f"{device_udid}屏幕已锁屏")
            else:
                print((f"{device_udid}屏幕原本就是锁屏状态"))
        except:
            print(f"{device_udid},设备WDA服务未启动...")

# # pip install moviepy
# import os
# from moviepy.editor import VideoFileClip
#
#
# def print_video_length(path, depth):
#     for foldername, subfolders, filenames in os.walk(path):
#         # 控制路径遍历深度，如果超过深度，则忽略此次遍历
#         if abs(foldername.count(os.sep) - os.getcwd().count(os.sep)) > depth: continue
#         if "项目视频" in foldername:
#             for filename in filenames:
#                 if filename.endswith('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'):
#                     video_path = os.path.join(foldername, filename)
#                     clip = VideoFileClip(video_path)
#                     seconds = clip.duration  # 视频多少秒
#                     # 把秒修改为小时分钟秒格式
#                     minutes, seconds = divmod(seconds, 60)
#                     hours, minutes = divmod(minutes, 60)
#                     # print(f"文件名: 【{video_path}】,时长:{int(hours)}小时{int(minutes)}分钟{int(seconds)}秒")
#                     print(f"文件名: 【{video_path.split('：', 1)[1]}】,时长:{int(hours)}小时{int(minutes)}分钟{int(seconds)}秒")


def isValid(s):
    stack = []  # 假设栈
    mapping = {")": "(", "}": "{", "]": "["}  # 括号映射才
    for char in s:
        if char in mapping:  # 如果当前字符是右括号
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:  # 如果此右括号与栈顶元素不匹配，返回无效
                return False
        else:
            stack.append(char)  # 如果它是一个左括号，将其推入栈
    return not stack  # 如果栈仍然包含元素，则说明未关闭的左括号，因此返回无效。否则返回有效


#

if __name__ == '__main__':
    # print_video_length(r'D:\L_Learning\测开课程\狂神\3-项目实战 - GVA后台项目管理开发', 4)
    # print(isValid("(){}[]()"))
    ## 批量解锁
    # unlock_device()
    ## 批量锁屏
    lock_device()
