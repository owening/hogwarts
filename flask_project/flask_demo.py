#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/18 15:14
# @Author  : Owen
# @File    : flask_demo.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "我是一个Flask_Demo"

@app.route("/home")
def home():
    return "这是是Home"

if __name__ == '__main__':
    app.run()


