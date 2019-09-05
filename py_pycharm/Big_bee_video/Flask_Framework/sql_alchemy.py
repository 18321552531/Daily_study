# -*- coding: utf-8 -*-
# @Time    : 2019-09-05  20:18
# @File    : sql_alchemy.py
# @Author  : 啊啊
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
#
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 指定连接字符串
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zszaa0805@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 执行完毕自动提交
app.config['SQLALCHEMY_COMMIT_ON_TRARDOWN'] = True
db = SQLAlchemy(app)

# 创建模型类 - Models
'''
创建Users的类，映射到表中users
创建字段id，主键， 递增
字段username ，长度为80的字符串，不允许为空，必须唯一
字段age， 整数， 允许空
字段email， 长度为120的字符串， 必须唯一
'''
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String(80),nullable=False,unique=True)
    age = db.Column(db.SmallInteger, nullable=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return '<Users:%r>' %self.username

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True,)
    sname = db.Column(db.String(30), nullable=False,)
    sage = db.Column(db.Integer, )

    def __init__(self, sname, sage):
        self.sname = sname
        self.sage = sage

    def __repr__(self):
        return '<Student:%r>'%self.sname

class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True,)
    tname = db.Column(db.String(30), nullable=False,)
    tage = db.Column(db.Integer, )

    def __init__(self, tname, tage):
        self.tname = tname
        self.tage = tage

    def __repr__(self):
        return '<Student:%r>'%self.tname

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True,)
    cname = db.Column(db.String(30), nullable=False,)

    def __init__(self, cname, ):
        self.cname = cname

    def __repr__(self):
        return '<Student:%r>'%self.cname


# 将创建好的实体类映射回数据库
db.create_all()
#
# @app.route('/insert')
# def inser_values():
#     # 创建users对象
#     users = Users('zszaa', 24, '729269746@qq.com')
#     # 将对象db.session.add()插入数据库
#     db.session.add(users)
#     # 提交操作
#     db.session.commit()
#     return "insert success"

@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    age = request.form['age']
    email = request.form['email']
    users = Users(username,age,email)
    db.session.add(users)
    db.session.commit()
    return '提交成功'




if __name__ == '__main__':
    app.run(debug=True)



