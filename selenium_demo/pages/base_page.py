#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 16:51
# @Author  : Owen
# @File    : base_page.py
# @Software: PyCharm
from selenium import webdriver


class BasePage:

    def __init__(self, base_driver=None):

        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

    def do_find(self,by):
        return self.driver.find_element(*by)

    def do_click(self,by):
        self.do_find(by).click()

    def do_sendkeys(self,by,value):
         el =self.do_find(by)
         el.clear()
         el.send_keys(value)

    def do_quit(self):
        self.driver.quit()

    def do_screenshot(self,filename):
        self.driver.save_screenshot(filename)