#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：dirver_web
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/1 17:46 
'''
import time

from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"wd").send_keys("selenium")
time.sleep(1)
driver.find_element(By.ID,"su").click()
time.sleep(1)
driver.refresh()
driver.find_element(By.XPATH,'//*[@id="s_tab"]/div/a[2]').click()
time.sleep(1)
str = driver.find_element(By.XPATH,'//*[@id="pagelet_frs-header/pagelet/head"]/div/div[3]/div[2]/div[2]/div[2]/a').text
driver.back()
time.sleep(1)
driver.minimize_window()
driver.quit()
assert str == "selenium吧"

