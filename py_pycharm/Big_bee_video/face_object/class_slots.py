# -*- coding: utf-8 -*-
# @Time    : 2019-09-05  13:08
# @File    : class_slots.py
# @Author  : 啊啊

class Student(object):
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student('sam', 80)

s1.score = 90

print(s1.age)


