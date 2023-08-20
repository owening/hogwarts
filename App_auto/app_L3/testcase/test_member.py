#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_member
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 16:50 
'''
import logging

from faker import Faker

from App_auto.app_L3.base.exception_handle import app_exception_record
from App_auto.app_L3.base.wework_app import WeWorkApp


class TestCase:

    def setup_class(self):
        # 初始化构造测试数据
        fake = Faker('zh_CN')
        self.name = fake.name()
        self.mobile = fake.phone_number()
        logging.info("启动APP跳转到主页")
        self.main_page = WeWorkApp().start().goto_mainpage()


    def teardown_class(self):
        logging.info("关闭APP")
        self.main_page.stop()

    @app_exception_record
    def test_add_member(self):
        logging.info(f"执行添加成员，输入用户名：{self.name} ,手机号：{self.mobile}")
        toast_result = self.main_page.click_goto_Contacts().clilk_add_member().click_manual_input().add_member(self.name,self.mobile)
        logging.info(f"添加成员保存后toast框内容为：{toast_result}")
        self.main_page.do_sleep()
        logging.info("添加成功后返回通讯录页面")
        self.main_page.do_back()
        logging.info("执行获取添加成员的姓名")
        result = self.main_page.click_goto_Contacts().get_member_info(self.name)
        assert toast_result == "添加成功"
        assert result == self.name