#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：opencv_demo
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/8 18:00 
'''
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestImage:
    def setup_class(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_image(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Graphics').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'BitmapMesh').click()
        self.driver.find_element(AppiumBy.IMAGE, "nose.png").click()
        self.driver.find_element(AppiumBy.IMAGE, "flower.png").click()
        # self.driver.find_element_by_image("nose.png").click()
        # self.driver.find_element_by_image("flower.png").click()