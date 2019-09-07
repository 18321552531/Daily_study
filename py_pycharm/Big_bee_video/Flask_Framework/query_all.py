# -*- coding: utf-8 -*-
# @Time    : 2019-09-06  23:04
# @File    : query_all.py
# @Author  : 啊啊

from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sql_alchemy import Users,Students
import pymysql
app = Flask(__name__)

#连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zszaa0805@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# class Users(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True,)
#     username = db.Column(db.String(80),nullable=False,unique=True)
#     age = db.Column(db.SmallInteger, nullable=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self,username,age,email):
#         self.username = username
#         self.age = age
#         self.email = email
#
#     def __repr__(self):
#         return '<Users:%r>' %self.username


@app.route('/queryall', methods=['GET','POST'])
def query_all():
    users = db.session.query(Users).all()
    return render_template('user_01.html',params=locals())

@app.route('/querybyid/<int:id>', methods=['GET','POST'])
def query_by_id(id):
    user = db.session.query(Users).filter(Users.id==id).first()
    return render_template('use_info.html', params=locals())

@app.route('/delete')
def delete():
    userid = request.args.get('id')
    user = db.session.query(Users).filter(Users.id == userid).first()
    db.session.delete(user)
    db.session.commit()
    url = request.headers.get('referer','queryall')
    return redirect(url)
@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'GET':
        # 获取前端传递的id返回id的界面
        id = request.args.get('id')
        user = db.session.query(Users).filter_by(id=id).first()
        return render_template('update.html',user=user)
    else:
        # 接受前端传递的参数
        id = request.form.get('id')
        username = request.form.get('username')
        age = request.form.get('age')
        email = request.form.get('email')
        # 查
        user = db.session.query(Users).filter_by(id=id).first()
        user.username = username
        user.age = age
        user.email = email
        db.session.add(user)
        db.session.commit()
        return redirect('/queryall')

if __name__ == '__main__':
    app.run(debug=True)


