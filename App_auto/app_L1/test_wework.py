#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_wework
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/15 16:03 
'''
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


def swipe_find_element_wait(locator, direction, timeout=10):
    def inner(driver):
        screen_width = driver.get_window_size()['width']
        screen_height = driver.get_window_size()['height']
        end_time = time.time() + timeout * 1000
        while True:
            try:
                element = driver.find_element(*locator)
                if element.is_displayed():
                    # 找到元素可见后停止滑动,并return
                    return element
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
        #初始化构造测试数据
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
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addmember(self):
        # 进入到通讯录页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").is_displayed()

        # 执行等待并查找元素
        WebDriverWait(self.driver, 10).until(swipe_find_element_wait((AppiumBy.XPATH, "//*[@text='添加成员']"), "UP", 10))
        # 点击添加按钮跳转到添加成员页面。
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()

        # 点击手动输入添加
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入用户名、手机号
        self.driver.find_element(AppiumBy.ID, "com.tencent.wework:id/c4k").send_keys(self.name)
        self.driver.find_element(AppiumBy.ID, "com.tencent.wework:id/igg").send_keys(self.mobile)
        # 点击保存
        self.driver.find_element(AppiumBy.ID, "com.tencent.wework:id/b2s").click()
        # 返回通讯录页面,获取添加的成员信息
        time.sleep(1)
        self.driver.back()
        WebDriverWait(self.driver, 10).until(
            swipe_find_element_wait((AppiumBy.XPATH, f"//*[@text='{self.name}']"), "DOWN", 10))
        result_str = self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{self.name}']").text

        # 断言所有的成员姓名是否包含添加时输入的姓名；
        assert result_str == self.name
