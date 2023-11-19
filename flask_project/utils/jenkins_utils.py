#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 15:19
# @Author  : Owen
# @File    : jenkins_utils.py
# @Software: PyCharm

from jenkinsapi.jenkins import Jenkins


class JenkinsUtils:
    # Jenkins 服务
    BASE_URL = "http://42.192.73.147:7080/"
    # Jenkins 服务对应的用户名
    USERNAME = "admin"
    # Jenkins 服务对应的token
    PASSWORD = "1146976718c30d0b1c4f571ef074904060"
    JOB = "tpf"

    @classmethod
    def invoke(cls, invoke_params):
        """
        执行构建任务
        :return:
        """
        # 获取 Jenkins 对象
        jenkins_hogwarts = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 获取 Jenkins 的 job 对象
        job = jenkins_hogwarts.get_job(cls.JOB)
        # 构建 hogwarts job，传入的值必须是字典，key 对应 jenkins 设置的参数名
        # job.invoke(build_params={
        #     "step": "xx.py::TestXX::test_xx",
        #     "methods": "pytest"
        # })
        # job.invoke(build_params=invoke_params)
        job.invoke()
        # 获取job 最后一次完成构建的编号
        last_build_number = job.get_last_buildnumber() + 1
        # 执行方式为：pytest 用例名称 指定报告生成地址
        # 生成报告格式为
        # http://42.192.73.147:7080/job/tpf/22/allure/
        # 获取本次构建的报告地址
        report = f"{cls.BASE_URL}job/{cls.JOB}/{last_build_number}/allure/"
        return report