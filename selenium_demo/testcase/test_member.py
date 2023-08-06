#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 17:35
# @Author  : Owen
# @File    : test_member.py
# @Software: PyCharm
import time

from faker import Faker
from selenium import webdriver

from selenium_demo.pages.login_page import LoginPage
from selenium_demo.testcase.test_base import TestBase


class TestMember(TestBase):


    def test_addmember(self):
        self.home_page.click_add_member().save_member(self.username,self.account_id,self.mobile)
        time.sleep(1)
        self.home_page.do_screenshot(f"../image/add_member_{self.timestamp}.PNG")



