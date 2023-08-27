#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 17:07
# @Author  : Owen
# @File    : base_page.py
# @Software: PyCharm
import time

from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException

from appium_demo.base.exception_handle import app_exception_record


class BasePage():

    def __init__(self, driver=None):
        self.driver: WebDriver = driver

    # @app_exception_record
    def find(self, by):
        return self.driver.find_element(*by)

    # @app_exception_record
    def finds(self, by):
        return self.driver.find_elements(*by)

    def find_and_click(self, by):
        self.find(by).click()

    def find_send(self, value, by):
        self.find(by).send_keys(value)

    def find_and_displayed(self, by):
        return self.find(by).is_displayed()

    def set_implicitly_wait(self, time=1):
        """
        封装隐式等待
        :param time:
        :return:
        """
        self.driver.implicitly_wait(time)

    def get_tips(self, by):
        return self.find(by).text

    def do_sleep(self, seconds=1):
        time.sleep(seconds)

    def go_back(self, nums):
        for i in range(nums):
            self.driver.back()

    def swipe_find(self, by, max_num=3):
        """
        滑动查找一个文本
        如果没有找到元素，则滑动去查找，
        如果找到了，则返回该元素
        :param text:
        :param max_num:
        :return:
        """
        self.set_implicitly_wait()
        for num in range(max_num):
            try:
                element = self.find(by)
                self.set_implicitly_wait(self.IMPLICITLY_WAIT)
                return element
            except NoSuchElementException as e:
                print(f"元素未找到,原因  ===> {e}")
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")

                startx = width * 0.5
                starty = height * 0.8

                endx = startx
                endy = height * 0.2

                duration = 2000
                self.driver.swipe(startx, starty, endx, endy, duration)
        self.set_implicitly_wait(self.IMPLICITLY_WAIT)
        raise NoSuchElementException(f"使用 {by[0]} 定位方式进行{by[1]}的查找，找了{max_num}次并未找到")

    def get_cur_time(self):
        t = time.localtime(time.time())
        cur_time = time.strftime("%Y-%m-%d_%H%M%S", t)
        return cur_time

    def page_source(self):
        return self.driver.page_source

    def screenshot(self, filename):
        self.driver.save_screenshot(filename)
