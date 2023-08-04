#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_ceshiren
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/3 19:29 
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCeShiRen:

    def setup(self):
        """
        前置步骤
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://ceshiren.com/search?expanded=true")


    def teardown(self):
        """
        后置步骤
        """
        self.driver.quit()

    @pytest.mark.parametrize("keyword",["selenium","appium","面试"])
    def test_search(self,keyword):
        """
        测试步骤
        断言
        """
        self.driver.find_element(By.CSS_SELECTOR,"[placeholder='搜索']").send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR,".search-cta").click()
        res_element = self.driver.find_element(By.CSS_SELECTOR,".topic-title")
        print(f"搜索结果第一个标题为：{res_element.text}")
        assert keyword in res_element.text.lower()




