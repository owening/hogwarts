#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 14:39
# @Author  : Owen
# @File    : test_wework.py
# @Software: PyCharm
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


def swipe_exception(by: tuple, direction: str, timeout=10):
    """

    :param by: 元素定位方式和定位表达式 示例：(AppiumBy.XPATH, "//*[@text='添加成员']")
    :param direction: 滑动方向  "UP" , "DOWN"
    :param timeout: 超时时间
    :return:
    """

    def inner(driver):
        screen_width = driver.get_window_size()['width']
        screen_height = driver.get_window_size()['height']
        end_time = time.time() + timeout * 1000
        while True:
            try:
                if driver.find_element(*by):
                    # 找到元素后停止滑动,并return
                    return driver.find_element(*by)
            except NoSuchElementException as e:
                if time.time() > end_time:
                    raise (e("未找到元素"), TimeoutException("滑动查找元素超时了"))
            # 未找到元素，继续滑动
            if direction == "UP":
                driver.swipe(screen_width / 2, screen_height * 0.8, screen_width / 2, screen_height * 0.4)
            elif direction == "DOWN":
                driver.swipe(screen_width / 2, screen_height * 0.4, screen_width / 2, screen_height * 0.8)

    return inner

class TestWeWork:

    def setup(self):
        fake = Faker('zh_CN')
        self.name = fake.name()
        self.mobile = fake.phone_number()

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

    def teardown(self):
        self.driver.quit()


    def test_add_member(self):

        self.driver.find_element(AppiumBy.XPATH,"//*[@text='通讯录']").click()
        WebDriverWait(self.driver, 10).until(swipe_exception((AppiumBy.XPATH, "//*[@text='添加成员']"), "UP", 10))

        self.driver.find_element(AppiumBy.XPATH,"//*[@text='添加成员']").click()

        self.driver.find_element(AppiumBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(AppiumBy.XPATH,"//*[@text='姓名']/../*[@text='必填']").send_keys(self.name)
        self.driver.find_element(AppiumBy.XPATH,"//*[@text='+86']/../..//*[@text='必填']").send_keys(self.mobile)
        self.driver.find_element(AppiumBy.XPATH,"//*[@text='保存']").click()

        tips = self.driver.find_element(AppiumBy.XPATH,"//*[@text='添加成功']").text

        assert tips == "添加成功"


