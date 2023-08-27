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

from appium_demo.base.wework_app import WeWorkApp


from appium_demo.test_wework import swipe_exception


class ContactPage(WeWorkApp):
    _ADD_MEMBER_MENU = (AppiumBy.XPATH, "//*[@text='添加成员']")

    _SELECT_MEMBER = (AppiumBy.XPATH, "//*[@text='{}']")

    _SEARCH_INPUT = AppiumBy.XPATH, "//*[@text='搜索']"

    _BTN_SEARCH = AppiumBy.XPATH, '//*[@text="好啊游爱豆有限公司"]/../../../following-sibling::*/*[1]'

    def clilk_add_member(self):
        # 执行等待并查找元素
        WebDriverWait(self.driver, 10).until(swipe_exception(self._ADD_MEMBER_MENU, "UP", 10))
        # 点击添加按钮跳转到添加成员页面
        self.find_and_click(self._ADD_MEMBER_MENU)
        from appium_demo.pages.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_member_info(self, keyword):
        # 返回通讯录页面,获取添加的成员信息
        ele = WebDriverWait(self.driver, 10).until(
            swipe_exception((self._SELECT_MEMBER[0], self._SELECT_MEMBER[1].format(keyword)), "DOWN", 10))
        return ele.text

    def goto_person_info(self, name):
        by = AppiumBy.XPATH, f"//*[@text='{name}']"
        self.swipe_find(by).click()
        from appium_demo.pages.person_info_page import PersonInfoPage
        return PersonInfoPage(self.driver)

    def goto_search_page(self):
        self.find_and_click(self._BTN_SEARCH)
        from appium_demo.pages.search_member_page import SearchMemberPage
        return SearchMemberPage(self.driver)
