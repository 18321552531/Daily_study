#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: app.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-18 18:13:57
##########################################

from flask import Flask, request, render_template
import hashlib
import pymysql
import logging

app = Flask(__name__)
# mysql配置参数
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'zszaa0805',
    'db': 'Mysql_test',
}

@app.route('/home', methods=['GET','POST']) 
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def sigin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    # 连接mysql数据库
    db = pymysql.connect(**db_config)
    # 打开游标
    cursor = db.cursor()
    # 查找数据
    cursor.execute("select * from signin_table where username like '%s'"%(username))
    res = cursor.fetchall()
    cursor.close()
    db.close()
    if res == ():
        return render_template('form.html', message='账号不存在!', username=username)
    elif password != res[0][2]:
        return render_template('form.html', message='密码错误!', username=username)
    return render_template('signin_ok.html', username=username)

@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    # 连接数据库
    db = pymysql.connect(**db_config)
    # 打开游标
    cursor = db.cursor()
    # 插入数据
    cursor.execute('select max(id) from signin_table')
    id_max = cursor.fetchall()
    cursor.execute("insert into signin_table (id,username,password) values \
                   ('%s','%s','%s')"%(id_max[0][0]+1,username,password))
    db.commit()
    cursor.close()
    db.close()
    return render_template('register.html', message='注册成功!', username=username)

if __name__ == '__main__':
    app.run()








