#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 14:12
# @Author  : Owen
# @File    : user_dao.py
# @Software: PyCharm

from flask_project.model.user_model import UserModel
from flask_project.server import DBSession as db_session

# Dao 负责和数据库的交互
class UserDao:

    def get(self, user_id) -> UserModel:
        '''
        根据 ID 查询用户
        '''
        return db_session.query(UserModel).filter_by(id=user_id).first()

    def list(self) -> UserModel:
        '''
        查询所有
        '''
        return db_session.query(UserModel).all()

    def get_by_name(self, user_name) -> UserModel:
        '''
        根据姓名查询用户
        '''
        return db_session.query(UserModel).filter_by(username=user_name).first()

    def create(self, user_model: UserModel):
        '''
        创建用户
        '''
        db_session.add(user_model)
        db_session.commit()
        return user_model.id
