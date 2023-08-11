#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 16:51
# @Author  : Owen
# @File    : base_page.py
# @Software: PyCharm
import time

from selenium import webdriver


class BasePage:
    _BASE_URL = ""

    def __init__(self, base_driver=None):

        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

        # if not self.driver.current_url.startswith("http"):
        #     self.driver.get(self._BASE_URL)

    def do_find(self, by, locator=None):
        """
         查找获取单个元素
        :param by:
        :return: 单个元素对象
        """
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        """
        查找获取多个元素
        :param by:
        :return: 多个元素对象列表
        """
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_by_keyword_find(self, by, keywords):
        """
        通过关键字定位信息定位元素
        示例： '//*[text() =\'{}\']/../../td/input'.format(keywords)
        :param by:
        :param keywords:
        :return:
        """
        return self.driver.find_element(by[0], by[1].format(keywords))

    def do_click(self, by):
        """
        点击
        :param by:
        :return:
        """
        self.do_find(by).click()

    def do_sendkeys(self, by, value):
        """
        输入数据
        :param by:
        :param value:
        :return:
        """
        el = self.do_find(by)
        el.clear()
        el.send_keys(value)

    def do_quit(self):
        self.driver.quit()

    def do_screenshot(self, filename):
        """
        截图
        :param filename:
        :return:
        """
        self.driver.save_screenshot(filename)

    def do_sleep(self, seconds=1):
        time.sleep(seconds)

