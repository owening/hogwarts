#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/17 15:16
# @Author  : Owen
# @File    : wework_api.py
# @Software: PyCharm
import requests

from interface.wework.utils.log_util import logger


class WeWorkApi:

    def __init__(self):
        self.corpid = "wwc21827e63c44f94f"
        self.corpsecret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin/"
        self.token = self.get_token()

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        token_res = requests.request("get", url,
                                     params={"corpid": self.corpid, "corpsecret": self.corpsecret})
        token = token_res.json()["access_token"]
        return token

    def send(self, method, url, **kwargs):
        if kwargs.get("params"):
            kwargs["params"].update({"access_token": self.token})
        else:
            kwargs["params"] = {"access_token": self.token}
        logger.debug(f"请求url为:{url}")
        res = requests.request(method, url=self.base_url + url, **kwargs)
        logger.debug(f"响应信息为:{res.text}")
        return res.json()
