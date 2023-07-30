# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 15:27
# @Author  : Owen
# @File    : hero_fight.py
# @Software: PyCharm
from L2.hero_other import Hero


def fight(hero1: Hero, hero2: Hero):
    """
       :param hero1: 第一个英雄的信息， 包含血量和姓名
       :param hero2: 第二个英雄的信息， 包含血量和姓名
       :return: 最后赢家的姓名
   """
    hero1_hp = hero1.hp
    hero2_hp = hero2.hp
    hero1_power = hero1.power
    hero2_power = hero2.power
    hero1_name = hero1.name
    hero2_name = hero2.name
    hero1.speck_Lines("欢迎来到魔法世界")
    hero2.speck_Lines("长坂坡上一决高下!")
    while True:
        hero1_hp = hero1_hp - hero2_power
        hero2_hp = hero2_hp - hero1_power
        # 当第一个英雄的血量小于0 或 当第二个英雄的血量小于0
        if hero1_hp <= 0 or hero2_hp <= 0:
            if hero1_hp > hero2_hp:
                # 字面量插值 - 字符串
                print(f"英雄{hero1_name}赢了")
                return hero1_name
            elif hero1_hp < hero2_hp:
                print("英雄赢了", hero2_name)
                return hero2_name
            else:
                print("平局")
                return "平局"
