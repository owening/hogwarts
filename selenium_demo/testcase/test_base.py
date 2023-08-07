#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 17:55
# @Author  : Owen
# @File    : test_base.py
# @Software: PyCharm
import time

from faker import Faker

from selenium_demo.pages.login_page import LoginPage


class TestBase:

    def setup_class(self):
        fake = Faker("zh_CN")
        self.username = fake.name()
        self.account_id = fake.ssn()
        self.mobile = fake.phone_number()
        self.home_page = LoginPage().login()
        self.timestamp = time.time()
        self.company = fake.company()

    def teardown_class(self):
        self.home_page.do_quit()