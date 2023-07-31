#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/30 17:13
# @Author  : Owen
# @File    : load_yaml.py
# @Software: PyCharm
import yaml


def load_yaml():
    datas = yaml.safe_load(open("data.yaml",encoding="utf-8"))
    return datas


print(load_yaml())