#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 16:29
# @Author  : Owen
# @File    : test_testcase.py
# @Software: PyCharm

from flask_project.model.testcase_model import TestcaseModel
from flask_project.service.testcase_service import TestcaseService

testcase1 = TestcaseModel(name='case001', step='step1', method='pytest', remark='第一个测试用例')
testcase2 = TestcaseModel(name='case002', step='step2', method='pytest', remark='第二个测试用例')
testcase3 = TestcaseModel(id=3, name='case002', step='step22测试', method='method22', remark='测试更新')

testcase4 = TestcaseModel(name='case003', step='step33', method='pytest', remark='第三个测试用例')
testcase_service = TestcaseService()

def test_add():
    id = testcase_service.create(testcase4)
    assert id
    print(id)


def test_get():
    testcase = testcase_service.get_by_name('case001').as_dict()
    testcases = testcase_service.list()
    print(testcase)
    print([testcase.as_dict() for testcase in testcases])


def test_update():
    testcase = testcase_service.update(testcase3)
    print(testcase)

def test_delete():
    testcase = testcase_service.delete(4)
    print(testcase)