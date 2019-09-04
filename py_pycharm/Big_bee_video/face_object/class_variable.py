# -*- coding: utf-8 -*-
# @Time    : 2019-09-04  13:05
# @File    : class_variable.py
# @Author  : 啊啊



# 记录创建类变量的个数

class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        self.__class__.count += 1
        print('student number is' ,self.count)

    def __del__(self):
        print('student gone',self.name)
        self.__class__.count -= 1

bob = Student('bob')
sam = Student('sam')



