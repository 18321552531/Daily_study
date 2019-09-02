# -*- coding: utf-8 -*-
# @Time    : 2019-09-01  21:28
# @File    : Itrator.py
# @Author  : 啊啊

'''
迭代器是指iter 函数返回的对象
迭代器可以用next来获取可迭代对象的数据

迭代器函数：
iter(iterable)可以从迭代对象中返回一个迭代器，
'''

lis = [1,3,4,5,6]
it = iter(lis)

print(next(it))
print(next(it))
a = iter(range(10))

print(next(a))





