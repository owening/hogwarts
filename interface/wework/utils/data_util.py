#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：data_util
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/29 10:28 
'''
import os
import time
import yaml


class DataUtil:

    @classmethod
    def get_root_path(cls):
        """
        获取appium项目绝对路径
        """
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def get_current_day():
        """
        获取当天日期
        """
        return time.strftime("%Y-%m-%d")

    @staticmethod
    def get_current_time():
        """
        获取当前时间
        """
        return time.strftime("%Y-%m-%d-%H-%M-%S")

    @staticmethod
    def get_yaml_data(yaml_path):
        """
        读取传入文件的yaml数据
        """
        yaml_file = os.sep.join([DataUtil.get_root_path(), "datas", yaml_path])
        with open(yaml_file, encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data

    # def get_member_data(self):
    #     """
    #     获取用户列表数据
    #     """
    #     member_data = DataUtil.get_yaml_data("xxx")
    #     return member_data

