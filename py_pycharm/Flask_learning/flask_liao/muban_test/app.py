#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: app.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-18 17:33:01
##########################################

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin_ok.html',username=username)
    else:
        return render_template('form.html', message='error password!', username=username)

if __name__ == '__main__':
    app.run()
