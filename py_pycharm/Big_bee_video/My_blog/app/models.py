# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  21:56
# @File    : models.py
# @Author  : 啊啊

'''
当前项目相关的所有实体类（模型文件）
'''
from . import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(50), nullable=False)
    # 增加与Topic之间的反向引用
    topic = db.relationship('Topic', backref='category', lazy='dynamic')

    def __init__(self, cate_name):
        self.cate_name = cate_name

    def __repr__(self):
        return '<cate_name:%s>' % self.cate_name


class BlogType(db.Model):
    __tablename__ = 'blogtype'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20), nullable=False)
    # 增加与Topic之间的反向引用
    topic = db.relationship('Topic', backref='blogtype', lazy='dynamic')

    def __init__(self, type_name):
        self.type_name = type_name

    def __repr__(self):
        return '<type_name:%s>' % self.type_name


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200))
    upwd = db.Column(db.String(30), nullable=False)
    is_author = db.Column(db.SmallInteger, default=0)
    # 增加与Topic之间的反向引用
    topic = db.relationship('Topic', backref='user', lazy='dynamic')
    # 增加与reply之间的反向引用
    reply = db.relationship('Reply', backref='user', lazy='dynamic')
    # 增加与Topic之间的关联关系和反向引用
    voke_topic = db.relationship(
        'Topic',
        secondary='voke',
        backref = db.backref('voke.users',lazy='dynamic',),
        lazy='dynamic',
    )


    def __init__(self, loginname, uname, email, url, upwd, is_author):
        self.loginname = loginname
        self.uname = uname
        self.email = email
        self.url = url
        self.upwd = upwd
        self.is_auther = is_author

    def __repr__(self):
        return '<loginname:%s>' % self.loginname


class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False)
    read_num = db.Column(db.Integer, default=0)
    content = db.Column(db.Text, nullable=False)
    images = db.Column(db.Text)
    # 增加与category的映射关系（一对多）
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # 增加与Blogtype的映射关系（一对多）
    blogtype_id = db.Column(db.Integer, db.ForeignKey('blogtype.id'))
    # 增加与User的映射关系（一对多）
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 与reply之间的反向关系及引用
    reply = db.relationship('Reply', backref='topic', lazy='dynamic')

    def __init__(self, title, pub_date, read_num, context, images):
        self.title = title
        self.pub_date = pub_date
        self.read_num = read_num
        self.context = context
        self.images = images

    def __repr__(self):
        return '<title:%s>' % self.title


class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    reply_time = db.Column(db.DateTime, )
    # 一对多关系：topic为一reply为多
    topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))
    # 一对多关系：user为一reply为多
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self, content, reply_time):
        self.content = content
        self.reply_time = reply_time

voke = db.Table(
    'voke',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer,db.ForeignKey('user.id')),
    db.Column('topic_id',db.Integer,db.ForeignKey('topic.id')),
)
# db.create_all()