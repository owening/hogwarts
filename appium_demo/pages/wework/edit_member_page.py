#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 10:59
# @Author  : Owen
# @File    : edit_member_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

from appium_demo.pages.wework.wework_app import WeWorkApp


class EditMemberPage(WeWorkApp):

    _BTN_DELETE_MEMBER = AppiumBy.XPATH, '//*[@text="删除成员"]'



    def select_delete(self):
        self.swipe_find(self._BTN_DELETE_MEMBER).click()
        from appium_demo.pages.wework.confirm_delete_page import ConfirmDeletePage
        return ConfirmDeletePage(self.driver)
