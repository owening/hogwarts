#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_wework
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/11 18:56 
'''
import allure

from api_stuq.api_L1.utils.log_util import logger

"""
1.通过企业微信接口文档获取登录权限 access_token，并进行响应断言。

2.生成对应的allure报告，显示log日志打印输出获取的access_token值。
"""
import requests

@allure.feature("企业微信获取access_token")
class TestWeWork:

    def setup_class(self):
        self.corpid = "wwc21827e63c44f94f"
        self.corpsecret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
        self.baseurl = "https://qyapi.weixin.qq.com/cgi-bin"
        self.get_token_url = self.baseurl + "/gettoken"
        pass

    @allure.story("获取access_token成功用例")
    def test_get_token(self):
        params_data = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret
        }
        res = requests.request(method="post", url=self.get_token_url, params=params_data)
        logger.info(f"获取到的access_token为：{res.json()['access_token']}")
        assert res.status_code == 200
        assert res.json()["errmsg"] == "ok"
        assert res.json()["access_token"] != ""

    @allure.story("获取access_token异常用例")
    def test_get_token_fail(self):
        params_data = {
            "corpid": self.corpid,
            "corpsecret": "0qjasdfhgjqqwsdfhgjqqwsderryuiso0"
        }
        res = requests.request(method="post", url=self.get_token_url, params=params_data)
        logger.info(f"响应结果为：{res.text}")
        assert res.status_code == 200
        assert res.json()["errcode"] == 40001
        assert "invalid credential" in res.json()["errmsg"]
