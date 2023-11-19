#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 17:43
# @Author  : Owen
# @File    : record_controller.py
# @Software: PyCharm

from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_project.service.record_service import RecordService

# 声明蓝图
record_router = Blueprint(name="record", import_name=__name__)
record_service = RecordService()


@record_router.route("/record/get")
@jwt_required()
def record_get():
    """
    记录的查找
    {id: 1}
    :return:
    """
    # 获取请求参数
    plan_id = request.args.get("plan_id")
    if plan_id:
        # 如有有id则进行数据查找
        data = record_service.list_by_plan(plan_id)
        if data:
            # 如果查到数据，则返回给前端
            datas = [_.as_dict() for _ in data]
            return {"code": 0, "msg": "get record success", "data": datas}
        else:
            # 如果没有数据，则返回数据已存在
            return {"code": 40004, "msg": "record is not exists"}
    else:
        # 如果没有id,则返回全部数据
        datas = [build.as_dict() for build in record_service.list()]
        return {"code": 0, "msg": "get records success", "data": datas}


@record_router.route("/record/post", methods=["POST"])
@jwt_required()
def record_post():
    """
    记录的新增
    {
        "plan_id":xxx,
    }
    :return:
    """
    data = request.json
    # 新增
    record_id = record_service.create(data.get("plan_id")).id
    if record_id:
        # 存在id,则证明新增成功了
        return {"code": 0, "msg": f"record add success", "data": {"record_id": record_id}}
    else:
        return {"code": 40001, "msg": "record is exists"}
