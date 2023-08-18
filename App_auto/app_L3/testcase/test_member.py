#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_member
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 16:50 
'''
from faker import Faker
from App_auto.app_L2.base.wework_app import WeWorkApp


class TestCase:

    def setup_class(self):
        # 初始化构造测试数据
        fake = Faker('zh_CN')
        self.name = fake.name()
        self.mobile = fake.phone_number()
        self.main_page = WeWorkApp().start().goto_mainpage()


    def teardown_class(self):
        self.main_page.stop()

    def test_add_member(self):
        #执行添加成员
        self.main_page.click_goto_Contacts().clilk_add_member().click_manual_input().add_member(self.name,self.mobile)
        self.main_page.do_sleep()
        self.main_page.do_back()
        #获取添加成员的姓名
        result = self.main_page.click_goto_Contacts().get_member_info(self.name)
        assert result == self.name