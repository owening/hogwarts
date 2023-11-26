#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 10:28
# @Author  : Owen
# @File    : server.py
# @Software: PyCharm

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base, scoped_session

# 定义 app
app = Flask(__name__)
# 解决跨域
CORS(app, supports_credentials=True)

# 注册 jwt
jwt = JWTManager(app)
# 配置服务端密钥
app.config["JWT_SECRET_KEY"] = "hogwarts_user_AHKFJJD5"
# 开启数据库跟踪模式
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# SQLAlchemy 设置
Base = declarative_base()
# 定义数据库
db_user = "root"
db_pass = 123456
db_host = "42.192.73.147"
db_port = "3307"
db_name = "owen_db"
# 数据库类型+数据库引擎（ pip install pymysql）
db_url = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'
# 创建引擎，连接到数据库
engine = create_engine(db_url, echo=True)
# 创建session对象
# DBSession = sessionmaker(bind=engine)
# db_session: Session = DBSession()
DBSession = scoped_session(sessionmaker(bind=engine))


@app.before_request
def before_request():
    # 在每个请求前执行的代码
    # 在请求开始的时候实例化DBsession
    DBSession()


@app.teardown_request
def teardown_request(exception=None):
    # 在每个请求后执行的代码
    if exception:
        DBSession.rollback()
    # 请求结束之后remove掉DBsession
    DBSession.remove()


def register_router():

    # 如果出现循环导入，把导包语句放在方法内执行。并且调用此函数
    from controller.user_controller import user_router
    from controller.testcase_controller import testcase_router
    from controller.plan_controller import plan_router
    from controller.record_controller import record_router
    # 注册蓝图
    app.register_blueprint(user_router)
    app.register_blueprint(testcase_router)
    app.register_blueprint(plan_router)
    app.register_blueprint(record_router)


if __name__ == '__main__':
    register_router()
    app.run(debug=True, port=5000)
