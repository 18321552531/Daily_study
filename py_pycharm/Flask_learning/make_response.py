# -*- coding: utf-8 -*-
# @Time    : 2019-09-02  22:59
# @File    : make_response.py
# @Author  : 啊啊

from flask import Flask,make_response,render_template,request

app = Flask(__name__)

@app.route('/response')
def response():
    res = make_response('使用相应对象返回')
    return res

if __name__ == '__main__':
    app.run()


