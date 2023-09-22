#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：wework_api
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/19 10:08 
'''
import os

import requests

from api_stuq.api_L4.utils.log_util import logger


class WeWorkAPI:

    def __init__(self):
        os.getenv("test")
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin/"
        self.corpid = "wwc21827e63c44f94f"
        self.corpsecret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
        self.token = self.get_token()

    def get_token(self):
        url = self.base_url + "gettoken"
        token_params = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret
        }
        res = requests.request("get", url=url, params=token_params)
        token = res.json()["access_token"]
        logger.info(f"获取的access_token为：{token}")
        return token

    def send(self, method, url, **kwargs):
        if kwargs.get("params"):
            kwargs["params"].update({"access_token": self.token})
        else:
            kwargs["params"] = {"access_token": self.token}
        return requests.request(method=method, url=self.base_url + url, **kwargs).json()
