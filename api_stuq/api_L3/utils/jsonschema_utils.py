#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：jsonschema_utils
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/18 15:14 
'''
import json

from genson import SchemaBuilder
from jsonschema.validators import validate

from api_stuq.api_L3.utils.log_util import logger


class JSONSchemaUtils:

    @classmethod
    def generate_schema(cls, obj):
        """
        生成jsonschema
        """
        builder = SchemaBuilder()
        builder.add_object(obj)
        return builder.to_schema()

    @classmethod
    def generate_schema_to_file(cls, obj, file_path):
        """
        将生成jsonschema数据写入文件
        """
        schema_res = cls.generate_schema(obj)
        with open(file_path, "w") as f:
            json.dump(schema_res, f)

    @classmethod
    def validate_schema(cls, obj, expr_schema):
        """
        通过schema校验数据结构和类型
        """
        try:
            validate(obj, expr_schema)
            return True
        except Exception as e:
            logger.error(f"结构体校验失败，原因为：{e}")
            return False

    @classmethod
    def validate_schema_by_file(cls, obj, schema_file):
        """
        读取文件中schema数据，校验传入obj数据结构
        """
        with open(schema_file) as f:
            expr_schema = json.load(f)
            return cls.validate_schema(obj, expr_schema)
