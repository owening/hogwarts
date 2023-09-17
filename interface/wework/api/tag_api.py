#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/17 15:16
# @Author  : Owen
# @File    : tag_api.py
# @Software: PyCharm
import requests

from interface.wework.api.wework_api import WeWorkApi


class TagApi(WeWorkApi):

    def create(self, tag_info):
        url = "tag/create"
        res = self.send("post", url, params={"access_token": self.token}, json=tag_info)
        return res

    def delete(self, tagid):
        url = "tag/delete"
        res = self.send("get", url, params={"access_token": self.token, "tagid": tagid})
        return res

    def update(self):
        pass

    def get(self, tag_id):
        url = "tag/get"
        res = self.send("get", url, params={"access_token": self.token, "tagid": tag_id})
        return res
