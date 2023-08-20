#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/18 21:11
# @Author  : Owen
# @File    : conftest.py
# @Software: PyCharm
import os
import time



# pytest 可以直接获取 rootdir 路径
import pytest


def get_rootdir(request):
    # 根目录
    rootdir = request.config.rootdir
    return rootdir


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_name = './log/' + now + '.logs'
    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(os.path.join(get_rootdir(request), log_name))