# -*- coding: utf-8 -*-
# @Time    : 2019-08-08  00:18
# @File    : 2.基本数据类型.py
# @Author  : 啊啊

import os
list = []
filename = os.listdir('/Users/zhushengzu/python_load/py_pycharm/My_Notebook')
for i in filename:
    if i.split('.')[-1] == 'todo':
        list.append(i)
print(list)
print(filename)


