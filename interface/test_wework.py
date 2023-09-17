#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/17 10:39
# @Author  : Owen
# @File    : test_wework.py
# @Software: PyCharm
import pytest
import requests


class TestWeWork:
    get_token_fail_data = [({"corpid": "", "corpsecret": "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"}, 41002),
                           ({"corpid": "wwc21827e63c44f94f", "corpsecret": ""}, 41004),
                           ({"corpid": "wwc21827e63c44f94f666",
                             "corpsecret": "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"}, 40013),
                           ({"corpid": "wwc21827e63c44f94f",
                             "corpsecret": "1230qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"}, 40001)]

    def setup_class(self):
        self.corpid = "wwc21827e63c44f94f"
        self.corpsecret = "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"

    @pytest.mark.parametrize("token_params,errcode", [
        ({"corpid": "wwc21827e63c44f94f", "corpsecret": "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"}, 0)])
    def test_get_token(self, token_params, errcode):
        # 获取access_token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        res = requests.request("get", url, params=token_params)
        assert res.status_code == 200
        assert res.json().get("errcode") == errcode

    @pytest.mark.parametrize("token_params,errcode",
                             [({"corpid": "", "corpsecret": "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"}, 41002),
                              ({"corpid": "wwc21827e63c44f94f", "corpsecret": ""}, 41004),
                              ({"corpid": "wwc21827e63c44f94f666",
                                "corpsecret": "0qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"}, 40013),
                              ({"corpid": "wwc21827e63c44f94f",
                                "corpsecret": "1230qjRWh5cnLgJQPUDLB2uHMwJn0h0KgKr93NBbyEDso0"}, 40001)]
        , ids=("【必填】不传 corpid", "【必填】不传 secret", "【异常】错误的 corpid", "【异常】错误的 secret"))
    def test_get_token_fail(self, token_params, errcode):
        url = " https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        res = requests.request("get", url, params=token_params)
        assert res.status_code == 200
        assert res.json().get("errcode") == errcode

    # def test_get_lables(self):
    #     # 获取标签列表
    #     get_label_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
    #     # label_res = requests.get(get_label_url)
    #     label_res = requests.request("get", get_label_url)
    #     print(label_res.json())

    def test_add_tag(self):
        # 获取token
        get_token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        token_res = requests.request("get", get_token_url,
                                     params={"corpid": self.corpid, "corpsecret": self.corpsecret})
        token = token_res.json()["access_token"]

        # 创建标签
        create_tag_url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        tag_info = {"tagname": "骑士2"}
        create_res = requests.request("post", create_tag_url, params={"access_token": token}, json=tag_info)
        tag_id = create_res.json()["tagid"]

        # 查询标签成员
        get_tag_user_url = "https://qyapi.weixin.qq.com/cgi-bin/tag/get"
        get_tag_res = requests.request("get", get_tag_user_url, params={"access_token": token, "tagid": tag_id})
        get_tag_res.json()["tagname"] == "骑士2"
