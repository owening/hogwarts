#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：binary_search
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/10/19 15:00 
'''

"""
二分法查找：实现思路
确定查找范围。
获取中间元素。
如果猜的数字小了，就修改最小值。
如果猜的数字大了，就修改最大值。
如果猜中了，则返回下标。
重复以上的过程直到找到目标元素或确定目标元素不存在于数组中。
"""


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def test_binary_search():
    assert binary_search([2, 4, 6, 7, 8, 9, ], 2) == 0
