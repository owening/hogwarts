#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 16:45
# @Author  : Owen
# @File    : test_contact.py
# @Software: PyCharm
from faker import Faker

from appium_demo.base.wework_app import WeWorkApp


class TestContact:

    def setup_class(self):
        self.app = WeWorkApp()
        self.faker = Faker('zh_CN')

    def setup(self):
        self.mian = self.app.star().goto_main()
        self.name = self.faker.name()
        self.mobile = self.faker.phone_number()


    def test_add_member(self):
        tips = self.mian.click_contact().click_add_member().click_add_by_manual().\
            save_member_info(self.name,self.mobile).get_tips_result()

        assert tips == "添加成功"