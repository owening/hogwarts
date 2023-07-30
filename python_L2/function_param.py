#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 16:08
# @Author  : Owen
# @File    : function_param.py
# @Software: PyCharm

def function_demo(name,age,hp,*args,**kwargs):
    print("元组参数：",args)
    print(f"我的名字是：{name},年龄是{age},血量为{hp}")
    print("字典参数：", kwargs)

function_demo(23,'赵云',33,"testing",886,power=120,mp=66900,ss='dage')