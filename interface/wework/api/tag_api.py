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
        return self.send("post", url, json=tag_info)


    def delete(self, tagid):
        url = "tag/delete"
        return self.send("get", url, params={"tagid": tagid})


    def update(self):
        pass

    def get(self, tag_id):
        url = "tag/get"
        return self.send("get", url, params={"tagid": tag_id})

    def list(self):
        url = "tag/list"
        return self.send("get",url)
