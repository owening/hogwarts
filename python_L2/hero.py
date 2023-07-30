#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 10:42
# @Author  : Owen
# @File    : oop_fight.py
# @Software: PyCharm

class Hero:

    def __init__(self,name,hp,power):
        #所有属性初始化
        #self.属性  实例属性
        self.name = name
        self._hp = hp
        self.power = power

    def speck_Lines(self,lines):
        print(f"我名字是{self.name},我的血量为{self._hp},{lines}")
        # self._get_name()

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

dmxy = Hero("德玛西亚",80,60)
hy = Hero("后羿",50,90)
bq = Hero("白起",60,99)

dmxy.speck_Lines("德玛西亚即将崛起！")
hy.speck_Lines("百步穿杨！一击即中！")
bq.speck_Lines("有死无生，大杀四方！")

Angela = APCHero("安琪拉",55,70,900)
Angela.speck_Lines("欢迎来到魔法世界")
Angela.put_Skill()

zhaoyun = TopHero("赵云",70,70,50)
zhaoyun.speck_Lines("长坂坡上一决高下！")




