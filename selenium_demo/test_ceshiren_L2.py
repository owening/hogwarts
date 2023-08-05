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

from selenium_demo.log_utils import logger


class TestCeShiRen:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize("keyword",["selenium","appium","面试"])
    @pytest.mark.parametrize("keyword", ["selenium"])
    def test_search(self, keyword):
        self.driver.get("https://ceshiren.com/")
        logger.info("访问测试人社区首页")
        self.driver.save_screenshot("ceshiren_main_page.png")
        url = "https://ceshiren.com/search?expanded=true"
        self.driver.find_element(By.CSS_SELECTOR, "#search-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show-advanced-search").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))
        self.driver.save_screenshot("advanced_search_page.png")
        logger.info(f"进入高级搜索页面,页面地址为：{self.driver.current_url}")
        self.driver.find_element(By.XPATH, "//*[@placeholder='搜索']").send_keys(keyword)
        logger.info(f"输入搜索关键字为：{keyword}")
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        with open("page_source.txt", "w", encoding="utf-8") as f: f.write(self.driver.page_source)
        logger.debug("将当前element对象的pagesource写入到文件page_source.txt中")
        res_text = self.driver.find_element(By.CSS_SELECTOR, ".topic-title").text
        self.driver.save_screenshot("search_result.png")
        logger.info(f"搜索结果列表的第一个标题内容为：{res_text}")
        print(res_text)
        assert keyword in res_text.lower()
        time.sleep(3)
