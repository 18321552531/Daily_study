# -*- coding: utf-8 -*-
# @Time    : 2019-07-07  21:50
# @File    : 返回函数.py
# @Author  : 啊啊
'''
返回函数：
将函数作为一个返回值。
高阶函数除了可以将函数作为参数之外，还能将函数作为一个返回值。
'''

###例如：
# def lazy_sum(*args):
#     def sum():
#         a = 0
#         for i in args:
#             a += i
#         return a
#     return sum
#
# num = lazy_sum(1,2,5,36,3)
# print(num())

##关于闭包函数

