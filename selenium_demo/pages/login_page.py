#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 17:13
# @Author  : Owen
# @File    : login_page.py
# @Software: PyCharm
import time

import yaml

from selenium_demo.pages.base_page import BasePage



class LoginPage(BasePage):

    def login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(10)
        cookies = self.driver.get_cookies()
        # 登录后获取cookies存放本地yaml文件
        with open("../cookies.yaml", "w", encoding="utf-8") as f:
            yaml.dump(data=cookies, stream=f)

        #获取本地文件cookies信息，通过便利列表添加到当前执行driver中
        with open("../cookies.yaml", "r", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        #重新访问或刷新首页,验证添加cookies是否正常可用
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        from selenium_demo.pages.home_page import HomePage
        return HomePage(self.driver)