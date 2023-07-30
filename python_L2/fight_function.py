#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 16:52
# @Author  : Owen
# @File    : fight_function.py
# @Software: PyCharm


# dict_one = {}
# dict_one["name"]=input("输入第1个英雄姓名：")
# dict_one["hp"]=int(input("输入第1个英雄血量："))
#
# dict_two = {}
# dict_two["name"]=input("输入第2个英雄姓名：")
# dict_two["hp"]=int(input("输入第2个英雄血量："))

# 每个英雄存放成功后，都打印其信息（print）。
# print("两个英雄分别是：",dict_one,dict_two)
# 添加完成两个英雄之后，自动开始对打，
# 对打的为多轮制的回合游戏（循环语句），
# 两个英雄的攻击力都为10。


def fight(dict_one, dict_two):
    """
    :param dict_one:  第一个英雄信息，包含姓名和血量
    :param dict_two:   第二个英雄信息，包含姓名和血量
    :return:  赢家英雄姓名
    """
    hero_hp = dict_one["hp"]
    hero2_hp = dict_two["hp"]
    while True:
        hero_hp = hero_hp - 10
        hero2_hp = hero2_hp - 10
        if hero_hp <= 0 or hero2_hp <= 0:
            if hero_hp > hero2_hp:
                return dict_one["name"]
            elif hero_hp < hero2_hp:
                return dict_two["name"]
            else:
                return "平局"
