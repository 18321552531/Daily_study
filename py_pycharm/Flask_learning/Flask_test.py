# -*- coding: utf-8 -*-
# @Time    : 2019-07-19  15:12
# @File    : Flask_test.py
# @Author  : 啊啊


from flask import Flask
app = Flask(__name__)

@app.route('/zszaa/<name>')
def hello_world(name):
   return 'hello world, my name is %s.' % (name)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'My post id is %s' %(postID)
if __name__ == '__main__':
   app.run()

