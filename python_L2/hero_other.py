#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 14:28
# @Author  : Owen
# @File    : hero_other.py
# @Software: PyCharm
class Hero:

    def __init__(self,name,hp,power):
        #所有属性初始化
        #self.属性  实例属性
        self.name = name
        self.hp = hp
        self.power = power

    def speck_Lines(self,lines):
        print(f"我名字是{self.name},我的血量为{self.hp},{lines}")

    def _get_name(self):
        print(f"我的名字是：{self.name}")

class APCHero(Hero):

    def __init__(self,name,hp,power,mp):
        super().__init__(name,hp,power)
        self.ap = mp

    def speck_Lines(self,lines):
        super(APCHero, self).speck_Lines(lines)

    def put_Skill(self,skill):
        print(f"我要放魔法大招是{skill}！")

class TopHero(Hero):

    def __init__(self,name,hp,power,armor):
        super().__init__(name,hp,power)
        self.armor = armor


# angela = APCHero("安琪拉",55,70,900)
# angela.speck_Lines("欢迎来到魔法世界")
# angela.put_Skill("大雨啦！收衣服啦！")
#
# zhaoyun = TopHero("赵云",70,70,50)
# zhaoyun.speck_Lines("长坂坡上一决高下!")

