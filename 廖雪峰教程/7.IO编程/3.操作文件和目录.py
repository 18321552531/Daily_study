# -*- coding: utf-8 -*-
# @Time    : 2019-07-13  22:57
# @File    : 3.操作文件和目录.py
# @Author  : 啊啊

'''
第三节 操作文件和目录
'''
import os

# uname主要是获取系统的详细信息
# for i in os.uname():
#     print(i)

# os.environ来获取操作系统的全部环境变量

# print(os.environ)
'''
操作文件和目录
操作文件的函数一部分在os中， 还有一部分在os.path中；
'''
# mkdir创建一个目录、rmdir删除一个目录。
# os.rename('test.py', 'test.txt')
file = open('aa.txt', 'w')
file.write('hello world!')
file.close()
os.remove('aa.txt')




