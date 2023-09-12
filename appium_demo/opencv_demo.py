#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：opencv_demo
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/8 18:00 
'''
import base64

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
        desired_caps['settings[fixImageFindScreenshotDims]'] = "false"
        desired_caps['settings[fixImageTemplateSize]'] = "true"
        desired_caps['settings[getMatchedImageResult]'] = "true"
        desired_caps['settings[imageMatchThreshold]'] = 0.4

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

        # 读取图片文件
        with open("nose.png", "rb") as image_file: self.nose_image = base64.b64encode(image_file.read())
        with open("flower.png", "rb") as image_file: self.flower_image = base64.b64encode(image_file.read())



    def test_image(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Graphics').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'BitmapMesh').click()
        # print(f"图片：{type(self.nose_image)},\n {self.flower_image}")
        self.driver.find_element(AppiumBy.IMAGE, str(self.nose_image)).click()
        self.driver.find_element(AppiumBy.IMAGE, str(self.flower_image)).click()


