#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 18:51
# @Author  : Owen
# @File    : student_middle.py
# @Software: PyCharm

"""
编写学员实体类 Student，对应成员变量包含：学号 id、姓名 name、性别 sex；
编写学员管理类 StudentManagement ，实现添加学员方法 addStudent()。
编写StudentManagement的main()方法进行学员信息的添加：
学号：1001,姓名：张三,性别：男。
学号：1002,姓名：莉丝,性别：女。
学号：1003,姓名：王武,性别：男。
编写学员管理类 StudentManagement ，实现删除学员方法 deleteStudent()，根据学员id 删除以下学员：
学号：1002,姓名：莉丝,性别：女。
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

    def __repr__(self):
        """
        定义类属性的打印格式
        """
        return f"学号：{self.id},姓名：{self.name},性别：{self.sex}"


class StudentManagement:
    # 类属性
    # 所有学员集合
    all_stu_set = set()

    def addStudents(self, student_info):
        """
        实例方法
        添加多个学生信息
        :param student_info:  Student类对象的Set
        :return:
        """
        # 学生集合定义、临时存储
        stu_set = set()
        # 遍历Student类对象集合
        for stu in student_info:
            self.all_stu_set.add(stu)
            # 将多个Student类对象依次添加到stu_集合学生集合中
            stu_set.add(stu)
        # 添加成功后，如stu_集合学生集合中存在数据则按格式打印出来，否则提示集合为空
        if stu_set:
            print("同时添加的多个学员信息为：")
            for stu in stu_set:
                print(stu)
        else:
            print("学生信息为空")

    def addStudent(self, student_info):
        """
        添加单个学生信息
        :param student_info:
        :return:
        """
        self.all_stu_set.add(student_info)
        print(f"添加的单个学生信息为：\n{student_info}")

    def getAllStudentInfo(self):
        """
        获取所有学生信息
        :return:
        """
        print("以下是所有的学员信息：")
        for stu in self.all_stu_set:
            print(stu)
        return self.all_stu_set

    def getStudentById(self, stu_id):
        for stu in self.all_stu_set:
            if stu.id == stu_id:
                print(f"查找到到学生信息为：\n{stu}")
                return stu

    def deleteStudent(self, stu_id):
        stu = self.getStudentById(stu_id)
        self.all_stu_set.remove(stu)
        print(f"被删除到学生信息为：\n{stu}")


if __name__ == "__main__":
    # 调用Student类，给类属性赋值,分别完成类实例化对象给s1、s2、s3
    s1 = Student(1001, "张三", "男")
    s2 = Student(1002, "丽思", "女")
    s3 = Student(1003, "王武", "男")
    s4 = Student(1004, "溜溜", "女")
    # 多个Student类对象--->创建集合
    stu_set = {s1, s2, s3}
    # 实例化StudentManagement类对象给manager
    manager = StudentManagement()
    # 通过manager对象调用StudentManagement类下的实例方法addStudent()
    #添加多个学员
    manager.addStudents(stu_set)
    #添加单个学员
    manager.addStudent(s4)

    #通过学号查询学生信息
    manager.getStudentById(1002)
    #通过学号删除学生信息
    manager.deleteStudent(1003)
    manager.deleteStudent(1001)
    #获取所有学生信息
    manager.getAllStudentInfo()