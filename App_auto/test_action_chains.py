#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_action_chinas
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/23 15:06 
'''
import logging
import time

import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestAction:

    def setup(self):
        desired_caps = {}
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.FlashActivity'
        desired_caps['noReset'] = "true"
        desired_caps['deviceReadyTimeout'] = 10

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @allure.title("滑动解锁案例")
    def test_action_chains(self):
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='设置手势']").click()

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(122, 199)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(363, 404)
        actions.w3c_actions.pointer_action.move_to_location(605, 178)
        actions.w3c_actions.pointer_action.move_to_location(598, 447)
        actions.w3c_actions.pointer_action.move_to_location(563, 666)
        actions.w3c_actions.pointer_action.move_to_location(362, 701)
        actions.w3c_actions.pointer_action.move_to_location(112, 701)
        actions.w3c_actions.pointer_action.move_to_location(100, 414)
        actions.w3c_actions.pointer_action.move_to_location(374, 177)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        time.sleep(2)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='继续']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='先玩玩看']").click()
        time.sleep(1)
        assert True
