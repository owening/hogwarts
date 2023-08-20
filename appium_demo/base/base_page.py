#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 17:07
# @Author  : Owen
# @File    : base_page.py
# @Software: PyCharm
from appium.webdriver.webdriver import WebDriver


class BasePage():

    def __init__(self,driver=None):
        self.driver = driver

    def find(self,by):
        return self.driver.find_element(*by)

    def finds(self, by):
        return self.driver.find_elements(*by)

    def find_click(self,by):
        self.find(by).click()

    def find_send(self,value,by):
        self.find(by).send_keys(value)

    def get_tips(self,by):
        self.find(by).text
