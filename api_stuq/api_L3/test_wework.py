#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_wework
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/11 18:56 
'''
import json

import allure
import jsonpath
import pytest
import requests
from genson import SchemaBuilder
from jsonschema import validate

from api_stuq.api_L2.utils.log_util import logger

"""

步骤：
通过企业微信接口文档获取登录权限 access_token，并进行响应断言。

创建部门，传入上一个接口的结果数据access_token，并使用jsonpath表达式获取响应结果的errmsg进行断言。

获取子部门ID列表，响应结果使用jsonschame进行断言验证。

生成对应的allure报告，显示log日志打印输出获取的access_token值。
"""


@allure.feature("企业微信标签管理")
class TestWeWork:

    def setup_class(self):
        self.baseurl = "https://qyapi.weixin.qq.com/cgi-bin"
        self.create_dep_url = self.baseurl + "/tag/create"
        self.proxy = {
            "http": "127.0.0.1:8899",
            "https": "127.0.0.1:8899"
        }

    @allure.story("正常-创建标签用例")
    @pytest.mark.parametrize("tagname,tagid", [("户外1", 711), ("零售1", 509), ("娱乐s", 0)])
    def test_create_label(self, token, tagname, tagid):
        with allure.step("获取access_token,定义请求参数"):
            logger.info(f"获取到的access_token为：{token}")
            param = {"access_token": token}
            dep_data = {
                "tagname": tagname,
                "tagid": tagid
            }
        with allure.step("发起请求并获取响应结果"):
            res = requests.request(method="post", url=self.create_dep_url, params=param, json=dep_data,
                                   proxies=self.proxy,
                                   verify=False)
        with allure.step("对各关键数据进行断言"):
            assert res.status_code == 200
            assert "created" in jsonpath.jsonpath(res.json(), "$..errmsg")

    @allure.story("异常-创建标签用例")
    @pytest.mark.parametrize("tagname,tagid,expect",
                             [("金融", 33, "UserTag Name Already Exist"),
                              ("旅游", -1, "field `tagid` expect type `uint32`"),
                              ("testname" * 6, 0, "tagname exceed max utf8 words 32")],
                             ids=["重复标签名", "标签ID参数不合法", "标签名超长"])
    def test_create_label_fail(self, token, tagname, tagid, expect):
        with allure.step("获取access_token,定义请求参数"):
            param = {"access_token": token}
            dep_data = {
                "tagname": tagname,
                "tagid": tagid
            }
        with allure.step("发起请求并获取响应结果"):
            res = requests.request(method="post", url=self.create_dep_url, params=param, json=dep_data,
                                   proxies=self.proxy,
                                   verify=False)
        with allure.step("对各关键数据进行断言"):
            res_list = jsonpath.jsonpath(res.json(), "$..errmsg")
            logger.info(f"提取到的响应errmsg信息为：{res_list}")
            res_str = "".join(res_list)
            assert res.status_code == 200
            assert expect in res_str

    def test_get_lables_list(self, token):
        url = "/tag/list"
        res = requests.request(method="get", url=self.baseurl + url, params={"access_token": token}, proxies=self.proxy,
                               verify=False)
        # print(res.json())
        #生成jsonschema
        builder = SchemaBuilder()
        builder.add_object(res.json())
        schema_res = builder.to_schema()
        #见生成jsonschema数据写入文件
        with open("schema.json", "w") as f:
            json.dump(schema_res, f)


