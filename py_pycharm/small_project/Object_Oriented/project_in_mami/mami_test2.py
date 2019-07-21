# -*- coding: utf-8 -*-
# @Time    : 2019-07-21  11:25
# @File    : mami_test2.py
# @Author  : 啊啊

'''
编写程序, A 继承了 B, 俩个类都实现了 handle 方法,
在 A 中的 handle 方法中调用 B 的 handle 方法
'''

class B(object):
    def __init__(self):
        pass
    def handle(self):
        print('B_handle')

class A(B):
    def __init__(self):
        super().__init__()
    def handle(self):
        super().handle()

a = A()     ###继承其他class的时候就要加（）？？？
a.handle()

