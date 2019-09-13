# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  21:59
# @File    : views.py
# @Author  : 啊啊

'''
主业务中的视图和路由定义
'''
# 主业务模块
from flask import render_template,request,session,redirect
# 导入蓝图,用于构建路由
from . import main_view
from app import db
# 导入实体类
from ..models import *

# 主界面
@main_view.route('/',)
def main():
    cates = Category.query.all()
    topics = Topic.query.all()
    # 获取登入信息
    if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id = session['uid']).first()
        return render_template('index.html',cates=cates,topics=topics,user=user)
    else:
        return render_template('index.html', cates=cates, topics=topics)

# 登入界面
@main_view.route('/login', methods=['POST','GET'])
def login_view():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 接收传递的数据
        loginname = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(loginname=loginname,upwd=password).first()
        # 如果存在数据将信息保存到session里面
        if user:
            session['uid'] = user.id
            session['uname'] = user.uname
            return redirect('/')
        else:
            errMsg = '用户名或者密码不正确！'
            return render_template('login.html', errMsg=errMsg)


# 注册界面
@main_view.route('/register', methods=['GET','POST'])
def register_view():
    print(request.method)
    if request.method == 'GET':
        print('get')
        return render_template('register.html')
    else:
        print('post')
        loginname = request.form.get('loginname')
        uname = request.form.get('username')
        email = request.form.get('email')
        url = request.form.get('url')
        upwd= request.form.get('password')
        user = User(loginname,uname,email,url,upwd)
        db.session.add(user)
        db.session.commit()
        # 获取session 并登入
        login_user = db.session.query(User).filter_by(loginname=loginname).first()
        session['uid'] = login_user.id
        session['uname'] = login_user.uname
        return redirect('/')
# 发表博客
@main_view.route('/release')
def release_view():
    return render_template('release.html')

# 退出的路径
@main_view.route('/logout')
def logout_view():
    if 'uid' in session and 'uname' in session:
        del session['uid']
        del session['uname']
    return redirect('/')
