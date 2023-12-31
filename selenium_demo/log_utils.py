#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：log_until
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/4 17:37 
'''

# 日志配置
import logging
# 创建logger实例
logger = logging.getLogger('simple_example')
# 设置日志级别
logger.setLevel(logging.DEBUG)
# 流处理器
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 日志打印格式
formatter = logging.Formatter\
('%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)')
# 添加格式配置
ch.setFormatter(formatter)

# 添加日志配置
logger.addHandler(ch)


# logging.basicConfig(
#     filename='myapp.logs',
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)',
#     datefmt='%m/%d/%Y %I:%M:%S %p')
