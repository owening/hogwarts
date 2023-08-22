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

import allure
from faker import Faker
from App_auto.app_L3.base.wework_app import WeWorkApp


@allure.story("成员管理测试场景")
class TestMember:

    def setup_class(self):
        logging.info("实例化构造测试数据对象")
        self.fake = Faker('zh_CN')
        logging.info("实例化APP对象并启动APP")
        self.app = WeWorkApp().start()

    def setup(self):
        logging.info("初始化构造测试数据")
        self.name = self.fake.name()
        self.mobile = self.fake.phone_number()
        logging.info("启动APP跳转到主页")
        self.main_page = self.app.goto_mainpage()

    def teardown_class(self):
        logging.info("关闭APP")
        self.app.stop()

    @allure.title("添加成员-成功")
    def test_add_member(self):
        with allure.step(f"执行添加成员，输入用户名：{self.name} ,手机号：{self.mobile}"):
            toast_result = self.main_page.click_goto_Contacts().clilk_add_member().click_manual_input().add_member(
                self.name, self.mobile).get_tips()
            logging.info(f"添加成员保存后toast框内容为：{toast_result}")
        self.main_page.do_sleep()
        with allure.step("添加成功后返回通讯录页面"):
            self.main_page.do_back()
        with allure.step("执行获取添加成员的姓名"):
            result = self.main_page.click_goto_Contacts().get_member_info(self.name)
        assert toast_result == "添加成功"
        assert result == self.name
