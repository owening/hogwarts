#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：tag_api
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/19 10:09 
'''
from api_stuq.api_L4.api.wework_api import WeWorkAPI


class TagAPI(WeWorkAPI):

    def create(self, tag_info):
        url = "tag/create"
        return self.send("post", url, json=tag_info)

    def get_tag_user(self, tag_id):
        url = "tag/get"
        return self.send("get", url, params={"tagid":tag_id})

    def list(self):
        url = "tag/list"
        return self.send("get", url)

    def update(self, tag_info):
        url = "tag/update"
        return self.send("post", url, json=tag_info)

    def delete(self, tag_id):
        url = "tag/delete"
        return self.send("get", url, params={"tagid":tag_id})



