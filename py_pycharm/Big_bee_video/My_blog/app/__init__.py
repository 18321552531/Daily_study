# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  21:54
# @File    : __init__.py.py
# @Author  : 啊啊

'''
对整个应用进行初始化
'''

'''
1.构建flask应用和各种配置
2.构建sqlalchemy的应用
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zszaa0805@localhost:3306/blog'
    # 数据库内容更新是自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 配置session的秘钥
    app.config['SECRET_KEY'] = 'zszaa0805'
    # 数据库的初始化
    db.init_app(app)
    # 将main函数的蓝图和app关联到一起
    from .main import main_view as main_blue_print
    app.register_blueprint(main_blue_print)
    # 将user的蓝图和app关联到一起
    from .user import user
    app.register_blueprint(user)
    return app



