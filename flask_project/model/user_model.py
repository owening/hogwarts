#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 10:57
# @Author  : Owen
# @File    : user_model.py
# @Software: PyCharm


from datetime import datetime
from passlib.handlers.sha2_crypt import sha256_crypt
from sqlalchemy import Column, Integer, String, DateTime
from flask_project.server import Base

# 创建用户表

class UserModel(Base):
    __tablename__ = "user"

    # 用户 ID, 用户的唯 一标识
    id = Column(Integer, primary_key=True)
    # 用户名, 限定 80个字符 ，不为空，并且唯一
    username = Column(String(80), nullable=False, unique=True)
    # 密码
    password = Column(String(500), nullable=False)
    # 创建时间,不需要手动传入，在写入记录的时候自动生成
    create_time = Column(DateTime, nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __init__(self, *args, **kwargs):
        # 密码进行自动加密
        self.username = kwargs.get('username')
        self.password = sha256_crypt.hash(kwargs.get('password'))

    def check_hash_password(self, raw_password):
        '''
        校验密码
        :param raw_password: 传入的密码
        :return: 校验结果 True or False
        '''
        return sha256_crypt.verify(raw_password, self.password)

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "create_time": str(self.create_time)
        }