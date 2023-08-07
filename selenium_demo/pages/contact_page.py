#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 17:02
# @Author  : Owen
# @File    : contact_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from selenium_demo.pages.base_page import BasePage


class ContactPage(BasePage):
    #添加成员元素属性
    _USER_NAME = (By.ID, "username")
    _ACCOUNT_ID = (By.XPATH, "//input[@id='memberAdd_acctid']")
    _MOBILE = (By.XPATH, "//input[@id='memberAdd_phone']")
    _SAVE_MEMBER_BTN = (By.XPATH, "//form[@class='js_member_editor_form']/div[3]/a[2]")

    #删除成员元素属性
    _MENU_CONTACTS = (By.ID, "menu_contacts")
    _SELECT_MEMBER = (By.XPATH, "//*[text() ='{}']/../../td/input")
    _DELETE_BTN = (By.XPATH, "//*[@class='js_has_member']/div[1]/a[3]")
    _COMFIRM_DELETE = (By.XPATH, "//*[@d_ck='submit_hr_helper']")

    #添加部门元素
    _DEPARTMENT_HOVER = (By.CSS_SELECTOR,".jstree-clicked .jstree-contextmenu-hover")
    _SUB_DEPARTMENT_ADD_BTN = (By.XPATH,"//*[text()='添加子部门']")
    _DEPARTMENT_NAME = (By.XPATH,"//*[@name='name']")
    _NEW_DEPARTMENT_SUBMIT = (By.XPATH,"//*[@d_ck='submit']")


    def save_member(self, username, account_id, mobile):
        self.do_sendkeys(self._USER_NAME, username)
        self.do_sendkeys(self._ACCOUNT_ID, account_id)
        self.do_sendkeys(self._MOBILE, mobile)
        self.do_click(self._SAVE_MEMBER_BTN)
        return self

    def delte_member(self, username):
        self.do_click(self._MENU_CONTACTS)
        self.do_by_keywords_find(self._SELECT_MEMBER,username).click()
        self.do_click(self._DELETE_BTN)
        self.do_click(self._COMFIRM_DELETE)
        return self

    def add_department(self,department_name):

        self.do_click(self._DEPARTMENT_HOVER)
        self.do_click(self._SUB_DEPARTMENT_ADD_BTN)
        self.do_sendkeys(self._DEPARTMENT_NAME,department_name)
        self.do_click(self._NEW_DEPARTMENT_SUBMIT)
        return self

