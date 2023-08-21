#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：add_member_collection_page
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 14:36 
'''
from appium.webdriver.common.appiumby import AppiumBy

from App_auto.app_L3.base.wework_app import WeWorkApp


class AddMemberCollectionPage(WeWorkApp):


    _MANUAL_INPUT_MENU = (AppiumBy.XPATH, "//*[@text='手动输入添加']")
    _ADD_SUCCESS_TOAST = AppiumBy.XPATH,"//*[@text='添加成功']"

    def click_manual_input(self):
        # 点击手动输入添加
        self.find_and_click(self._MANUAL_INPUT_MENU)
        from App_auto.app_L3.pages.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)


    def get_tips(self):
        # 获取toast提示框内容
        return self.get_text(self._ADD_SUCCESS_TOAST)
