#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: flask_url.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-15 23:48:55
##########################################

from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/user/')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
   app.run(debug = True)
