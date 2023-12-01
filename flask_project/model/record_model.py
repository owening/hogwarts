#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 11:11
# @Author  : Owen
# @File    : record_model.py
# @Software: PyCharm

from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from flask_project.model.plan_model import PlanModel
from flask_project.server import Base


# 创建构建记录表
class RecordModel(Base):
    __tablename__ = "record"

    # 在新系统下，使用带有显式注释的Mypy插件而在注释中不使用Mapped的SQLAlchemy应用程序会出现错误，
    # 因为在使用relationship（）等结构时，这些注释会被标记为错误。
    # 将__allow_unmapped__添加到显式类型的ORM模型一节说明了如何暂时禁止为使用显式注释的遗留ORM模型引发这些错误。
    __allow_unmapped__ = True

    # 执行记录 ID
    id = Column(Integer, primary_key=True)
    # 测试计划 ID
    plan_id = Column(Integer, ForeignKey('plan.id', ondelete='CASCADE'))
    # 测试报告
    report = Column(String(80), nullable=False, unique=True)
    # 执行时间
    create_time = Column(DateTime, nullable=True, default=datetime.utcnow)

    # 参数1： 关联的另外一个业务表类名， 参数2： 反射别名
    plan: PlanModel = relationship("PlanModel", backref="record")

    def __repr__(self):
        # 数据库的 魔法方法 直观展示数据
        '''[<User "xxxx">,<User "yyyy">]'''
        return '<Record %r>' % self.id

    def as_dict(self):
        return {
            "id": self.id,
            "plan_id": self.plan_id,
            "report": self.report,
            "create_time": str(self.create_time)
        }