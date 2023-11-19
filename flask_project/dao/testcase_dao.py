#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 14:14
# @Author  : Owen
# @File    : testcase_dao.py
# @Software: PyCharm
from flask_project.model.testcase_model import TestcaseModel
from flask_project.server import db_session
# Dao 负责和数据库的交互
class TestcaseDao:

    def get(self, testcase_id: int) -> TestcaseModel:
        """
        添加用例
        :param testcase_id: 用例id
        :return: TestcaseModel
        """
        return db_session.query(TestcaseModel).filter_by(id=testcase_id).first()

    def get_by_name(self, testcase_name: str) -> TestcaseModel:
        """
        根据测试用例名称查询
        """
        return db_session.query(TestcaseModel).filter_by(name=testcase_name).first()

    def list(self):
        """
        获取用例列表
        :return:
        """
        return db_session.query(TestcaseModel).all()

    def create(self, testcase_model: TestcaseModel) -> int:
        """
        创建用例
        :param testcase_model: testcase对象
        :return:
        """
        db_session.add(testcase_model)
        db_session.commit()
        return testcase_model.id

    def delete(self, testcase_id: int) -> int:
        """
        删除用例
        :param testcase_id: 用例id
        :return:
        """
        db_session.query(TestcaseModel).filter_by(id=testcase_id).delete()
        db_session.commit()
        return testcase_id

    def update(self, testcase_model: TestcaseModel) -> int:
        """
        更新用例
        :param testcase_model: testcase对象
        :param testcase_id: 用例id
        :return:
        """
        db_session.query(TestcaseModel).filter_by(id=testcase_model.id).update(testcase_model.as_dict())
        db_session.commit()
        return testcase_model.id