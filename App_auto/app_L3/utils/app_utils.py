#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：app_utils
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/17 19:35 
'''
import time

import allure
from appium.webdriver import WebElement

from selenium.common import NoSuchElementException, TimeoutException


def swipe_exception(by: tuple, direction: str, timeout=10):
    """

    :param by: 元素定位方式和定位表达式 示例：(AppiumBy.XPATH, "//*[@text='添加成员']")
    :param direction: 滑动方向  "UP" , "DOWN"
    :param timeout: 超时时间
    :return:
    """

    def inner(driver):
        screen_width = driver.get_window_size()['width']
        screen_height = driver.get_window_size()['height']
        end_time = time.time() + timeout * 1000
        while True:
            try:
                if driver.find_element(*by):
                    # 找到元素后停止滑动,并return
                    return driver.find_element(*by)
            except NoSuchElementException as e:
                if time.time() > end_time:
                    raise (e("未找到元素"), TimeoutException("滑动查找元素超时了"))
            # 未找到元素，继续滑动
            if direction == "UP":
                driver.swipe(screen_width / 2, screen_height * 0.8, screen_width / 2, screen_height * 0.4)
            elif direction == "DOWN":
                driver.swipe(screen_width / 2, screen_height * 0.4, screen_width / 2, screen_height * 0.8)

    return inner

def app_exception_record(func):

    def inner(*agrs,**kwargs):
        self:WebElement = agrs[0]
        try:
            func(*agrs,**kwargs)
        except Exception as e:
            print("异常啦，开始记录一下")
            time_stamp = time.time()
            image_path = f"../image/{time_stamp}_image.PNG"
            page_source_path = f"../page_source/{time_stamp}_page_source.html"
            self.driver.save_screenshot(image_path)
            with open(page_source_path,"w",encoding="utf-8") as f:
                f.write(self.driver.page_source())
            allure.attach.file(image_path,name="image",attachment_type=allure.attachment_type.PNG)
            allure.attach.file(page_source_path,name="page_source",attachment_type=allure.attachment_type.TEXT)
    return inner