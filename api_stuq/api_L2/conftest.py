#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：conftest
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/15 14:40 
'''
import pytest
import requests

from api_stuq.api_L2.utils.log_util import logger

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name=i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="session")
def token():
    get_token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    params_data = {
        "corpid": "wwc21827e63c44f94f",
        "corpsecret": "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"
    }
    res = requests.request(method="post", url=get_token_url, params=params_data)
    return res.json()['access_token']