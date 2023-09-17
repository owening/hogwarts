#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/17 15:22
# @Author  : Owen
# @File    : test_tag.py
# @Software: PyCharm
from interface.wework.api.tag_api import TagApi


class TestTag:

    def setup_class(self):
        self.tag_api = TagApi()
        self.tag_info = {"tagname": "刺客"}


    def test_create(self):
        tag_res = self.tag_api.create(self.tag_info)
        tag_id = tag_res["tagid"]
        res = self.tag_api.get(tag_id)
        self.tag_api.delete(tag_id)
        assert res["tagname"] == "刺客"
