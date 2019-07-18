# -*- coding: utf-8 -*-
# @Time    : 2019-07-04  23:03
# @File    : 高阶函数.py
# @Author  : 啊啊

'''
1.变量可以指向函数
2.函数名也是变量
'''
##变量可以指向函数，令f=abs（）看例子

# print(abs(-12))
# fun = abs
# print(fun(-12))
#
# ####2.函数名也是变量
# abs = 13
# print(abs)
#
# ###3.一个函数可以接受另外一个函数作为参数
#
# def sum_abs(x,y,fun):
#     return fun(x)+fun(y)
#
# a = sum_abs(-10, -12, fun)
# print(a)



'''
第二节：map/reduce函数
map接受两个参数，一个是函数，还有一个为Iterable，并且将结果作为一个新的Iterator返回。
reduce函数接收两个参数，把一个函数作用在一个序列上，例如：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
import numpy as np
def fun(x):
    return x*x
a = map(fun, np.arange(10))

print(list(a))
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
L1 = ['adam', 'LISA', 'barT']
def normaliza(name):
    return name.title()

L2 = map(lambda x:x.title(), L1)
print(list(L2))



'''
第三节：filter()函数
python 内建的函数filter()主要使用来过滤序列的。
filter()把传入的参数依次作用在每个元素上面，然后更加Ture或者Flase来确定是否保留元素。
'''
####例如提取list中的偶数函数

def get_even(num):
    return num % 2 == 0

list1 = [1,2,3,44,5,6,6,5]
l = filter(get_even, list1)
print(list(l))

###用filter来求素数。
#先构造一个从三开始的奇数序列。
def _odd_inter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

#最后定义一个生成器，不断返回下一个素数。
def primes():
    yield 2
    it = _odd_inter()
    while True:
        n = next(it)
        yield n
        print(n)
        it = filter(_not_divisible(n), it)

# print(list(primes()))

'''
第四节：sorted函数（排序）
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L1 = sorted(L, key = by_name)
print(L1)

