#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 16:59
# @Author  : Owen
# @File    : test_fight_function.py
# @Software: PyCharm
from L2.fight_function import fight


def test_fight():
    dict_one = {"name":"ez","hp":70}
    dict_two = {"name":"jinx","hp":50}
    assert fight(dict_one,dict_two) == "ez"

