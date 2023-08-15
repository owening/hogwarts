#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/14 14:46
# @Author  : Owen
# @File    : app_demo1.py
# @Software: PyCharm
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

caps = {}
caps["platformName"] = "Android"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["deviceName"] = "emulator-5554"
caps["noSign"] = True
caps["ensureWebviewsHavePages"] = True
# caps["noReset"] = True


driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(8)
el1 = driver.find_element(AppiumBy.ID,"com.xueqiu.android:id/tv_agree")
el1.click()

el2 = driver.find_element(AppiumBy.ID,"com.xueqiu.android:id/login_outside")
el2.click()
el3 = driver.find_element(AppiumBy.ID,"com.xueqiu.android:id/login_account")
el3.send_keys("18033058407")
el4 = driver.find_element(AppiumBy.ID,"com.xueqiu.android:id/login_password")
el4.send_keys("123456")
el5 = driver.find_element(AppiumBy.ID,"com.xueqiu.android:id/service_agreement")
el5.click()
driver.back()
el6 = driver.find_element_by_id("com.xueqiu.android:id/service_agreement")
el6.click()
driver.back()
el7 = driver.find_element_by_id("com.xueqiu.android:id/button_next")
el7.click()

driver.quit()