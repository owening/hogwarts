#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/30 11:05
# @Author  : Owen
# @File    : hero_management.py
# @Software: PyCharm
class HeroManagement:
    def __init__(self):
        self.hero_list = []

    def update_hero(self, hero_name, hero_volume):

        for i in self.hero_list:
            if i.get("name") == hero_name:
                i["volume"] = hero_volume
                return i
        return False

    def delete_hero(self, hero_name):
        """
        :param hero_list:  英雄列表信息
        :param hero_name:  英雄的名字
        :return:
        """
        for i in self.hero_list:
            if hero_name == i["name"]:
                self.hero_list.remove(i)
                return self.hero_list
        return False

    def create_hero(self, hero_name, hero_volume, hero_power):
        """
        :param hero_name:
        :param hero_volume:
        :param hero_power:
        :return:
        """
        if hero_volume<=0 or hero_volume >= 100:
            raise Exception("血量必须在1~99之间")
        if hero_power <=0:
            return False
        hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
        self.hero_list.append(hero_info)
        return True

    def find_hero(self, res):
        """
        如果查询到英雄，则返回英雄信息。
        如果没有查询到英雄，则返回False
        :param res:
        :return:
        """
        # 遍历所有的英雄信息，
        for i in self.hero_list:
            if res == i["name"]:
                return i
        # raise Exception("没有找到该英雄")
        return False