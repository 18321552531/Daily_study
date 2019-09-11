# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  21:59
# @File    : views.py
# @Author  : 啊啊

'''
主业务中的视图和路由定义
'''
# 主业务模块
from flask import render_template
# 导入蓝图,用于构建路由
from . import main_view
from app import db
# 导入实体类
from ..models import *

# 主界面
@main_view.route('/',)
def main():
    cates = Category.query.all()
    print(cates)
    topics = Topic.query.all()
    return render_template('index.html',cates=cates,topics=topics)

# 登入界面
@main_view.route('/login')
def login_view():
    user = db.session.query(User).filter_by(id=1).first()
    print(user)
    return render_template('login.html')

# 注册界面
@main_view.route('/register')
def register_view():
    return render_template('register.html')
# 发表博客
@main_view.route('/release')
def release_view():
    return render_template('release.html')
