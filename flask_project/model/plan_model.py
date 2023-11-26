#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 11:09
# @Author  : Owen
# @File    : plan_model.py
# @Software: PyCharm
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from flask_project.model.testcase_plan_rel import testcase_plan_rel
from flask_project.server import Base


# 创建测试计划表



class PlanModel(Base):

    __tablename__ = "plan"

    # 测试计划 ID
    id = Column(Integer, primary_key=True)
    # 测试计划名称
    name = Column(String(80), nullable=False, unique=True)
    # 测试用例列表
    testcases = relationship("TestcaseModel", secondary=testcase_plan_rel, backref='plan')
    # 创建时间
    create_time = Column(DateTime, nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __repr__(self):
        # 数据库的 魔法方法 直观展示数据
        '''[<User "xxxx">,<User "yyyy">]'''
        return '<Plan %r>' % self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "testcases": [testcase.as_dict() for testcase in self.testcases],
            "create_time": str(self.create_time)
        }