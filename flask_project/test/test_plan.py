#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 16:45
# @Author  : Owen
# @File    : test_plan.py
# @Software: PyCharm
from flask_project.model.plan_model import PlanModel
from flask_project.service.plan_service import PlanService

plan1 = PlanModel(name='test_plan001')
plan2 = PlanModel(name='test_plan002')
plan_service = PlanService()

def test_add():
    id = plan_service.create(plan2, [1, 3])
    assert id
    print(id)


def test_get():
    plan = plan_service.get_by_name('test_plan001').as_dict()
    plans = plan_service.list()
    print(plan)
    print([plan.as_dict() for plan in plans])


def test_delete():
    plan = plan_service.delete(2)
    print(plan)