# -*- coding: utf-8 -*-
# @Time    : 2019-07-02  19:41
# @File    : 2.高级特性.py
# @Author  : 啊啊
'''
主要介绍了函数的高级特性：
切片；迭代；列表生成器；生成器
'''

####迭代:python的数据可迭代对象较多，例如：
dic = {'a':1, 'b':2, 'c':3}
for i in dic:
    print(i)
#####可以通过collection模块中的Iterable来进行判断是否为可迭代的对象
from collections import Iterable
A = isinstance(123456, Iterable)
print(A)
####一个很重要的迭代函数enumerate可以吧list变为索引对应元素
for i,values in enumerate(dic):
    print(i, values)
###使用迭代找出list中的最大和最小值，返回一个tuple：
list = [5,4,5,6,57,6214,3]
def findMaxandMin(list):
    if len(list)==0:
        return (0,0)
    else:
        max = min = list[0]
        for i in list:
            if max <= i:
                max = i
            if min >= i:
                min = i
        return (max, min)


a = findMaxandMin(list)
# print(a)

#####列表生成式
#将L1 = ['Hello', 'World', 18, 'Apple', None]输出为L2 = ['Hello', 'World', 'Apple']
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i for i in L1 if isinstance(i, str)]
# print(L2)

####生成器：generator 其中list为[]，而列表生成器则为（）, 用next来获取打印值：
g = (x for x in range(10))
for i in g:
    print(i)

'''
迭代器：生成器不仅仅能可以用作for循环，还能通过next进行调用。可以被next调用的我们称之为
迭代器，可以通过instance来判断其是否为Iterator
凡是可作用于for循环的对象都是Iterable类型：凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
'''












import pandas as pd







