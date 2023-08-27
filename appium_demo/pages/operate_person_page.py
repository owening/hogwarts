#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 14:19
# @Author  : Owen
# @File    : operate_person_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

from appium_demo.base.wework_app import WeWorkApp



class OperatePersonPage(WeWorkApp):
    _BTN_EDIT_MEMBER = AppiumBy.XPATH, '//*[@text="编辑成员"]'

    def edit_person_info(self):
        self.find_and_click(self._BTN_EDIT_MEMBER)
        from appium_demo.pages.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

