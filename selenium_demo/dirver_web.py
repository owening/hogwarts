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

hogwarts_grid_url = "https://selenium-node.hogwarts.ceshiren.com/wd/hub"

capabilities = {"browserName": "firefox", "browserVersion": "99.0"}

# options = webdriver.ChromeOptions()
# options.add_argument('window-size=300x600')
# options.add_argument("--headless")
# options.add_argument("start-maximized")
# options.add_argument('window-size=375x812')


# # 指定用户客户端-模拟手机浏览
# options.add_argument(
#     'user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')




# driver = webdriver.Remote(command_executor=hogwarts_grid_url,desired_capabilities=capabilities)
driver = webdriver.Remote(
    command_executor=hogwarts_grid_url,
    desired_capabilities=capabilities)
# driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)
driver.get("https://www.baidu.com")

print(driver.get_window_size())
# driver.maximize_window()

driver.find_element(By.NAME,"wd").send_keys("selenium")

driver.find_element(By.ID,"su").click()

driver.refresh()
driver.find_element(By.XPATH,'//*[@id="s_tab"]/div/a[2]').click()

str = driver.find_element(By.XPATH,'//*[@id="pagelet_frs-header/pagelet/head"]/div/div[3]/div[2]/div[2]/div[2]/a').text
driver.back()

driver.minimize_window()
driver.quit()
assert str == "selenium吧"

