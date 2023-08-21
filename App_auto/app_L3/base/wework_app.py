#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：wework_app
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 10:04 
'''
from appium import webdriver

from App_auto.app_L3.base.base_page import BasePage



class WeWorkApp(BasePage):

    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = 'emulator-5554'
            caps['automationName'] = 'UiAutomator2'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = '.launch.LaunchSplashActivity'
            caps["noReset"] = "true"
            # 打开企业微信
            self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_mainpage(self):
        from App_auto.app_L3.pages.main_page import MainPage
        return MainPage(self.driver)
