# -*- coding: utf-8 -*-
"""
@Time : 2024/9/13 17:57
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : connect_ios17_or_higher.py
"""
__author__ = "梦无矶小仔"


import os
import subprocess
import time
from airtest.core.api import connect_device, device, sleep, auto_setup, click, text
from poco.drivers.ios import iosPoco


class IOS17HigherAutomation:
    def __init__(self, wda_package_name, uuid, wda_ipa_path, log_dir='./ios'):
        self.wda_package_name = wda_package_name
        self.uuid = uuid
        self.wda_ipa_path = wda_ipa_path
        self.log_dir = log_dir
        self.device = None
        self.poco = None
        self.width = None
        self.height = None

    def install_wda(self):
        os.system(self.wda_ipa_path)
        time.sleep(6)

    def run_wda(self):
        run_wda_command = [
            'ios', 'runwda',
            f'--bundleid={self.wda_package_name}',
            f'--testrunnerbundleid={self.wda_package_name}',
            '--xctestconfig=WebDriverAgentRunner.xctest'
        ]
        subprocess.Popen(run_wda_command)
        time.sleep(6)

    def connect_device(self):
        self.device = connect_device(f"ios:///http+usbmux://{self.uuid}")
        self.poco = iosPoco(device=self.device)
        dev = device()
        self.width, self.height = dev.get_current_resolution()
        auto_setup(logdir=self.log_dir, compress=3, devices=[f"ios:///http+usbmux://{self.uuid}"])
        sleep(6)

    def start_recording(self, fps=4, orientation=1):
        self.device.start_recording(fps=fps, orientation=orientation)

    def stop_recording(self):
        self.device.stop_recording()

    def start_app(self, app_package_name):
        # # you need to kill the app firstly, and then start the app
        # otherwith it would fail to open the app after you open the app more than 188 times
        self._kill_app(app_package_name)
        self._launch_app(app_package_name)

    def _kill_app(self, app_package_name):
        kill_app_command = ['ios', 'kill', app_package_name]
        subprocess.run(kill_app_command, check=True)

    def _launch_app(self, app_package_name):
        launch_app_command = ['ios', 'launch', app_package_name]
        subprocess.run(launch_app_command, check=True)

    def search_in_app_store(self, search_text):
        self.poco(nameMatches=".*search").click()
        self.poco(nameMatches="AppStore.searchField").click()
        text(search_text)
        click([self.width * 0.5, self.height * 0.5])

    def uninstall_wda(self):
        os.system(f'tidevice uninstall {self.wda_package_name}')


def main():
    WDA_PACKAGE_NAME = 'xxx'
    UUID = 'xxx'
    # WDA_IPA_PATH = r'tidevice install C:\xxx\xxxx\xxxx\xxxxx\xxxxx\wda.ipa'
    WDA_IPA_PATH = r'ios install C:\xxx\xxxx\xxxx\xxxxx\xxxxx\wda.ipa'

    ios_automation = IOS17HigherAutomation(WDA_PACKAGE_NAME, UUID, WDA_IPA_PATH)

    ios_automation.install_wda()
    ios_automation.run_wda()
    ios_automation.connect_device()
    ios_automation.start_recording()

    ios_automation.start_app("com.apple.AppStore")
    ios_automation.search_in_app_store("微信")

    ios_automation.stop_recording()
    ios_automation.uninstall_wda()


if __name__ == "__main__":
    main()
