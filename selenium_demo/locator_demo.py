#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：locator_demo
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/2 10:09 
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://vip.ceshiren.com/#/ui_study")
driver.implicitly_wait(3)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"元素定位").click()

driver.find_element(By.CSS_SELECTOR,'#ember26 > a').click()
# str1 = dr.text
# dr.click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember102"]/a').click()
sleep(1)
driver.back()


driver.quit()
