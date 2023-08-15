#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_ceshiren_L2
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/4 18:08 
'''
import time

import allure
import pytest
import six
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_demo.conftest import global_env
from selenium_demo.log_utils import logger


def ui_exception_record(func):
    """
    异常处理数据记录-装饰器
    :return:
    """
    @six.wraps(func)
    def inner(*agrs, **kwargs):
        self = agrs[0]
        try:
            return func(*agrs, **kwargs)
        except Exception as e:
            self.get_screenshot("search_result")
            self.get_page_source("search_result")
            logger.debug("将当前element对象的pagesource写入到html文件中")
            print("找不到元素啦，赶紧看下")
            raise e
    return inner


class TestCeShiRen:

    def setup(self):

        # self.browser = global_env.get("browser")
        # logger.info(f"指定浏览器为：{self.browser}")
        # if self.browser == "firefox":
        #     self.driver = webdriver.Firefox()
        # else:
        #     self.driver = webdriver.Chrome()

        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # options.add_argument("start-maximized")
        options.add_argument('window-size=375x812')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def get_screenshot(self, name):
        timestamp = int(time.time())
        image_path = f"./image/image_{name}_{timestamp}.PNG"
        self.driver.save_screenshot(image_path)
        allure.attach.file(source=image_path, name="Picture", attachment_type=allure.attachment_type.PNG)

    def get_page_source(self, name):
        page_source_path = f"./page_source/{name}_page_source.html"
        with open(page_source_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)

    # @pytest.mark.parametrize("keyword", ["selenium", "appium", "面试"])
    @pytest.mark.parametrize("keyword", ["selenium"])
    @ui_exception_record
    def test_search(self, keyword):
        self.driver.get("https://ceshiren.com/")
        time.sleep(10)
        logger.info("访问测试人社区首页")
        url = "https://ceshiren.com/search?expanded=true"
        self.driver.find_element(By.CSS_SELECTOR, "#search-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show-advanced-search").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))
        logger.info(f"进入高级搜索页面,页面地址为：{self.driver.current_url}")
        self.driver.find_element(By.XPATH, "//*[@placeholder='搜索']").send_keys(keyword)
        logger.info(f"输入搜索关键字为：{keyword}")
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        res_text = self.driver.find_element(By.CSS_SELECTOR, ".topic-title").text
        logger.info(f"搜索结果列表的第一个标题内容为：{res_text}")
        print(res_text)
        assert keyword in res_text.lower()
