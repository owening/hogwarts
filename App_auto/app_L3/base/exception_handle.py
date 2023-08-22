#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 23:09
# @Author  : Owen
# @File    : exception_handle.py
# @Software: PyCharm

import logging
import os
import time

import allure


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
                logging.info(f"定位元素{by}and {type(by)}")
                if driver.find_element(*by):
                    # 找到元素后停止滑动,并return
                    return driver.find_element(*by)
            except NoSuchElementException as e:
                if time.time() > end_time:
                    raise (e("未找到元素"), TimeoutException("滑动查找元素超时了"))
                # 未找到元素，继续滑动
                if direction == "UP":
                    logging.info("向上滑动，查找元素中...")
                    driver.swipe(screen_width / 2, screen_height * 0.8, screen_width / 2, screen_height * 0.4)
                elif direction == "DOWN":
                    logging.info("向下滑动，查找元素中...")
                    driver.swipe(screen_width / 2, screen_height * 0.4, screen_width / 2, screen_height * 0.8)

    return inner

def app_exception_record(func):
    """
    发生异常时进行截图和记录当前页面pagesource
    :param func:
    :return:
    """

    def inner(*agrs,**kwargs):
        from App_auto.app_L3.base.base_page import BasePage
        basepage:BasePage = agrs[0]
        try:
            return func(*agrs,**kwargs)
        except NoSuchElementException as e:
            logging.warning("执行过程中发生异常,记录截图和pagesource")
            cur_time = basepage.get_cur_time()
            image_name = f"{cur_time}_({basepage.driver.current_activity}).PNG"
            image_path = os.path.join(os.path.dirname(__file__), "..", "images", image_name)
            page_source_name = f"{cur_time}_({basepage.driver.current_activity}).html"
            page_source_path = os.path.join(os.path.dirname(__file__), "..", "page_source", page_source_name)

            basepage.screenshot(image_path)
            with open(page_source_path,"w",encoding="utf-8") as f:
                f.write(basepage.page_source())
            allure.attach.file(image_path,name="images",attachment_type=allure.attachment_type.PNG)
            allure.attach.file(page_source_path,name="page_source",attachment_type=allure.attachment_type.TEXT)
            logging.error(f"跑出捕获的异常>>>{e}")
            raise e
    return inner

