# -*- coding: utf-8 -*-
# @Time    : 2019-08-21  22:23
# @File    : Flask_01.py
# @Author  : 啊啊


from flask import Flask, render_template,url_for
# 把当前程序构成flask应用调试接受请求（request） 给出 响应（response）
app = Flask(__name__)
# @app.route 是 flask中的路由 定义用户的路径，'/'表示根路径。home 表示匹配路劲之后的处理程序。
# 函数必须要有 响应对象
@app.route('/home')
def hello_world():
    print(url_for('static', filename='pic/IMG_1138.jpg'))
    return render_template('template_02.html')

@app.errorhandler(404)
def not_find_page(e):
    return render_template('/error/404.html'),404


if __name__ == '__main__':
    #  开发环境中使用调试模式，生产环境不允许使用。
    app.run(debug = True)
