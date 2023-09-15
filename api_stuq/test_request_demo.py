#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_request_demo
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/11 16:34 
'''
import requests


def test_get():
    params = {
        "name": "nali",
        "age": 22,
        "Are you OK ?": False
    }
    res1 = requests.get(url="https://httpbin.ceshiren.com/get", params=params, verify=False)
    res2 = requests.get(url="https://ceshiren.com/search?expanded=true&q=requests", verify=False)

    print("\n", res1.json())
    print("\n", res2.text)


def test_post():
    params = {
        "name": "nali",
        "age": 22,
        "Are you OK ?": False
    }
    res1 = requests.post(url="https://httpbin.ceshiren.com/post", params=params, verify=False)
    res2 = requests.post(url="https://httpbin.ceshiren.com/post", data=params, verify=False)
    print(res1.json())
    print(res2.json())


def test_req():
    req_headers = {
        "Content-type": "appliction/json",
        "user-agent": "Owen-tools",
        "cookie": "owen-test",
        "Authorization": "666Authorization888"

    }
    data = {
        "name": "Owen",
        "age": 18,
        "Are you OK ?": True
    }
    res = requests.request(method="post", url="https://httpbin.ceshiren.com/post", json=data, headers=req_headers,
                           verify=False)

    print(res.json())
    assert res.status_code == 200
    assert res.json()["json"]["name"] == "Owen"







