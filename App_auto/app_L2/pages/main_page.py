#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：main_page
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 10:38 
'''
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy

from App_auto.app_L2.base.wework_app import WeWorkApp



class MainPage(WeWorkApp):

    _CONTACTS_MENU = (AppiumBy.XPATH, "//*[@text='通讯录']")


    def click_goto_Contacts(self):
        self.find_and_displayed(self._CONTACTS_MENU)
        self.find_and_click(self._CONTACTS_MENU)
        # 进入到通讯录页面
        from App_auto.app_L2.pages.contact_page import ContactPage
        return ContactPage(self.driver)
