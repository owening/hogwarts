#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_tag
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/19 10:05 
'''
import os

import allure
import pytest
from jsonpath import jsonpath
from api_stuq.api_L4.api.tag_api import TagAPI


@allure.feature("标签管理")
class TestTag:

    def setup(self):
        self.tag_api = TagAPI()

    @allure.story("创建标签")
    @pytest.mark.parametrize("tag_info", [{"tagname": "藏獒"}])
    def test_tag_create(self,tag_info):
        with allure.step("创建标签"):
            tag_id = self.tag_api.create(tag_info)["tagid"]
        with allure.step("获取标签"):
            res = self.tag_api.get_tag_user(tag_id)
        with allure.step("删除新增的标签"):
            self.tag_api.delete(tag_id)
        assert jsonpath(res, "$..tagname")[0] == "藏獒"




