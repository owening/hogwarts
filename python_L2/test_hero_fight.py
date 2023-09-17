#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 15:30
# @Author  : Owen
# @File    : test_hero_fight.py
from unittest import TestCase


# @Software: PyCharm



from python_L2.hero_fight import fight
from python_L2.hero_other import APCHero, TopHero


class Test(TestCase):

    def test_fight(self):
        angela = APCHero("安琪拉", 55, 70, 900)
        zhaoyun = TopHero("赵云", 70, 70, 50)
        re = fight(angela,zhaoyun)
        assert re == '赵云'


    def test_fight2(self):
        angela = APCHero("安琪拉", 70, 70, 900)
        zhaoyun = TopHero("赵云", 70, 70, 50)
        re = fight(angela,zhaoyun)
        assert re == '平局'



