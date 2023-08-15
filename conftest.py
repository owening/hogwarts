#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/30 15:39
# @Author  : Owen
# @File    : conftest.py
# @Software: PyCharm
from _pytest.config import Config
from _pytest.config.argparsing import Parser

global_env = {}

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name=i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_addoption(parser: Parser):
    mygroup = parser.getgroup("owen")
    mygroup.addoption("--browser", default="Chrome", dest="browser", help="选择需要使用的浏览器")

def pytest_configure(config:Config):
    browser = config.getoption("browser", default="Chrome")
    browser_conf = {"browser":browser}
    global_env.update(browser_conf)