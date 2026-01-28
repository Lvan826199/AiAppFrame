# -*- coding: utf-8 -*-
'''
@Time : 2022/9/14 10:54
@Author : Vincent.xiaozai
@Email : Lvan826199@163.com
@File : RunTestCase.py
'''
__author__ = "梦无矶小仔"

import unittest
from airtest.core.api import *
from TestCase import *
from unittestreport import TestRunner
import unittestreport
from datetime import datetime
from common.ParameterizedTestCase import ParameterizedTestCase

_print = print


def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)


# 运行Testcase
def RunTestCase(MD, start):
    ### 使用者可以根据自己的需求，将unittest框架更改为pytest框架，这个报告都兼容
    device_id = MD.get_mdevice()
    print("进入{}的RunTestCase".format(device_id))
    # 获取路径
    TestCasePath = MD.get_TestCasePath()
    if not os.path.exists(TestCasePath):
        print("测试用例需放到‘TestCase’文件目录下")
    reportpath = os.path.join(os.getcwd(), "Reports")
    # 读取ini文件，获得期望测试的用例(这里只做了一个文件，可以使用多个，以后再加)
    testCaseList = MD.get_testCaseWhichRun(device_id)
    print("{}的待测用例为：{}".format(MD.get_mdevice(), testCaseList))
    SpCaseFolderPath = MD.get_SpCaseFolder()
    SpCaseFolderName = str(SpCaseFolderPath).split('\\')[-1]
    print("文件夹名称:", SpCaseFolderName)

    # 没有测试用例，直接不出报告
    # 未对All选项的测试集进行适配，只适配了单个文件夹下的，如果不需要传参数进入TestCase，则可以不用适配（有生之年我可能会适配一下）
    if testCaseList:
        suite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(start_dir=SpCaseFolderPath)
        print("discover:", discover)
        for test_suite in discover:
            print("============================================================")
            print("test_suite._test:【", test_suite._tests)
            print("=============================================================")
            try:
                test_suite_py_name = str(test_suite._tests[0]).split('tests=[<')[1].split('.')[0].strip()
                test_class_name = str(test_suite._tests[0]).split('tests=[<')[1].split('.')[1].split(' ')[0].strip()
            except:
                try:
                    test_suite_py_name = str(test_suite._tests[1]).split('tests=[<')[1].split('.')[0].strip()
                    test_class_name = str(test_suite._tests[1]).split('tests=[<')[1].split('.')[1].split(' ')[0].strip()
                except:  # 过滤掉没有测试用例的case
                    continue
            print(f'得到的用例的文件为:{test_suite_py_name}')
            print(f'得到的用例的类名为:{test_class_name}')

            if test_suite_py_name in testCaseList:
                ##########################################
                # for test_case in test_suite:
                #     # suite.addTest(test_case)
                #     ...
                ######################################
                exec(f'from TestCase.{SpCaseFolderName}.{test_suite_py_name} import {test_class_name}')
                print(f'得到的用例的类名为:{test_class_name}')
                x = locals()
                suite.addTest(ParameterizedTestCase.parameterize(eval(x['test_class_name']), device_id=device_id))
                print("==========")
                print(suite)
                print("==========")

        if MD.get_nickname() == '4438650ca0ef0073a711ae68b7c5fdc629db9772':  # SH-SJ-0046
            reportName = 'SH-SJ-0046'
        elif MD.get_nickname() == 'f4865892438965021723a179972cab72807ce4de':  # SH-SJ-0098
            reportName = 'SH-SJ-0098'
        elif MD.get_nickname() == '00008101-001859DE1E38001E':  # SH-SJ-0123
            reportName = 'SH-SJ-0123'
        elif MD.get_nickname() == 'bba4ba579a9664eba4fc566ca6ef802ca36b71aa':  # SH-SJ-0163
            reportName = 'SH-SJ-0163'
        elif MD.get_nickname() == '00008110-000275943EEB801E':  # SH-SJ-0182
            reportName = 'SH-SJ-0182'
        elif MD.get_nickname() == 'cc6aecac0cbaf3e0a9aef1e8fcb848cd8292461b':  # BJ-SJ-0011
            reportName = 'BJ-SJ-0011'
        elif MD.get_nickname() == '00008030-001E19021A42802E':  # #SH-SJ-0186
            reportName = 'SH-SJ-0186'
        elif MD.get_nickname() == '27d62264ebf40fb3a9e4868590b62ff3b4de90ff':  # SH-SJ-0192
            reportName = 'SH-SJ-0192'
        elif MD.get_nickname() == '00008027-001968942140402E':  # SH-SJ-0100
            reportName = 'SH-SJ-0100'
        elif MD.get_nickname() == '49687f67a4c70fbd027e19b4a5e40218acdc06e4':  # SH-SJ-0067
            reportName = 'SH-SJ-0067'
        elif MD.get_nickname() == 'e455517036f9aabe3ceb7111a8eaf1c01d7de3f0':  # SH-SJ-0067
            reportName = 'SH-SJ-0049'
        else:
            reportName = MD.get_nickname()

        # nowtime = time.strftime("%Y-%m-%d_%H-%M-%S", start) # #原先的代码
        # unittestReport = BeautifulReport(suite) #原先的代码
        # unittestReport.report(filename=str(nowtime)+"_"+reportName,description=package, report_dir=reportpath) #原先的代码

        nowtime = time.strftime("%Y-%m-%d_%H-%M-%S", start)
        runner = TestRunner(suite, title=f'{reportName}测试报告', filename=f"{nowtime}_{reportName}.html", report_dir=reportpath, templates=2,
                            tester='梦无矶小仔')
        runner.run()
