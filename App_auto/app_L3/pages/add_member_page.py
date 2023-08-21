#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：add_member_page
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 16:17 
'''
from appium.webdriver.common.appiumby import AppiumBy

from App_auto.app_L3.base.wework_app import WeWorkApp



class AddMemberPage(WeWorkApp):
    _NAME_INPUT = AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']"
    _PHONE_INPUT = AppiumBy.XPATH, "//*[@text='+86']/../..//*[@text='必填']"
    _SAVE_BTN = AppiumBy.XPATH, "//*[@text='保存']"



    def add_member(self,username,mobile):
        self.find_and_send(username,self._NAME_INPUT)
        self.find_and_send(mobile,self._PHONE_INPUT)
        # 点击保存
        self.find_and_click(self._SAVE_BTN)
        from App_auto.app_L3.pages.add_member_collection_page import AddMemberCollectionPage
        return AddMemberCollectionPage(self.driver)
