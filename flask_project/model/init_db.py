#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 11:11
# @Author  : Owen
# @File    : init_db.py
# @Software: PyCharm

from flask_project.server import Base, engine
from flask_project.model.testcase_model import TestcaseModel
from flask_project.model.plan_model import PlanModel
from flask_project.model.record_model import RecordModel
from flask_project.model.user_model import UserModel

if __name__ == '__main__':
    # 删除所有数据
    # Base.metadata.drop_all(bind=engine)
    # 创建表，需要传入创建连接的对象
    Base.metadata.create_all(bind=engine)