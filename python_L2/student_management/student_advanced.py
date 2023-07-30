#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 21:29
# @Author  : Owen
# @File    : student_advanced.py
# @Software: PyCharm

"""
作业要求
编写学员实体类 Student，对应成员变量包含：学号 id、姓名 name、性别 sex；
编写学员管理类 StudentManagement ，实现添加学员方法 addStudent()。
编写StudentManagement的main()方法进行学员信息的添加：
学号：1001,姓名：张三,性别：男。
学号：1002,姓名：莉丝,性别：女。
学号：1003,姓名：王武,性别：男。
编写学员管理类 StudentManagement ，实现删除学员方法 deleteStudent()，根据学员id 删除以下学员：
学号：1002,姓名：莉丝,性别：女。
控制台打印字符串界面，提示用户根据编号选择对应功能，界面功能如下：
1.根据学号查看学员信息
2.添加学员
3.查看所有学员信息
4.查看当前所有学员的信息
5.退出系统
自定义异常类：添加学员传入参数不合理时抛出自定义异常
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
        print(f"添加成功,添加的学生信息为：\n{student_info}")

    def getAllStudentInfo(self):
        """
        获取所有学生信息
        :return:
        """
        for stu in self.all_stu_list:
            print(stu)

    def getStudentById(self, stu_id):
        for stu in self.all_stu_list:
            if stu.id == stu_id:
                return stu


    def deleteStudent(self, stu_id):
        for stu in self.all_stu_list:
            if stu.id == stu_id:
                self.all_stu_list.remove(stu)
                print(f"删除成功，删除的学员信息为：\n{stu}")
        print(f"删除后的学员信息为:")
        for stu in self.all_stu_list:
            print(stu)

    def managementOperation(self, num):

        if num == 1:
            sut_id = int(input("请输入想要查找的学员编号:"))
            stu_info = self.getStudentById(sut_id)
            print(f"学员信息获取成功，该学员信息为：\n{stu_info}")
        elif num == 2:
            stu_id = int(input("请输入学员编号："))
            stu_name = input("请输入学员姓名：")
            stu_sex = input("请输入学员性别：")
            if stu_sex != '男' and stu_sex != '女':
                print("性别输入有误，请重新输入性别：")
                stu_sex = input("请输入学员性别：")
            stu_info = Student(stu_id, stu_name, stu_sex)
            self.addStudent(stu_info)
        elif num == 3:
            sut_id = int(input("请输入想要删除的学员编号"))
            self.deleteStudent(sut_id)
        elif num == 4:
            print("以下是所有学员信息：")
            self.getAllStudentInfo()


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
    # 添加多个学员
    manager.addStudents(stu_dict)
    state = True
    while state:
        print("""
        ----------欢迎来到学员信息管理系统----------
               1. 根据学号查看学员信息
               2. 添加学员
               3. 根据学号删除学员后，查看所有学员信息
               4. 查询当前所有学员的信息
               5. 退出系统
               """)
        try:
            num = int(input(f"请输入你的选择:"))
            if num == 5:
                state = False
            else:
                manager.managementOperation(num)
        except ValueError:
            print("输入有误！请输入正确编号！")
            continue

    print("成功退出系统,欢迎下次使用")
