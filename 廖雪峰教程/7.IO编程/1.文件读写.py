# -*- coding: utf-8 -*-
# @Time    : 2019-07-13  21:08
# @File    : 1.文件读写.py
# @Author  : 啊啊
'''
第一节 文件读写

'''

load = 'test.txt'
#
# file = open(load, 'r')
# # 文件读取和关闭
# file.read()
# file.close()
# print(file)
#
# #但是每次要关闭过于麻烦，所以一般用with...open...
# with open(load, 'r') as file:
#     print(file.read())

'''
文件写入
'''
with open(load, 'a') as file:
    file.write('\n好好学习啊！')

with open(load, 'r') as file:
    print(file.read())