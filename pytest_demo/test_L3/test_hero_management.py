#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/30 14:51
# @Author  : Owen
# @File    : test_hero_management.py
# @Software: PyCharm
import allure
import pytest

from pytest_demo.test_L2.hero_management import HeroManagement
from pytest_demo.test_L3.load_yaml import load_yaml

create_data = load_yaml()

class TestHeroManagement:

    def setup(self):
        self.heromanagement = HeroManagement()



    def test_update_hero(self):
        assert True

    def test_delete_hero(self):
        assert True

    @allure.title("添加英雄用例，英雄姓名:{name}，血量:{hp},攻击力：{power}")
    @pytest.mark.parametrize("name,hp,power",create_data)
    def test_create_hero(self,name,hp,power):
        with allure.step(f"步骤一：添加英雄{name}"):
            self.heromanagement.create_hero(name,hp,power)
        with allure.step(f"步骤二：查找英雄{name}"):
            res = self.heromanagement.find_hero(name)
        with allure.step("步骤三：断言"):
            assert res["name"] == name
            assert res["volume"] == hp
            assert res["power"] == power


    @allure.title("英雄姓名参数错误场景")
    @pytest.mark.parametrize("name",[66,78.09,True])
    def test_create_hero_name_fail(self,name,):
        self.heromanagement.create_hero(name,25,78)
        res = self.heromanagement.find_hero(name)
        assert res["name"] == name

    @allure.title("有效姓名、无效血量")
    @pytest.mark.parametrize("hp",[0,-1,100])
    @pytest.mark.parametrize("name", ["赵云","张飞"])
    def test_create_hero_fail1(self,name,hp):
        with pytest.raises(Exception) as exc_create_info:
            self.heromanagement.create_hero(name,hp,66)
            # self.heromanagement.find_hero("赵云")
        assert str(exc_create_info.value) == "血量必须在1~99之间"


    @allure.story("有效血量、无效姓名")
    @pytest.mark.parametrize("hp",[1,2,99])
    @pytest.mark.parametrize("name", [66,False])
    def test_create_hero_fail2(self,name,hp):
        self.heromanagement.create_hero(name,hp,66)
        res = self.heromanagement.find_hero(name)
        assert res == False

    @allure.title("用例标题：查找不到英雄")
    def test_find_hero(self):
        with pytest.raises(Exception) as exc_info:
            self.heromanagement.find_hero("貂蝉")
        assert str(exc_info.value) == "没有找到该英雄"
