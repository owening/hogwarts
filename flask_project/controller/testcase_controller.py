#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 17:38
# @Author  : Owen
# @File    : testcase_controller.py
# @Software: PyCharm

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from flask_project.model.testcase_model import TestcaseModel
from flask_project.service.testcase_service import TestcaseService

# 声明蓝图
testcase_router = Blueprint(name="testcase", import_name=__name__)
testcase_service = TestcaseService()


@testcase_router.route("/testcase/get")
@jwt_required()
def testcase_get():
    """
    测试用例的查找
    {id: 1}
    :return:
    """
    # 获取请求参数
    data = request.args
    case_id = data.get("id")
    # 如果有id则进行数据查找
    if case_id:
        testcase = testcase_service.get(int(case_id))
        # 如果查询到结果
        if testcase:
            datas = [testcase.as_dict()]
            return {"code": 0, "msg": "get data success", "data": datas}
        else:
            # 如果没有数据，则返回数据已存在
            return {"code": 40004, "msg": "data is not exists"}
    else:
        # 如果没有id,则返回全部数据
        datas = [testcase.as_dict() for testcase in testcase_service.list()]
        return {"code": 0, "msg": "get data success", "data": datas}

@testcase_router.route("/testcase/post", methods=["POST"])
@jwt_required()
def testcase_post():
    """
    测试用例的新增
    {
        "name":xxx,
        "step":xxx,
        "method":xxx,
        "remark":xxx,
    }
    :return:
    """
    # 获取请求体
    data = request.json
    # 构造测试用例对象
    testcase = TestcaseModel(**data)
    # 新增用例
    case_id = testcase_service.create(testcase)
    if case_id:
        # 存在测试用例id, 则证明用例新增成功了
        return {"code": 0, "msg": "add testcase success", "data": {"testcase_id": case_id}}
    else:
        return {"code": 40001, "msg": "testcase is exists"}


@testcase_router.route("/testcase/put", methods=["POST"])
@jwt_required()
def testcase_put():
    """
    测试用例的修改
    {
        "id":xxx,
        "name":xxx,
        "step":xxx,
        "method":xxx,
        "remark":xxx,
    }
    :return:
    """
    # 获取请求体
    data = request.json
    # 构造测试用例对象
    testcase = TestcaseModel(**data)
    # 修改测试用例
    case_id = testcase_service.update(testcase)
    if case_id:
        # 存在测试用例id, 则证明用例新增成功了
        return {"code": 0, "msg": "update testcase success", "data": {"testcase_id": case_id}}
    else:
        return {"code": 40001, "msg": "update testcas fail"}


@testcase_router.route("/testcase/delete", methods=["POST"])
@jwt_required()
def testcase_delete():
    """
    测试用例的删除
    {"id": 1}
    :return:
    """
    # 获取请求体
    data = request.json
    delete_case_id = data.get("id")
    if delete_case_id:
        case_id = testcase_service.delete(delete_case_id)
        if case_id:
            # 存在测试用例id,则证明用例修改成功了
            return {"code": 0, "msg": f"delete testcase success", "data": {"testcase_id": case_id}}
        else:
            return {"code": 40001, "msg": "delete case fail"}
