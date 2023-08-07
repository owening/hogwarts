#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_department
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/7 15:26 
'''
import time

from selenium_demo.testcase.test_base import TestBase


class TestDepartment(TestBase):

    @allure.title("添加子部门")
    def test_add_department(self):
        self.home_page.click_contacts_menu().add_department(self.company)
        self.home_page.do_sleep()
        self.home_page.do_screenshot(f"../image/add_department_{self.timestamp}.PNG")