#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_webdriver_wait
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/4 12:30 
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebDriverWait:

    def setup(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://vip.ceshiren.com/#/ui_study/")


    def teardown(self):

        self.driver.quit()

    def test_webdriver_wait(self):

        def more_clickable(target_element, next_element):
            """
            官方的 excepted_conditions 不可能覆盖所有场景
            定制封装条件会更加灵活、可控
            ### 显示等待高级用法，自定义结束条件
            自定义结束条件函数下写内函数实现
            """
            def inner(driver):
                driver.find_element(*target_element).click()
                return driver.find_element(*next_element)
            return inner

        # driver.find_element(By.CSS_SELECTOR,"#primary_btn").click()
        # driver.find_element(By.CSS_SELECTOR, "#primary_btn").click()
        WebDriverWait(self.driver,10,3).until(more_clickable((By.CSS_SELECTOR,"#primary_btn"),(By.XPATH,"//*[text()='该弹框点击两次后才会弹出']")))
        time.sleep(3)




