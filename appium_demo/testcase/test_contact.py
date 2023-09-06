#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/20 16:45
# @Author  : Owen
# @File    : test_contact.py
# @Software: PyCharm
import pytest
from faker import Faker

from appium_demo.pages.wework.wework_app import WeWorkApp
from appium_demo.utils.data_util import DataUtil


class TestContact:

    def setup_class(self):
        self.app = WeWorkApp()
        self.faker = Faker('zh_CN')
        self.name = self.faker.name()
        self.mobile = self.faker.phone_number()

    def setup(self):
        self.main = self.app.star().goto_main()

    def teardown(self):
        self.app.go_back(2)

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize("name, phone", DataUtil().get_member_data())
    def test_add_member(self, name, phone):
        tips = self.main.click_goto_Contacts().clilk_add_member().click_manual_input() \
            .save_member_info(name, phone).get_tips_result()
        assert tips == "添加成功"

    @pytest.mark.parametrize("name", [data[0] for data in DataUtil().get_member_data()])
    def test_delete_member(self, name):
        member_list = self.main.click_goto_Contacts().goto_person_info(name) \
            .select_operate().edit_person_info().select_delete().confirm_delete_member() \
            .goto_search_page().search_member(name)
        assert len(member_list) == 0
