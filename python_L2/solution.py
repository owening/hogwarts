#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：solution
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/30 10:57 
'''
from typing import List

#
# def merge(nums1, m, nums2, n):
#
#     """
#     :type nums1: List[int]
#     :type m: int
#     :type nums2: List[int]
#     :type n: int
#     :rtype: None Do not return anything, modify nums1 in-place instead.
#     """
#     # length = m + n
#     # if len(nums1) == length:
#
#     # remove_list = []
#     # for i in nums1:
#     #     if i <= 0:
#     #         remove_list.append(i)
#     # print(remove_list)
#     # for e in remove_list:
#     #     nums1.remove(e)
#     #
#     # print(nums1)
#     # nums1 = nums1 + nums2
#     # nums1.sort()
#     # print(nums1)
#
#     nums1[m:] = nums2
#     nums1.sort()
#     print(nums1)
#
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
#
# nums2 = [2, 5, 6]
# n = 3
#
# merge(nums1, m, nums2, n)

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""



def two_sum(nums, target):
    # 创建一个空字典，用于记录数字与其索引的映射关系
    num_dict = {}

    # 遍历整数数组
    for i in range(len(nums)):
        # 计算当前数字与目标值的差值
        complement = target - nums[i]

        # 检查差值是否在字典中
        if complement in num_dict:
            # 返回满足条件的两个数字的索引
            return [num_dict[complement], i]

        # 将当前数字作为键，索引作为值存入字典
        num_dict[nums[i]] = i

    # 如果没有找到满足条件的两个数字，则返回空列表
    return []


# 示例使用
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # 输出：[0, 1]