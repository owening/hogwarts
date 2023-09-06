#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 10:49
# @Author  : Owen
# @File    : member_info_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

from App_auto.app_L3.base.wework_app import WeWorkApp



class MemberInfoPage(WeWorkApp):
    _THREE_POINT = AppiumBy.ID, "com.tencent.wework:id/lll"


    _EDIT_MEMBER_BTN = AppiumBy.XPATH, "//*[@text='编辑成员']"


    def click_three_point(self):
        self.find_and_click(self._THREE_POINT)
        return self


    def click_edit_member(self):
        self.find_and_click(self._EDIT_MEMBER_BTN)
        from App_auto.app_L3.pages.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

