#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 11:40
# @Author  : Owen
# @File    : test_work_wx.py
# @Software: PyCharm
import time

import allure
import yaml
from faker import Faker

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWorkWX:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def test_get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(20)
        cookies = self.driver.get_cookies()
        #登录后获取cookies存放本地yaml文件
        with open("./cookies.yaml", "w", encoding="utf-8") as f:
            yaml.dump(data=cookies, stream=f)

        # #获取本地文件cookies信息，通过便利列表添加到当前执行driver中
        # with open("./cookies.yaml", "r", encoding="utf-8") as f:
        #     cookies = yaml.safe_load(f)
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)

    @allure.story("添加成员")
    def test_add_memeber(self):
        fake = Faker("zh_CN")
        username = fake.name()
        account_id = fake.ssn()
        mobile = fake.phone_number()
        with open("./cookies.yaml", "r", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR,"[node-type='addmember']").click()
        self.driver.find_element(By.ID,"username").send_keys(username)
        self.driver.find_element(By.XPATH,"//input[@id='memberAdd_acctid']").send_keys(account_id)
        self.driver.find_element(By.XPATH,"//input[@id='memberAdd_phone']").send_keys(mobile)
        self.driver.find_element(By.XPATH,"//form[@class='js_member_editor_form']/div[3]/a[2]").click()
        time.sleep(1)
        self.driver.save_screenshot("./images/add_member.PNG")

    @allure.story("删除成员")
    def test_deleted_member(self):
        fake = Faker("zh_CN")
        username = fake.name()
        account_id = fake.ssn()
        mobile = fake.phone_number()
        with open("./cookies.yaml", "r", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, "[node-type='addmember']").click()
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='memberAdd_acctid']").send_keys(account_id)
        self.driver.find_element(By.XPATH, "//input[@id='memberAdd_phone']").send_keys(mobile)
        self.driver.find_element(By.XPATH, "//form[@class='js_member_editor_form']/div[3]/a[2]").click()

        #=========添加成员造数据后再删除============
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID,"menu_contacts").click()
        self.driver.find_element(By.XPATH,f"//*[text() ='{username}']/../../td/input").click()
        self.driver.find_element(By.XPATH, "//*[@class='js_has_member']/div[1]/a[3]").click()
        self.driver.find_element(By.XPATH,"//*[@d_ck='submit_hr_helper']").click()
        time.sleep(1)
        self.driver.save_screenshot("./images/add_member.PNG")