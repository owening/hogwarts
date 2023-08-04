#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_ceshiren_L2
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/4 18:08 
'''
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCeShiRen:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://ceshiren.com/")
        self.driver.save_screenshot("ceshiren_main_page.png")


    def teardown(self):
        self.driver.quit()


    @pytest.mark.parametrize("keyword",["selenium","appium","面试"])
    def test_search(self,keyword):
        url = "https://ceshiren.com/search?expanded=true"
        self.driver.find_element(By.CSS_SELECTOR,"#search-button").click()
        self.driver.find_element(By.CSS_SELECTOR,".show-advanced-search").click()
        WebDriverWait(self.driver,10).until(expected_conditions.url_to_be(url))
        self.driver.save_screenshot("advanced_search_page.png")
        self.driver.find_element(By.CSS_SELECTOR,"[placeholder='搜索']").send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR,".search-cta").click()
        print(f"查询结果页pagesource: {self.driver.page_source}")
        res_text = self.driver.find_element(By.CSS_SELECTOR, ".topic-title").text
        self.driver.save_screenshot("search_result.png")
        print(res_text)
        assert keyword in res_text.lower()
        time.sleep(3)