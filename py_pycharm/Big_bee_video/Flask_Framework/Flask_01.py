# -*- coding: utf-8 -*-
# @Time    : 2019-08-21  22:23
# @File    : Flask_01.py
# @Author  : 啊啊


from flask import Flask
# 把当前程序构成flask应用调试接受请求（request） 给出 响应（response）
app = Flask(__name__)
# @app.route 是 flask中的路由 定义用户的路径，'/'表示根路径。home 表示匹配路劲之后的处理程序。
# 函数必须要有 响应对象
@app.route('/home')
def hello_world():
    return 'It is my fisrt flask'

if __name__ == '__main__':
    #  开发环境中使用调试模式，生产环境不允许使用。
    app.run(debug = True)
