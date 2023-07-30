#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 16:45
# @Author  : Owen
# @File    : hero_factory.py
# @Software: PyCharm
from L2.hero_other import APCHero, TopHero, Hero


class HeroFactory:

    def create(self,hery_type,*args):

        if hery_type == 'apc':
            return APCHero(*args,)
        elif hery_type == 'top':
            return TopHero(*args)
        else:
            return Hero(*args)

hero_factory = HeroFactory()
yase = hero_factory.create("top","亚瑟",90,80,30)
yase.speck_Lines("亚瑟来了")