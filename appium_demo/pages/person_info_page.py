#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 14:18
# @Author  : Owen
# @File    : person_info_page.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

from appium_demo.base.wework_app import WeWorkApp



class PersonInfoPage(WeWorkApp):
    _BTN_OPERATE = AppiumBy.XPATH, '//*[@text="个人信息"]/../../../../../*[@class="android.widget.LinearLayout"][2]'

    def select_operate(self):
        self.find_and_click(self._BTN_OPERATE)
        from appium_demo.pages.operate_person_page import OperatePersonPage
        return OperatePersonPage(self.driver)
