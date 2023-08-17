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