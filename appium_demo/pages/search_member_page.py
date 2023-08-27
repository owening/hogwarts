#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 11:37
# @Author  : Owen
# @File    : search_member_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

from appium_demo.base.wework_app import WeWorkApp


class SearchMemberPage(WeWorkApp):
    _SEARCH_INPUT = AppiumBy.XPATH, "//*[@text='搜索']"

    _INPUT_NAME = AppiumBy.XPATH, '//*[@class="android.widget.EditText"]'
    _TEXT_MEMBER_LIST = AppiumBy.XPATH, '//*[@class="android.widget.ListView"]//*[@class="android.widget.ImageView"]'

    # def search_member_by_name(self, name):
    #         self.find_send(name,self._SEARCH_INPUT)
    #
    #         self.find_click()
    #         return MemberInfoPage(self.driver)

    def search_member(self, name):
        self.find_send(name, self._INPUT_NAME)
        member_list = self.finds(self._TEXT_MEMBER_LIST)
        return member_list
