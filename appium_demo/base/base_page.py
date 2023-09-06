#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 17:07
# @Author  : Owen
# @File    : base_page.py
# @Software: PyCharm
import time

import allure
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException

from appium_demo.base.exception_handle import app_exception_record
from appium_demo.utils.data_util import DataUtil
from appium_demo.utils.error_handle import black_wrapper
from appium_demo.utils.log_util import logger


class BasePage():
    IMPLICITLY_WAIT = 10

    def __init__(self, driver=None):
        self.driver: WebDriver = driver

    @black_wrapper
    def find(self, by):
        step_text = f"使用 {by[0]} 的定位方式进行 {by[1]} 的定位操作"
        logger.info(step_text)
        with allure.step(step_text):
            return self.driver.find_element(*by)

    @black_wrapper
    def finds(self, by):
        step_text = f"使用 {by[0]} 的定位方式进行 {by[1]} 的定位操作"
        logger.info(step_text)
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

    def quit(self):
        self.driver.quit()

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
        filename = DataUtil.save_source_datas("pagesource")
        # 写 page source 文件
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        logger.info(f"源码保存的路径为{filename}")
        # 返回 page source 保存路径
        return filename

    def screenshot(self):
        """
        截图
        """
        filename = DataUtil.save_source_datas("images")
        self.driver.save_screenshot(filename)
        logger.info(f"截图保存的路径为{filename}")
        return filename
