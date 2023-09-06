#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/27 15:30
# @Author  : Owen
# @File    : log_util.py
# @Software: PyCharm

import logging
import os
from logging.handlers import RotatingFileHandler
from appium_demo.utils.data_util import DataUtil

# 绑定绑定句柄到logger对象
logger = logging.getLogger(__name__)

# 拼接当前要输出日志的路径
log_dir_path = os.sep.join([DataUtil.get_root_path(), "/logs"])

# 当文件目录不存在时，则创建一个文件目录
if not os.path.isdir(log_dir_path):
    os.mkdir(log_dir_path)

# 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限,backupCount日志文件数据上限
file_log_handler = RotatingFileHandler(os.sep.join([log_dir_path, f'{DataUtil.get_current_day()}.log']),
                                       maxBytes=1024 * 1024, backupCount=10, encoding="utf-8")
# 设置日志的格式
date_string = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] [%(filename)s]/[line: %(lineno)d]/[%(funcName)s] %(message)s ', date_string)

# 日志输出到控制台的句柄
stream_handler = logging.StreamHandler()

# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 为全局的日志工具对象添加日志记录器
# 绑定绑定句柄到logger对象
logger.addHandler(stream_handler)
logger.addHandler(file_log_handler)

# 设置日志输出级别
logger.setLevel(level=logging.INFO)
