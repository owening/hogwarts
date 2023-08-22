#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 23:12
# @Author  : Owen
# @File    : black_handle.py
# @Software: PyCharm
import logging
import traceback

from appium.webdriver import WebElement

black_list = [("by", "locator"), ("by", "locator")]


def black_list_proce(func):
    def inner(*args, **kwargs):
        from App_auto.app_L3.base.base_page import BasePage
        basepage: BasePage = args[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            for black in black_list:
                logging.info("遍历黑名单进行处理")
                eles: WebElement = basepage.finds(black)
            if len(eles) > 0:
                logging.info("点击黑名单弹框")
                eles[0].click()
                return func(*args, **kwargs)
            logging.error(f"遍历黑名单，仍未找到元素，异常信息 ====> {e}")
            logging.error(f"traceback.format_exc() ====> {traceback.format_exc()}")
        raise e

    return inner

