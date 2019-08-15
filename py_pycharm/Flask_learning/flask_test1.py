#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: flask_test1.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-14 23:41:45
##########################################

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello_word'

if __name__ == '__main__':
    app.run()

