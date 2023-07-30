#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/19 21:39
# @Author  : Owen
# @File    : student.py
# @Software: PyCharm

"""
作业内容
编写学员实体类 Student，对应成员变量包含：学号 id、姓名 name、性别 sex；
编写学员管理类 StudentManagement ，实现添加学员方法 addStudent()。
编写StudentManagement的main方法进行学员信息的添加：

学号：1001,姓名：张三,性别：男。
学号：1002,姓名：莉丝,性别：女。
学号：1003,姓名：王武,性别：男。
"""

class Student:

    def __init__(self, id, name, sex):
        """
        构造方法
        :param id:   学号
        :param name: 姓名
        :param sex:    性别
        """
        self.id = id
        self.name = name
        self.sex = sex


class StudentManagement:
    # 类属性
    # 所有学员列表
    all_stu_list = []

    def addStudents(self, student_info):
        """
        实例方法
        添加多个学生信息
        :param student_info:  Student类对象的List
        :return:
        """
        # 学生列表初始化
        stu_list = []
        # 遍历Student类对象列表
        for stu in student_info:
            self.all_stu_list.append(stu)
            # 将多个Student类对象依次添加到stu_list学生列表中
            stu_list.append(stu)
        # 添加成功后，如stu_list学生列表中存在数据则按格式打印出来，否则提示列表为空
        if stu_list:
            print("同时添加的多个学员信息为：")
            for stu in stu_list:
                print(f"学号：{stu.id},姓名：{stu.name},性别：{stu.sex}")
        else:
            print("学生列表为空")

    def addStudent(self, student_info):
        """
        添加单个学生信息
        :param student_info:
        :return:
        """
        self.all_stu_list.append(student_info)
        print(f"添加的单个学生信息为：\n学号：{student_info.id},姓名：{student_info.name},性别：{student_info.sex}")

    def getAllStudentInfo(self):
        """
        获取所有学生信息
        :return:
        """
        print("以下是所有的学员信息：")
        for stu in self.all_stu_list:
            print(f"学号：{stu.id},姓名：{stu.name},性别：{stu.sex}")
        return self.all_stu_list


if __name__ == "__main__":
    # 调用Student类，给类属性赋值,分别完成类实例化对象给s1、s2、s3
    s1 = Student(1001, "张三", "男")
    s2 = Student(1002, "丽思", "女")
    s3 = Student(1003, "王武", "男")
    # 多个Student类对象--->创建列表
    stu_dict = [s1, s2, s3]
    # 实例化StudentManagement类对象给manager
    manager = StudentManagement()
    # 通过manager对象调用StudentManagement类下的实例方法addStudent()
    #添加多个学员
    manager.addStudents(stu_dict)
    s4 = Student(1004, "溜溜", "女")
    #添加单个学员
    manager.addStudent(s4)
    manager.getAllStudentInfo()

