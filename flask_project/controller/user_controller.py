#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 17:36
# @Author  : Owen
# @File    : user_controller.py
# @Software: PyCharm

from flask import Blueprint, request
from flask_project.model.user_model import UserModel
from flask_project.service.user_service import UserService

user_router = Blueprint(name="user", import_name=__name__)
user_service = UserService()


@user_router.route("/user/register", methods=["POST"])
def user_register():
    """
    用户的注册
    {
        "username":xxx,
        "password":xxx,
    }
    :return:
    """
    # 获取请求体
    data = request.json
    # 构建用户对象
    user = UserModel(**data)
    print(user.password)
    if user:
        user_id = user_service.create(user)
        if user_id:
            # 存在id,则证明新增成功了
            return {"code": 0, "msg": f"register success"}
        else:
            return {"code": 40001, "msg": "register fail"}
    return {"code": 40001, "msg": "register fail"}


@user_router.route("/user/login", methods=["POST"])
def user_login():
    """
    用户的登录
    {
        "username":xxx,
        "password":xxx,
    }
    :return:
    """
    # 获取请求体
    data = request.json
    # 构建用户对象
    user = UserModel(**data)
    # 通过用户名查找用户是否存在
    user_result = user_service.get_by_name(user.username)
    print(user_result)
    print(data.get("password"))
    # 如果用户不存在，说明用户还未注册
    if not user_result:
        return {"code": 40013, "msg": "user is not register"}
    # 如果密码不匹配，说明密码错误
    if not user_result.check_hash_password(data.get("password")):
        return {"code": 40014, "msg": "password is wrong"}
    # 用户存在，且密码匹配，则生成 token
    access_token = user_service.create_access_token(user_result)
    print(access_token)
    if access_token:
        # 存在access_token,则证明登录成功了
        return {"code": 0, "msg": "login success", "data": {"token": access_token}}
    else:
        return {"code": 40021, "msg": "login fail"}


@user_router.route("/user/get")
def user_list():
    """
    获取所有用户数据
    :return:
    """
    # 获取请求参数
    data = user_service.list()
    if data:
        # 如果查到数据，则返回给前端
        datas = [_.as_dict() for _ in data]
        return {"code": 0, "msg": "get userinfo success", "data": datas}
    else:
        # 如果没有数据，则返回数据已存在
        return {"code": 40001, "msg": "userinfo is not exists"}
