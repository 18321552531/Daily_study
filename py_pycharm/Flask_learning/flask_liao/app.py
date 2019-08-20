#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: app.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-18 17:03:24
##########################################

from flask import Flask, request

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return '<h1>home</h1>'

@app.route('/signin', methods=['GET'])
def sigin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route('/signin', methods=['POST'])
def sigin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h2>hello admin</h2>'
    else:
        return '<h2>error password</h2>'

if __name__ == '__main__':
    app.run()
