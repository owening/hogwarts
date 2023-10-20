#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：insure_no_generate
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/9/25 14:08 
'''

insure_no = 663315276454400001


def insure_no_generate(insure_no):
    for i in range(5000):
        insure_num =str(insure_no + i)
        with open("insure_no.txt", "a", encoding="utf-8") as f:
            f.write(insure_num+"\n")


insure_no_generate(insure_no)
