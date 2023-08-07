#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 16:58
# @Author  : Owen
# @File    : home_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from selenium_demo.pages.base_page import BasePage



class HomePage(BasePage):

    _ADD_MEMBER = (By.CSS_SELECTOR, "[node-type='addmember']")
    _MENU_CONTACTS = (By.ID, "menu_contacts")



    def click_add_member(self):
        """
        点击添加成员
        :return:
        """
        self.do_find(self._ADD_MEMBER).click()
        from selenium_demo.pages.contact_page import ContactPage
        return ContactPage(self.driver)

    def click_contacts_menu(self):
        self.do_click(self._MENU_CONTACTS)
        from selenium_demo.pages.contact_page import ContactPage
        return ContactPage(self.driver)