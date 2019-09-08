# -*- coding: utf-8 -*-
# @Time    : 2019-09-08  17:49
# @File    : many_with_many.py
# @Author  : 啊啊


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
# print('import sql_alchemy')
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
    # 增加一个列：course_id ,外键列， 引用自主键表（course）
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    # 增加反向引用和partner实体类做反向引用，在partner中也能找到teachers
    partner = db.relationship('Partner', backref='teacher',uselist=False)

    def __init__(self, tname, tage):
        self.tname = tname
        self.tage = tage

    def __repr__(self):
        return '<Student:%r>'%self.tname

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True,)
    cname = db.Column(db.String(30), nullable=False,)
    # 反向引用：返回与当前课表相关的teacher列表
    # backref: 定义反向关系，本质上会向Teacher实体中增加一个course属性。
    teachers = db.relationship('Teachers', backref='course',lazy='dynamic')


    def __init__(self, cname, ):
        self.cname = cname

    def __repr__(self):
        return '<Student:%r>'%self.cname

class Partner(db.Model):
    __tablename__ ='partner'
    id = db.Column(db.Integer, primary_key=True,)
    pname = db.Column(db.String(30), nullable=False,)
    page = db.Column(db.Integer, )
    # 增加一个列表示引用子teache表的主键
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

    def __init__(self, pname, page):
        self.pname = pname
        self.page = page
    def __repr__(self):
        return '<Partner:%r>'%self.pname

class Student(db.Model):
    __tablename__='student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, )
    score = db.Column(db.Integer, )
    # 增加关联属性和反向引用
    courses = db.relationship(
        'Course',
        secondary='student_course',
        lazy='dynamic',
        backref=db.backref('students', lazy='dynamic')
    )

    def __init__(self, sname, sage, score):
        self.sname = sname
        self.sage = sage
        self.score = score

    def __repr__(self):
        return '<Student:%>'%self.sname


student_course = db.Table(
    'student_course',
    db.Column('id',db.Integer, primary_key=True),
    db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
)

db.create_all()

@app.route('/add')
def add():
    # 向多对多的关系表中增加数据
    # 先查询student，在查询course
    stu = Student.query.filter_by(id=2).first()
    cou = Course.query.filter_by(id=3).first()
    # 将cou的这门课程追加到stu中
    stu.courses.append(cou)
    db.session.add(stu)
    db.session.commit()
    return 'ok'

@app.route('/query')
def query():
    student = db.session.query(Student).filter_by(id=2).first()
    courses = student.courses.all()
    print('学生姓名:%s'%student.sname)
    for i in courses:
        print("课程为：%s"%i.cname)
    return "query ok!"

if __name__ == '__main__':
    app.run(debug=True)
