#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 14:29
# @Author  : Owen
# @File    : confirm_delete_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

from appium_demo.base.wework_app import WeWorkApp


class ConfirmDeletePage(WeWorkApp):
    _BTN_CONFIRM = AppiumBy.XPATH, '//*[@text="删除"]'

    def confirm_delete_member(self):
        self.find_and_click(self._BTN_CONFIRM)
        from appium_demo.pages.contact_page import ContactPage
        return ContactPage(self.driver)
