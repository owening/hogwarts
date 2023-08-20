#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：contact_page
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 11:16 
'''
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from App_auto.app_L3.base.exception_handle import swipe_exception
from App_auto.app_L3.base.wework_app import WeWorkApp


class ContactPage(WeWorkApp):



    _ADD_MEMBER_MENU = (AppiumBy.XPATH, "//*[@text='添加成员']")

    _SELECT_MEMBER =(AppiumBy.XPATH, "//*[@text='{}']")

    def clilk_add_member(self):
        # 执行等待并查找元素
        WebDriverWait(self.driver, 10).until(swipe_exception(self._ADD_MEMBER_MENU, "UP", 15))
        # 点击添加按钮跳转到添加成员页面
        self.find_and_click(self._ADD_MEMBER_MENU)
        from App_auto.app_L3.pages.add_member_collection_page import AddMemberCollectionPage
        return AddMemberCollectionPage(self.driver)



    def get_member_info(self,keyword):
        # 返回通讯录页面,获取添加的成员信息

        by_locator = (self._SELECT_MEMBER[0],self._SELECT_MEMBER[1].format(keyword))
        ele = WebDriverWait(self.driver, 10).until(swipe_exception(by_locator, "DOWN", 15))
        return ele.text
