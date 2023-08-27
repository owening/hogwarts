#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 16:33
# @Author  : Owen
# @File    : add_member_info_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

from appium_demo.base.wework_app import WeWorkApp


class AddMemberInfoPage(WeWorkApp):
    _NAME_INPUT = AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']"
    _PHONE_INPUT = AppiumBy.XPATH, "//*[@text='+86']/../..//*[@text='必填']"
    _SAVE_BTN = AppiumBy.XPATH, "//*[@text='保存']"

    def save_member_info(self, name, mobile):
        self.find_send(name, self._NAME_INPUT)
        self.find_send(mobile, self._PHONE_INPUT)
        self.find_and_click(self._SAVE_BTN)
        from appium_demo.pages.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

