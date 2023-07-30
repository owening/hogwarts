#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 17:55
# @Author  : Owen
# @File    : decorator_demo.py
# @Software: PyCharm
import datetime
from time import sleep

def param(decorate_param):

    def timer(func):
        def inner():
            start_time = datetime.datetime.now()
            if decorate_param == True:
                print("开始执行")
                print("装饰器传惨为：",decorate_param)
                func()
                end_time = datetime.datetime.now()
                run_time = end_time - start_time
                print("执行结束,执行的时长为：", run_time)
            else:
                return func()
        return inner
    return timer


@param(False)
def run_function():
    # sleep()
    print("执行方法啦ing")


run_function()
