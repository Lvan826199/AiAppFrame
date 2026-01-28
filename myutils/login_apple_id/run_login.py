# -*- coding: utf-8 -*-
'''
@Time : 2023/7/4 10:51
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : run_login.py
'''
__author__ = "梦无矶小仔"

# 使用进程进行登录

from multiprocessing import Process
from poco.exceptions import *
import traceback
from myutils.readConfig import *
from airtest.core.error import *
from myutils.login_apple_id.case import *

index_print = print


def print(*args, **kwargs):
    index_print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)


class MultiDevices():
    def __init__(self, mdevice=""):
        # 获取当前文件的上层路径
        self.parentPath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())) + os.path.sep + ".")
        # 获取当前项目的根路径
        self.rootPath = os.path.abspath(os.path.dirname(self.parentPath) + os.path.sep + ".")
        self._mdevice = mdevice
        # 处理模拟器端口用的冒号
        if ":" in self._mdevice:
            self._nickName = self._mdevice.split(":")[1]
        else:
            self._nickName = self._mdevice

    # 本方法用于读取实时的设备连接
    def getdevices(self):
        ios_list = []
        try:
            from tidevice import Usbmux
            ios = Usbmux().device_udid_list()
            for i in ios:
                ios_list.append(i)
                print("已添加：苹果设备 - {}".format(i))
        except:
            print("IOS设备未连接，请重新连接！")
        deviceslist = ios_list
        return deviceslist

    # 获取当前设备id
    def get_mdevice(self):
        return self._mdevice

    # 获取当前设备id的昵称，主要是为了防范模拟器和远程设备带来的冒号问题。windows的文件命名规范里不允许有冒号。
    def get_nickname(self):
        return self._nickName

    # 修改当前设备的方法
    def set_mdevice(self, device):
        self._mdevice = device


    # 获取测试用例路径，不填是默认根目录TestCase
    def get_TestCasePath(self):
        testCasePath = os.path.join(self.rootPath, "TestCase")
        return testCasePath

    # 获取针对特定设备的用例列表
    def get_testCaseWhichRun(self, device):
        device = str(device).lower()  # 该死的config库使用option提取会变小写
        try:
            testCase = getAllTestCase()[device]
            testCaseList = testCase.split(',')
        except KeyError:
            testCaseList = []
        return testCaseList

    # 获取用例的指定文件夹
    def get_SpCaseFolder(self):
        # 获取TestCase下的文件夹
        TestCasePath = f'{self.rootPath}\\TestCase'
        ChildFolderList = []
        for root, dirs, files in os.walk(TestCasePath, topdown=False):
            ChildFolderList.append(root)
        getSpCaseFolderList = getSpCaseFolder()
        if len(getSpCaseFolderList) == 1 and getSpCaseFolderList[0]:
            if getSpCaseFolderList[0] == 'all':
                return TestCasePath
            else:
                for ChildFolder in ChildFolderList:
                    folderName = ChildFolder.split('\\')[-1].lower()
                    if getSpCaseFolderList[0] == folderName:
                        return ChildFolder
                else:
                    print(f"请在TestCase文件夹中添加【{getSpCaseFolderList[0]}】文件夹及用例！")
                    return None
        else:
            print('TestCaseSpFolder中的选项只能有一个为1')
            return None

def isRunDevices():
    isRundevicesList = []
    for key,value in devices_dict.items():
        if value == 1:
            isRundevicesList.append(key)

    return  isRundevicesList


def main():
    allDevicesList = MultiDevices().getdevices()

    print(f'当前所连接的设备列表:{allDevicesList}')
    isRundevicesList = isRunDevices()
    print('当前标记的设备列表：', isRundevicesList)
    # 判定配置表里面TestCase下的设备是否在线
    for device in isRundevicesList:
        if device.lower() not in [x.lower() for x in allDevicesList]:
            print(f'\033[31m{device}设备不在线，可能未开启WebDriverAgent服务，请在tools文件夹下启动start_ios_devices或检查设备是否配置好相关环境!\033[0m')

    # 只有在TestCase配置项下配置了,并且在线的设备才会进行运行
    d = dict(zip(range(len(allDevicesList)), allDevicesList))
    for k, v in d.items():
        if v not in isRundevicesList:
            d[k] = []
    finalDevicesList = [v for k, v in d.items() if v]
    print('等待跑用例的设备列表:', finalDevicesList)
    if finalDevicesList:
        try:
            print("启动进程池")
            pool_list = []
            # 根据设备列表去循环创建进程，对每个进程调用enter_processing 方法
            for i in range(len(finalDevicesList)):
                start = time.localtime()
                MD = MultiDevices(finalDevicesList[i])
                pools = Process(target=enter_processing, args=(i, MD, start,))
                pool_list.append(pools)
            print("---------------------------------------------")
            print(f"当前线程池列表：{pool_list}")
            print("---------------------------------------------")
            for pool in pool_list:
                pool.start()
            for pool in pool_list:
                pool.join()
            print("进程回收完毕")
            print("测试结束")
        except AirtestError as ae:
            print(f"Airtest发生错误:{ae}")
        except PocoException as pe:
            print(f"Poco发生错误:{pe}")
        except Exception as e:
            print(f"发生未知错误:{e}")
    else:
        print("未找到设备，测试结束")


from airtest.cli.parser import cli_setup



def enter_processing(processNo, MD, start):
    devices = MD.get_mdevice()  # 获取当前连接的设备名字
    print("进入第{}个进程,devicename={}".format(processNo, devices))
    try:
        startflag = "Success"
        # 调用airtest的各个方法连接设备 以下为示例（不同的设备有些连接方式是不能互通的，具体的根据自己的实际情况进行选择）
        ####### 以下为Android设备  ##########
        if devices == "HA0Y7AUR":
            if not cli_setup():
                auto_setup(__file__, logdir=True, devices=["Android://127.0.0.1:5037/HA0Y7AUR", ])
        elif devices == "66J5T18A28047220":
            connect_device("Android:///" + devices)
        elif devices == "04157df4d5a71515":
            connect_device("Android:///" + devices + "?touch_method=ADBTOUCH")
        elif devices == "R28M405TJBX":
            connect_device("Android:///" + devices + "?cap_method=JAVACAP")
        elif devices == "2684c2b0":
            connect_device("Android:///" + devices + "?cap_method=JAVACAP&&touch_method=ADBTOUCH")

        #########################   以下为ios设备
        #### SH-SJ-0046
        elif devices == "4438650ca0ef0073a711ae68b7c5fdc629db9772":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://4438650ca0ef0073a711ae68b7c5fdc629db9772", ])
        #### SH-SJ-0098
        elif devices == "f4865892438965021723a179972cab72807ce4de":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://f4865892438965021723a179972cab72807ce4de", ])

        ###########SH-SJ-0123
        elif devices == "00008101-001859DE1E38001E":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://00008101-001859DE1E38001E", ])
        #### SH-SJ-0163
        elif devices == "bba4ba579a9664eba4fc566ca6ef802ca36b71aa":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://bba4ba579a9664eba4fc566ca6ef802ca36b71aa", ])
        #### SH-SJ-0182
        elif devices == "00008110-000275943EEB801E":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://00008110-000275943EEB801E", ])
        #### SH-SJ-0011
        elif devices == "cc6aecac0cbaf3e0a9aef1e8fcb848cd8292461b":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://cc6aecac0cbaf3e0a9aef1e8fcb848cd8292461b", ])
        #### SH-SJ-0186
        elif devices == "00008030-001E19021A42802E":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://00008030-001E19021A42802E", ])
        #### SH-SJ-0192
        elif devices == "27d62264ebf40fb3a9e4868590b62ff3b4de90ff":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://27d62264ebf40fb3a9e4868590b62ff3b4de90ff", ])
        #### SH-SJ-0100
        elif devices == "00008027-001968942140402E":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://00008027-001968942140402E", ])
        #### SH-SJ-0067
        elif devices == "49687f67a4c70fbd027e19b4a5e40218acdc06e4":
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["ios:///http+usbmux://49687f67a4c70fbd027e19b4a5e40218acdc06e4", ])
        else:
            print(f'{devices}未做处理，请在index文件下添加该设备！')
            startflag = "Fail"

        time.sleep(15)
        auto_setup(__file__)
        print("设备{}连接成功".format(devices))

        # 应用启动成功则开始运行用例
        if (startflag == "Success"):
            case_run(devices=devices)
            print("{}完成测试".format(devices))
        else:
            print("{}未运行测试。".format(devices))
    except Exception as e:
        print("连接设备{}失败".format(devices) + traceback.format_exc())
