# -*- coding: utf-8 -*-
# @Time    : 2019-09-07  23:41
# @File    : add_practise.py
# @Author  : 啊啊

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
from one_with_many import Course,Teachers
# print('import sql_alchemy')
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 指定连接字符串
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zszaa0805@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 执行完毕自动提交
app.config['SQLALCHEMY_COMMIT_ON_TRARDOWN'] = True
db = SQLAlchemy(app)

@app.route('/add_info',methods=['GET','POST'])
def add_info():
    if request.method == 'GET':
        courses = db.session.query(Course)
        print(courses)
        return render_template('register_teacher.html',courses=courses)
    else:
        tname = request.form.get('tname')
        tage = request.form.get('tage')
        course_id = request.form.get('course_id')
        print(course_id)
        teacher = Teachers(tname, tage)
        course = db.session.query(Course).filter_by(id=course_id).first()
        teacher.course=course
        db.session.add(teacher)
        db.session.commit()
        return '上传教师信息成功！'




if __name__ == '__main__':
    app.run(debug=True)




