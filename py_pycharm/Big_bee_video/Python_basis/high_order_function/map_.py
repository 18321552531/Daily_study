# -*- coding: utf-8 -*-
# @Time    : 2019-08-25  22:36
# @File    : map_.py
# @Author  : 啊啊

'''
满足下列一个条件的函数即为高阶函数：
1.函数接受一个或者多个函数作为参数传入
2.函数返回一个函数

python内建的高阶函数有：
map，filter，sorted
'''

'''
map函数：
    map(func,*interables)
    用函数和对和迭代对象中的每一个元素作为参数传入，
    计算出新的可迭代对象，当最短的一个可迭代对象不在提供数据时，
    可迭代对象生成结束
'''

for i in map(lambda x, y:x**y, range(1,11),range(11,1,-1)):
    print(i)

