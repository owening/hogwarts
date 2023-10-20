#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：sequential_search
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/10/19 15:00 
'''

"""
顺序查找
"""

def sequential_search(num_list, target_num):
    for i in range(len(num_list)):
        print(i)
        if num_list[i] == target_num:
            return i
    return -1


def test_sequential_search():
    # target_num = 9
    # num_list = [5,8,3,7,0,1,9,6,6]
    assert sequential_search([5, 8, 3, 7, 0, 1, 9, 6, 6], 6) == 7
