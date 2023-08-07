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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_demo.log_utils import logger

driver = webdriver.Chrome()
driver.get("https://vip.ceshiren.com/#/ui_study/file_down")
driver.implicitly_wait(3)
driver.maximize_window()
# str = driver.find_element(By.CSS_SELECTOR,"#locate > span").text
# driver.find_element(By.CSS_SELECTOR,"#locate > span").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='father']")

#连续点击两次按钮，再提示
# WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#success_btn")))
# driver.find_element(By.CSS_SELECTOR, "#success_btn > span").click()

# WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn')))
# driver.find_element(By.CSS_SELECTOR, "#success_btn").click()
# str2 = driver.find_element(By.CSS_SELECTOR,"#success_btn > span").text

#=============frame定位练习==========
# driver.switch_to.frame("frame1")
# logger.debug("切换到第frame1")
# driver.find_element(By.CSS_SELECTOR,".ma-2.frame1 #frame_btn").click()
# logger.debug("第1个frame按钮定位成功")
# # time.sleep(1)
# # driver.switch_to.frame("frame2")
# driver.switch_to.default_content()
# driver.switch_to.parent_frame()
# #从frame1下,先退回父级或默认frame后才能成功切换到frame2
# driver.switch_to.frame("frame2")
# logger.debug("切换到第frame2")
# # time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,".ma-2.frame3 #frame_btn").click()
# logger.debug("第2个frame按钮定位成功")

#=====alert弹框练习=======================
# driver.find_element(By.CSS_SELECTOR,"#warning_btn").click()
# logger.debug("成功点击了alert弹框按钮进行厨房")
# time.sleep(1)
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.accept()
# time.sleep(3)

#===================元素拖拽练习=================
# e1= driver.find_element(By.CSS_SELECTOR,"#item1")
#
# e2 = driver.find_element(By.CSS_SELECTOR,"#item3")
#
# action = ActionChains(driver)
# action.click_and_hold(e1).move_to_element(e2).release().perform()
#
# # action.drag_and_drop(e1,e2)


driver.find_element(By.ID,"fileInput").send_keys("C:\\Users\\hz19054109\\PycharmProjects\\hogwarts\\selenium_demo\\add_department_1691394334.9521086.PNG")
time.sleep(5)
driver.quit()
