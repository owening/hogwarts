#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：base_page
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 10:04 
'''
import time

from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, base_driver: WebDriver = None):
        self.driver = base_driver

    def find(self, by):
        return self.driver.find_element(*by)

    def find_and_send(self, by, text):
        return self.find(by).send_keys(text)

    def find_and_click(self, by):
        return self.find(by).click()

    def find_and_text(self, by):
        return self.find(by).text

    def find_and_displayed(self, by):
        return self.find(by).is_displayed()


    def do_sleep(self,seconds=1):
        time.sleep(seconds)

    def do_back(self):
        self.driver.back()

    def get_page_source(self):
        self.driver.page_source

    def by_keyword_find(self, by, keyword):
        """
        通过关键字定位信息定位元素
        示例： "//*[text() ='{}']/../../td/input".format(keywords)
        :param by:
        :param keywords:
        :return:
        """
        return self.do_find(by[0], by[1].format(keyword))