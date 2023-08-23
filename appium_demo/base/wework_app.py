#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 16:32
# @Author  : Owen
# @File    : wework_app.py
# @Software: PyCharm
from appium import webdriver

from appium_demo.base.base_page import BasePage


class WeWorkApp(BasePage):

    def star(self):
        caps = {}
        caps["platformName"] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps["noReset"] = "true"
        # 打开企业微信
        self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        return self

    def goto_main(self):

        from appium_demo.pages.main_page import MainPage
        return MainPage(self.driver)