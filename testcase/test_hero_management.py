#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/30 11:07
# @Author  : Owen
# @File    : test_hero_management.py
# @Software: PyCharm
import allure
import pytest

from python_L2.hero_management import HeroManagement

class TestHeroManagement():

    def setup(self):
        self.hero_mangament = HeroManagement()

    def test_update_hero(self):
        self.hero_mangament.create_hero("亚瑟",90,70)
        self.hero_mangament.update_hero("亚瑟",56)
        res = self.hero_mangament.find_hero("亚瑟")
        assert res["volume"] == 56


    def test_delete_hero(self):
        self.hero_mangament.create_hero("亚瑟", 90, 70)
        self.hero_mangament.delete_hero("亚瑟")
        res = self.hero_mangament.find_hero("亚瑟")
        assert res == False

    @allure.title("测试添加英雄，英雄姓名：{name},血量:{volume},攻击力:{power}")
    @pytest.mark.parametrize("name, volume, power",[["亚瑟",90,70],["EZ",70,66]])
    def test_create_hero(self,name, volume, power):
        with allure.step("添加英雄"):
            self.hero_mangament.create_hero(name, volume, power)
        with allure.step("添加后查找该英雄"):
            res = self.hero_mangament.find_hero(name)
        with allure.step("进行断言"):
            assert res["name"] == name
            assert res["volume"] == volume
            assert res["power"] == power


    def test_find_hero(self):
        res = self.hero_mangament.find_hero("亚瑟")
        assert res == False
