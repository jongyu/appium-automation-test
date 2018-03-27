# coding=utf-8
import time

import os
from appium import webdriver
from util.write_user_command import WriteUserCommand

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseDriver:

    def __init__(self):
        pass

    @staticmethod
    def android_driver(i):
        print "this is android_driver:", i
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        capabilities = {
            "platformName": "Android",
            "deviceName": devices,
            "app": PATH("../../apps/yhjs-debug-3.3.0-android_yingyong_market.apk"),
            "noReset": False,
            "appPackage": "com.kingkr.kuhtnwi",
            "appWaitActivity": ".ui.main.MainActivity",
        }
        driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
        time.sleep(10)
        return driver
