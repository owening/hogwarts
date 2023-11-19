#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 15:17
# @Author  : Owen
# @File    : plan_service.py
# @Software: PyCharm

from flask_project.dao.plan_dao import PlanDao
from flask_project.model.plan_model import PlanModel
from flask_project.service.testcase_service import TestcaseService
plan_dao = PlanDao()
testcase_service = TestcaseService()


class PlanService:

    def get(self, plan_id):
        '''
        通过 ID 查询测试计划
        '''
        return plan_dao.get(plan_id)

    def get_by_name(self, plan_name):
        '''
        通过名称查询测试计划
        '''
        return plan_dao.get_by_name(plan_name)

    def list(self):
        '''
        返回所有测试计划
        '''
        return plan_dao.list()

    def create(self, plan_model: PlanModel, testcase_id_list):
        '''
        创建测试计划
        '''
        # 创建之前先通过名称查询计划是否已经存在
        plan = self.get_by_name(plan_model.name)
        print(f"名称 {plan_model.name} 的查询结果为 {plan}")
        # 不存在则新增
        if not plan:
            # 根据测试用例 ID 查询获取测试用例对象列表
            testcase_list = [testcase_service.get(testcase_id) for testcase_id in testcase_id_list]
            # 构建测试计划对象
            plan_model.testcases = testcase_list
            # 创建测试计划
            return plan_dao.create(plan_model)
        # 存在则返回 False
        return False

    def delete(self, plan_id):
        # 删除操作
        # 删除之前先查询数据是否存在，存在则进行删除，不存在则返回false
        plan = self.get(plan_id)
        if not plan:
            return False
        else:
            return plan_dao.delete(plan_id)