# -*- coding: utf-8 -*-
# @Time    : 2019-08-27  22:51
# @File    : Flask_03.py
# @Author  : 啊啊
from flask import Flask,request,render_template,url_for

app = Flask(__name__,template_folder='new_template')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)






