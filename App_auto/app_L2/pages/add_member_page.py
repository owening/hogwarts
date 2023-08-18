#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：add_member_page
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 16:17 
'''
import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from App_auto.app_L2.base.wework_app import WeWorkApp


class AddMemberPage(WeWorkApp):

    _USERNAME = (AppiumBy.ID, "com.tencent.wework:id/c4k")
    _MOBILE = (AppiumBy.ID, "com.tencent.wework:id/igg")
    _SAVE_BTN = (AppiumBy.ID, "com.tencent.wework:id/b2s")
    _ADD_SUCCESS_TOAST = (AppiumBy.XPATH,"//*[@text='添加成功']")

    def add_member(self,username,mobile):
        self.find_and_send(self._USERNAME,username)
        self.find_and_send(self._MOBILE,mobile)
        # 点击保存
        self.find_and_click(self._SAVE_BTN)
        # 获取toast提示框内容
        toast_element = self.find(self._ADD_SUCCESS_TOAST)
        return toast_element.text