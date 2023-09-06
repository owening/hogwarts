#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：conftest
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/29 17:18 
'''
import os.path

import pytest
import yaml

from appium_demo.utils.data_util import DataUtil
from appium_demo.utils.log_util import logger


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    fail_case_info = []

    # 错误类型
    error_type = None
    # 错误信息
    error_msg = None

    # 错误完整信息
    error_longrepr = None

    # 如果用例执行不通过
    if report.outcome != "passed":
        # 如果运行时有相应的错误日志则捕获日志，赋值到一个变量中
        logger.info(call.excinfo)
        if call.excinfo:
            error_type = call.excinfo.typename
            error_msg = call.excinfo.value
            error_longrepr = str(out.result.longrepr)

        case_info = {
            "nodeid": report.nodeid,
            "result": report.outcome,
            "type": error_type,
            "msg": error_msg,
            "longrepr": error_longrepr
        }
        fail_case_info.append(case_info)

        error_path = DataUtil.get_root_path() + "/fail_record"

        if not os.path.isdir(error_path):
            os.mkdir(error_path)

        # 用例信息写入 yaml 文件
        with open(error_path + "/fail_case_info.yaml", "a", encoding="utf-8") as f:
            yaml.dump(fail_case_info, f, allow_unicode=True)

        logger.error(f'错误类型 =>> {error_type}，\n'
                     f'错误信息 =>> {error_msg}，\n'
                     f'错误详情 =>> {error_longrepr} \n')
