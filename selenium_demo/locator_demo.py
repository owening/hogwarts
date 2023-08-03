#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：locator_demo
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/2 10:09 
'''
import json
import time



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://vip.ceshiren.com/#/ui_study")
# driver.implicitly_wait(3)
driver.maximize_window()
# str = driver.find_element(By.CSS_SELECTOR,"#locate > span").text
# driver.find_element(By.CSS_SELECTOR,"#locate > span").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='father']")

WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#success_btn")))
driver.find_element(By.CSS_SELECTOR, "#success_btn > span").click()

# WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn')))
# driver.find_element(By.CSS_SELECTOR, "#success_btn").click()
# str2 = driver.find_element(By.CSS_SELECTOR,"#success_btn > span").text

# print(str2)
time.sleep(3)

driver.quit()
