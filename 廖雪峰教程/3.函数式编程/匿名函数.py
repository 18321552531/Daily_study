# -*- coding: utf-8 -*-
# @Time    : 2019-07-07  22:25
# @File    : 匿名函数.py
# @Author  : 啊啊
'''
匿名函数：lambda
lambda x: fun(x)
'''
###匿名函数可以作为返回值。
def building(x, y):
    return lambda: x ** 2 + y ** 2

results = building(3, 4)
print(results())


