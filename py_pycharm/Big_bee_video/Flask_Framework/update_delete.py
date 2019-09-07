# -*- coding: utf-8 -*-
# @Time    : 2019-09-07  14:51
# @File    : update_delete.py
# @Author  : 啊啊
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sql_alchemy import Users
import pymysql
# print('import sql_alchemy')
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 指定连接字符串
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zszaa0805@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 执行完毕自动提交
app.config['SQLALCHEMY_COMMIT_ON_TRARDOWN'] = True
db = SQLAlchemy(app)


@app.route('/delete', methods=['POST','GET'])
def delete():
    user = db.session.query(Users).filter_by(id=3).first()
    db.session.delete(user)
    db.session.commit()
    return 'delete id=3'

@app.route('/update', methods=['POST','GET'])
def update():
    user = db.session.query(Users).filter_by(id=1).first()
    user.username = 'zhushengzu_aa'
    user.age = 19
    db.session.add(user)
    db.session.commit()
    return 'update id=1'


if __name__ == '__main__':
    app.run()

