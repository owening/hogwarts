#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 10:59
# @Author  : Owen
# @File    : edit_member_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from App_auto.app_L3.base.exception_handle import swipe_exception
from App_auto.app_L3.base.wework_app import WeWorkApp



class EditMemberPage(WeWorkApp):
    _DELETE_MEMBER_BTN = AppiumBy.XPATH, "//*[@text='删除成员']"

    _CONFIRM_MEMBER_BTN = AppiumBy.XPATH, "//*[@text='删除']"

    def confirm_delete_member(self):
        WebDriverWait(self.driver,10).until(swipe_exception(self._DELETE_MEMBER_BTN,"UP",10))
        self.find_and_click(self._DELETE_MEMBER_BTN)
        self.find_and_click(self._CONFIRM_MEMBER_BTN)
        from App_auto.app_L3.pages.contact_page import ContactPage
        return ContactPage(self.driver)
