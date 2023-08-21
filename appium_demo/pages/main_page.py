#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 16:32
# @Author  : Owen
# @File    : main_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy




class MainPage(WeWorkApp):

    _CONTACT_BTN = AppiumBy.XPATH,"//*[@text='通讯录']"

    def click_contact(self):
        self.find_click(self._CONTACT_BTN)
        from appium_demo.pages.member_list_page import MemberListPage
        return MemberListPage(self.driver)