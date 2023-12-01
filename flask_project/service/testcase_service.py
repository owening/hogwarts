#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 15:15
# @Author  : Owen
# @File    : testcase_service.py
# @Software: PyCharm

from typing import List

from flask_jwt_extended import get_jwt_identity

from flask_project.dao.testcase_dao import TestcaseDao
from flask_project.model.testcase_model import TestcaseModel
testcase_dao = TestcaseDao()


class TestcaseService:
    def create(self, testcase_model: TestcaseModel) -> int:
        """
        创建用例
        """
        # 获取登录token对应用户名
        username = get_jwt_identity().get("username")
        result = testcase_dao.get_by_name(testcase_model.name)
        if not result:
            testcase_model.update_by = username
            return testcase_dao.create(testcase_model)

    def update(self, testcase_model: TestcaseModel) -> int:
        """
        更新用例
        """
        # if testcase_dao.get_by_name(testcase_model.name):
        if testcase_dao.get_by_id(testcase_model.id):
            testcase_dao.update(testcase_model)
        return testcase_model.id

    def delete(self, testcase_id: int) -> int:
        """
        删除用例
        """
        if self.get(testcase_id):
            return testcase_dao.delete(testcase_id)

    def list(self) -> List[TestcaseModel]:
        """
        获取全部用例
        """
        return testcase_dao.list()

    def get(self, testcase_id: int) -> TestcaseModel:
        """
        获取某个测试用例
        """
        return testcase_dao.get_by_id(testcase_id)

    def get_by_name(self, testcase_name: int) -> TestcaseModel:
        """
        通过name获取用例
        """
        return testcase_dao.get_by_name(testcase_name)