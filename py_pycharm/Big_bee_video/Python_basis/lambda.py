# -*- coding: utf-8 -*-
# @Time    : 2019-08-25  22:08
# @File    : lambda.py
# @Author  : 啊啊

l = [2,3,4,5]

L = [x*3 for x in l]

'写一个lambda表达式，判断这个数的2次方+1能否被5整除，能返回True，不能返回false'


fx = lambda n: True if (n**2+1)%5 == 0 else False

'求两个变量的最大值'

fn = lambda x, y: max(x,y)


print(fn(4,6))





