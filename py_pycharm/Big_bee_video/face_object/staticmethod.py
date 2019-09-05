# -*- coding: utf-8 -*-
# @Time    : 2019-09-05  13:38
# @File    : staticmethod.py
# @Author  : 啊啊

class A(object):
    @staticmethod
    def myadd(x,y):
        return x+y


print(A.myadd(1,2))



