#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 10:32
# @Author  : Owen
# @File    : oop_base.py
# @Software: PyCharm

class Teacher:

    def __init__(self,name,age,shop):
        """
        构造方法
        """
        self.name = name
        self.age = age
        self.shop= shop

    def talk(self):
        print(f"讲师{self.name}可以讲课，他的年龄是{self.age},他喜欢穿{self.shop}上课")



tang_teacher = Teacher("汤达人",28,"马丁靴")
tang_teacher.talk()
