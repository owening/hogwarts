#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 16:39
# @Author  : Owen
# @File    : add_member_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

from appium_demo.pages.wework.wework_app import WeWorkApp



class AddMemberPage(WeWorkApp):

    _ADD_BY_MANUAL = AppiumBy.XPATH,"//*[@text='手动输入添加']"

    _TOAST_TIP_TEXT = AppiumBy.XPATH,"//*[@text='添加成功']"

    def click_manual_input(self):
        self.find_and_click(self._ADD_BY_MANUAL)
        from appium_demo.pages.wework.add_member_info_page import AddMemberInfoPage
        return AddMemberInfoPage(self.driver)

    def get_tips_result(self) -> str:
        return self.get_tips(self._TOAST_TIP_TEXT)



