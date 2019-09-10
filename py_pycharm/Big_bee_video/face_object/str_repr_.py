# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  20:55
# @File    : str_repr_.py
# @Author  : 啊啊

class Number(object):
    def __init__(self,name):
        self.name = name

    def __len__(self):
        return 18

    def __repr__(self):
        return '<Number:%s>'%self.name



n = Number('zsz')
print(repr(n))


