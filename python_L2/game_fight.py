#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 15:09
# @Author  : Owen
# @File    : game_fight.py
# @Software: PyCharm

# 接下来需要实现添加英雄与英雄对战的功能，
# 需要输入 (input) 英雄的姓名与血量，然后将英雄的信息存放成为一个字典（字典），


dict_one = {}
dict_one["name"] = input("输入第1个英雄姓名：")
dict_one["hp"] = int(input("输入第1个英雄血量："))

dict_two = {}
dict_two["name"] = input("输入第2个英雄姓名：")
dict_two["hp"] = int(input("输入第2个英雄血量："))

# 每个英雄存放成功后，都打印其信息（print）。
print("两个英雄分别是：", dict_one, dict_two)
# 添加完成两个英雄之后，自动开始对打，
# 对打的为多轮制的回合游戏（循环语句），
# 两个英雄的攻击力都为10。

# 方式一
hero_hp = dict_one["hp"]
hero2_hp = dict_two["hp"]
while True:
    # 每一轮血量的变化为:
    # hero_hp = hero_hp - 10 （赋值加运算）
    hero_hp = hero_hp - 10
    hero2_hp = hero2_hp - 10
    # 对打完成之后需要输出（print）赢家（判断）
    if hero_hp <= 0 or hero2_hp <= 0:  # 大于0时继续执行递减
        if hero_hp > hero2_hp:
            print("赢家是：", dict_one["name"])
        elif hero_hp < hero2_hp:
            print("赢家是：", dict_two["name"])
        break
#
#
# 方式二
# while True:
#     # 每一轮血量的变化为:
#     # hero_hp = hero_hp - 10 （赋值加运算）
#     dict_one["hp"]  = dict_one["hp"] - 10
#     dict_two["hp"]  = dict_two["hp"] - 10
#     # 对打完成之后需要输出（print）赢家（判断）
#     if dict_one["hp"] <= 0 or dict_two["hp"] <= 0:
#         if dict_one["hp"] > dict_two["hp"]:
#             print("赢家是：",dict_one["name"])
#         elif dict_one["hp"] < dict_two["hp"]:
#             print("赢家是：", dict_two["name"])
#         break
