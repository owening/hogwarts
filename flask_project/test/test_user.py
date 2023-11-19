#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 16:23
# @Author  : Owen
# @File    : test_user.py
# @Software: PyCharm

from flask_project.model.user_model import UserModel
from flask_project.service.user_service import UserService

user1 = UserModel(username='owen001', password='admin123')
user2 = UserModel(username='owen002', password='admin456')
user3 = UserModel(username='owen003', password='admin789')
user_service = UserService()

def test_register():
    id = user_service.create(user3)
    assert id
    print(id)

def test_token():
    token = user_service.create_access_token(user3)
    assert token
    print(token)