import os
import signal
import subprocess
import threading
import time
import socket
from multiprocessing import Process
import psutil

# from utils.Gdevice import GetDevice
import queue

def get_ios():
    """由于tidevice 升级的原因，导致获取设备的方法 可以用 tidevice list 再提取处理"""
    ios_list = []
    try:
        from tidevice import Usbmux
        ios = Usbmux().device_list()
        for io in ios:
            # print(io.udid)
            ios_list.append(io.udid)
            # ios_list.append(io['SerialNumber'])
            # print("苹果设备{}被添加到deviceslist中".format(i['SerialNumber']))
        return ios_list
    except:
        print("IOS设备未连接，请检查数据线或者爱思助手")
        return ios_list

class IOSconnent:
    def __init__(self):

        self.queue = queue.Queue()
        self.devices = []
    def find_free_port(self):
        """
        获取随机可用的端口
        :return: 端口
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))  # 绑定到本地主机的随机端口
        _, port = sock.getsockname()  # 获取分配的端口号
        sock.close()
        return port


    def detection(self):

        while 1:
            try:
                # self.queue.put(1111)
                time.sleep(2)
                # ios = set(GetDevice.get_ios())
                ios = set(get_ios())
                # print(ios)
                """找出ios不在devices存储的元素"""
                res = ios - set(self.devices)
                if res:
                    print("检测到新增苹果设备",res)
                for io in res:
                    ##对新增设备进行服务启动
                    # os.popen("tidevice --udid {} xctest -B com.facebook.WebDriverAgentRunnerxzz.xctrunner -e USB_PORT:{}".format(io,self.find_free_port()))
                    subprocess.Popen("tidevice --udid {} xctest -B com.facebook.WebDriverAgentRunnerxzz.xctrunner -e USB_PORT:{}".format(io,self.find_free_port()))
                self.devices = self.devices+list(res)
                """找出devices本地存储不在ios的元素
                  当断线的时候，可以对比出哪个设备不在
                """
                res = set(self.devices) - ios
                if res:
                    print("检测到断线苹果设备",res)
                for io in res:
                    self.devices.remove(io)
                # print("目前在线苹果设备",self.devices)
            except Exception as e:
                print("有设备断开",e)


    def start(self):

        threading.Thread(target=self.detection).start()
        # Process(target=self.detection).start()

def iosserver():
    try:
        current_pid = os.getpid()
        signal.signal(signal.SIGINT, lambda signum, frame: stop_ios_server(signum, frame, current_pid))
        threading.Thread(target=IOSconnent().detection).start()
        # threading.Thread(target=IOSconnent().start).start()
        while True:
            pass
            time.sleep(1)
    except KeyboardInterrupt as e:
        pass

def stop_ios_server(signum, frame,pid):
    print("Stopping ios server...")
    broker_pid = psutil.Process(pid)
    broker_pid.terminate()



if __name__ == '__main__':
    # IOSconnent().start()
    # test()
    iosserver()


    # 寻找可用的闲置端口
    # port = find_free_port()
    # print(f"Free port found: {port}")
    # set1 = {1, 2, 3, 4, 5}
    # set2 = {3, 4, 5, 6, 7}
    #
    # # 找出在set1中而不在set2中的元素
    # result = set1 - set2
    # print(result)
    # result = set2 - set1
    # print(result)
