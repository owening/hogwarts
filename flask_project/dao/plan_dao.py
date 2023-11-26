#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 14:14
# @Author  : Owen
# @File    : plan_dao.py
# @Software: PyCharm

from flask_project.model.plan_model import PlanModel
from flask_project.server import DBSession as db_session
# Dao 负责和数据库的交互
class PlanDao:

    def get(self, plan_id) -> PlanModel:
        # 根据id返回数据
        return db_session.query(PlanModel).filter_by(id=plan_id).first()

    def get_by_name(self, name) -> PlanModel:
        # 根据name返回数据
        return db_session.query(PlanModel).filter_by(name=name).first()

    def list(self):
        # 返回所有数据
        return db_session.query(PlanModel).all()

    def create(self, plan_do: PlanModel):
        # 新增数据
        db_session.add(plan_do)
        db_session.commit()
        return plan_do.id

    def delete(self, plan_id):
        # 删除操作
        db_session.query(PlanModel).filter_by(id=plan_id).delete()
        db_session.commit()
        return plan_id