#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 15:20
# @Author  : Owen
# @File    : record_service.py
# @Software: PyCharm

from flask_project.dao.record_dao import RecordDao
from flask_project.model.record_model import RecordModel
from flask_project.service.plan_service import PlanService
from flask_project.utils.jenkins_utils import JenkinsUtils

record_dao = RecordDao()
plan_service = PlanService()


class RecordService:

    def list_by_plan(self, plan_id):
        '''
        根据测试计划 ID 获取对应的测试记录
        '''
        return record_dao.list_by_plan_id(plan_id)

    def list(self):
        '''
        获取所有执行记录
        '''
        return record_dao.list()

    def create(self, plan_id):
        '''
        新增测试记录
        '''
        # 新增之前先查询要执行的测试计划是否存在
        plan = plan_service.get(plan_id)
        # 不存在则返回 False
        if not plan:
            return False
        # 存在则创建测试记录
        else:
            # 执行命令格式
            # pytest test_demo1 test_demo2 test_demo3
            # 获取测试记录中包含的测试用例的执行方式
            method_list = [testcase.method for testcase in plan.testcases]
            # 为测试执行方式列表去重
            methods = set(method_list)
            print(f"去重后的 method 列表为 {methods}")
            # 获取测试记录中包含的测试用例 step 中包含的 nodeid
            # test_demo1 ==> test_add_params.py
            nodeid_list = [testcase.step for testcase in plan.testcases]
            nodeid = " ".join(nodeid_list)
            print(f"获取到的用例 id 列表为 {nodeid}")
            # 执行测试用例
            invoke_params = {
                "methods": methods,
                "steps": nodeid
            }
            report = JenkinsUtils.invoke(invoke_params)
            # 构造测试记录对象
            record_model = RecordModel(plan_id=plan_id, report=report)
            # 新增测试记录
            return record_dao.create(record_model)