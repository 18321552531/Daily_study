# -*- coding: utf-8 -*-
# @Time    : 2019-08-24  16:04
# @File    : tem_test1.py
# @Author  : 啊啊

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

class Animal(object):

    def run(self):
        return 'dog is running!'
@app.route('/login', methods=['GET','POST'])
def login():
    return '这里是登入界面！'

@app.route('/template', methods=['GET','POST'])
def tem_index():
    url = url_for('login')
    lis = ['zsz','sdaf','haha']
    dic = {
        'title':'zszaa',
        'name':'zszaa',
        'age':'18',
        'bookname':'没啥书好看的',
        'lis':lis,
    }
    animal = Animal()

    return render_template('template_01.html',login_url=url,params=dic, animal=animal)

if __name__ == '__main__':
    app.run(debug=True)



