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
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait


def sliding_find_element_wait(locator):
    """
    官方的 excepted_conditions 不可能覆盖所有场景
    定制封装条件会更加灵活、可控
    ### 显示等待高级用法，自定义结束条件
    自定义结束条件函数下写内函数实现
    """

    def inner(driver):
        screen_width = driver.get_window_size()['width']
        screen_height = driver.get_window_size()['height']
        print(screen_width, screen_height)
        while True:
            try:
                element = driver.find_element(*locator)
                # 找到元素后停止滑动
                return element
            except NoSuchElementException:
                # 未找到元素，继续滑动
                driver.swipe(screen_width / 2, screen_height * 0.8, screen_width / 2, screen_height * 0.2, 1000)

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
        # 打开企业微信，不清空用户信息
        self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addmember(self):
        # 进入到通讯录页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").is_displayed()

        #执行等待并查找元素
        WebDriverWait(self.driver, 10).until(sliding_find_element_wait((AppiumBy.XPATH, "//*[@text='添加成员']")))
        # 点击添加按钮跳转到添加成员页面。
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()

        # 点击手动输入添加
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入用户名、手机号
        self.driver.find_element(AppiumBy.ID, "com.tencent.wework:id/c4k").send_keys(self.name)
        self.driver.find_element(AppiumBy.ID, "com.tencent.wework:id/igg").send_keys(self.mobile)
        # 点击保存
        self.driver.find_element(AppiumBy.ID, "com.tencent.wework:id/b2s").click()
        # 多断言：
        # 所有的成员姓名是否包含添加时输入的姓名；
        # 所有的成员手机号是否包含添加时输入的手机号；
        self.driver.back()
        # eles = self.driver.find_elements(AppiumBy.ID, "com.tencent.wework:id/g60")
        # name_list = []
        # for ele in eles:
        #     print(ele.text)
        #     name_list.append(ele.text)
        #
        # print(f"所有成员姓名为：{name_list}")
        # # assert self.name in name_list
