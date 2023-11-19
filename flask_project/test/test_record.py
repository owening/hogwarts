#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 17:08
# @Author  : Owen
# @File    : test_record.py
# @Software: PyCharm

from flask_project.service.record_service import RecordService

record_service = RecordService()

def test_add():
    id = record_service.create(1)
    assert id
    print(id.as_dict())