# -*- coding: utf-8 -*-
# @Time    : 2019-09-06  13:30
# @File    : override.py
# @Author  : 啊啊

'''
覆盖
'''


class A(object):
    def work(self):
        print('a is working!')

class B(A):
    def work(self):
        print('b is working')

b = B()

a = A().work()
'''调用超类'''

super(B,B()).work()

