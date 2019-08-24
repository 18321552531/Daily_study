# -*- coding: utf-8 -*-
# @Time    : 2019-08-23  13:03
# @File    : Flask_02.py.py
# @Author  : 啊啊
from flask import Flask,request,render_template,url_for
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    login_url = url_for('login')
    return '<a href='+login_url+'>点击登入</a>'

@app.route('/login', methods=['GET','POST'])
def login():
    return '这是的登入页面！'

if __name__ == '__main__':
    app.run(debug=True)



