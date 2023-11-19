#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 14:14
# @Author  : Owen
# @File    : record_dao.py
# @Software: PyCharm

from flask_project.model.record_model import RecordModel
from flask_project.server import db_session

# Dao 负责和数据库的交互
class RecordDao:

    def list_by_plan_id(self, plan_id):
        # 根据id返回数据
        return db_session.query(RecordModel).filter_by(plan_id=plan_id).all()

    def list(self):
        # 返回所有数据
        return db_session.query(RecordModel).all()

    def create(self, build_do: RecordModel):
        # 新增数据
        db_session.add(build_do)
        db_session.commit()
        return build_do