#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: Flask_04.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-29 23:25:17
##########################################

from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form_01.html')

@app.route('/form_return')
def form_return():
    if request.method=='GET':
        usename = request.args['usename']
        password = request.args['password']
        print('账号是:%s,密码是%s'%(str(usename),str(password)))
    return '提交成功'

if __name__ == '__main__':
    app.run(debug=True)
