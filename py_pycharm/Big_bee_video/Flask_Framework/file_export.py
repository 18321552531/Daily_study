# -*- coding: utf-8 -*-
# @Time    : 2019-09-02  23:15
# @File    : file_export.py
# @Author  : 啊啊
from flask import Flask,request,render_template
import datetime

app = Flask(__name__)

@app.route('/file',methods=['GET','POST'])
def file_views():
    if request.method == 'GET':
        return render_template('file_export.html')
    else:
        # 接受名称为uimg的文件
        f = request.files['uimg']
        # 获取上传图片的名称
        date_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = date_time+'.'+f.filename.split('.')[-1]
        print('文件名称:'+filename)
        # 将文件保存到static的文件
        f.save('img/'+filename)
        return 'upload ok!'

if __name__ == '__main__':
    app.run(debug=True)


