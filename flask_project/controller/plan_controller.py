#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 17:40
# @Author  : Owen
# @File    : plan_controller.py
# @Software: PyCharm

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from flask_project.model.plan_model import PlanModel
from flask_project.service.plan_service import PlanService

# 声明蓝图
plan_router = Blueprint(name="plan", import_name=__name__)
plan_service = PlanService()


@plan_router.route("/plan/get")
@jwt_required()
def plan_get():
    """
    计划的查找
    {id: 1}
    :return:
    """
    # 获取请求参数
    id = request.args.get("id")
    # 如果请求参数中存在 id
    if id:
        # 根据 id 查询测试计划
        data = plan_service.get(id)
        # 如果测试计划存在
        if data:
            # 将查询结果返回
            datas = [data.as_dict()]
            return {"code": 0, "msg": "get plan success", "data": datas}
        else:
            # 如果测试计划不存在，返回提示信息
            return {"code": 40004, "msg": "plan is not exists"}
    else:
        # 如果参数中不包含 id，则返回全部测试计划
        datas = [p.as_dict() for p in plan_service.list()]
        return {"code": 0, "msg": "get plans success", "data": datas}

@plan_router.route("/plan/post", methods=["POST"])
@jwt_required()
def plan_post():
    """
    计划的新增
    {
        "name":xxx,
        "testcase_ids":[1,2,3,4],
    }
    :return:
    """
    data = request.json
    # data -> {name=1, testcase_ids=[2,3,4,5,6]}
    testcase_id_list = data.pop("testcase_ids")
    plan = PlanModel(**data)
    # 新增
    plan_id = plan_service.create(plan, testcase_id_list)
    if plan_id:
        # 存在id,则证明新增成功了
        return {"code": 0, "msg": f"add plan success", "data": {"plan_id": plan_id}}
    else:
        return {"code": 40001, "msg": "plan is exists"}


@plan_router.route("/plan/delete", methods=["POST"])
@jwt_required()
def plan_delete():
    """
    测试用例的删除
    {"id": 1}
    :return:
    """
    # 获取请求体
    data = request.json
    # 删除
    plan_id = plan_service.delete(data.get("id"))
    if plan_id:
        # 存在测试用例id,则证明用例修改成功了
        return {"code": 0, "msg": f"plan delete success", "data": {"plan_id": plan_id}}
    else:
        return {"code": 40001, "msg": "delete plan fail"}