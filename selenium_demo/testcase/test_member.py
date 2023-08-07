#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 17:35
# @Author  : Owen
# @File    : test_member.py
# @Software: PyCharm
import time

import allure

from selenium_demo.testcase.test_base import TestBase


class TestMember(TestBase):

    @allure.title("添加成员")
    def test_addmember(self):
        self.home_page.click_add_member().save_member(self.username,self.account_id,self.mobile)
        self.home_page.do_sleep()
        self.home_page.do_screenshot(f"../image/add_member_{self.timestamp}.PNG")

    @allure.title("删除成员")
    def test_delete_member(self):
        self.home_page.click_add_member().save_member(self.username, self.account_id, self.mobile)
        self.home_page.do_sleep()
        self.home_page.click_contacts().delte_member(self.username)
        self.home_page.do_screenshot(f"../image/deleted_member_{self.timestamp}.PNG")



