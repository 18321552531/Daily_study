# -*- coding: utf-8 -*-
# @Time    : 2019-09-06  13:10
# @File    : inheritance.py
# @Author  : 啊啊
'''
继承

'''

class Human(object):
    pass

class Student(Human):
    pass

class Teacher(Student):
    pass

print(Teacher.__bases__)

