#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 17:02
# @Author  : Owen
# @File    : contact_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from selenium_demo.pages.base_page import BasePage


class ContactPage(BasePage):

    __USER_NAME= (By.ID, "username")
    __ACCOUNT_ID = (By.XPATH, "//input[@id='memberAdd_acctid']")
    __MOBILE = (By.XPATH, "//input[@id='memberAdd_phone']")
    __SAVE_MEMBER_BUTTON = (By.XPATH, "//form[@class='js_member_editor_form']/div[3]/a[2]")

    def save_member(self,username,account_id,mobile):
        self.do_sendkeys(self.__USER_NAME,username)
        self.do_sendkeys(self.__ACCOUNT_ID,account_id)
        self.do_sendkeys(self.__MOBILE,mobile)
        self.do_click(self.__SAVE_MEMBER_BUTTON)
        return self
