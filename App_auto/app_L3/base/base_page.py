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





class BasePage:

    def __init__(self, base_driver: WebDriver = None):
        self.driver = base_driver

    # @app_exception_record
    # @black_list_proce
    def find(self, by):
        return self.driver.find_element(*by)

    # @app_exception_record
    # @black_list_proce
    def finds(self, by):
        return self.driver.find_elements(*by)

    def find_and_send(self, text,by):
        return self.find(by).send_keys(text)

    def find_and_click(self, by):
        return self.find(by).click()

    def get_text(self, by):
        return self.find(by).text

    def find_and_displayed(self, by):
        return self.find(by).is_displayed()


    def do_sleep(self,seconds=1):
        time.sleep(seconds)

    def do_back(self):
        self.driver.back()

    def page_source(self):
        return self.driver.page_source

    def screenshot(self,filename):
        self.driver.save_screenshot(filename)

    def by_keyword_find(self,keyword, by ):
        """
        通过关键字定位信息定位元素
        示例： "//*[text() ='{}']/../../td/input".format(keywords)
        :param by:
        :param keywords:
        :return:
        """
        return self.do_find(by[0], by[1].format(keyword))

    def get_cur_time(self):
        t = time.localtime(time.time())
        cur_time = time.strftime("%Y-%m-%d_%H%M%S",t)
        return cur_time