# -*- coding: utf-8 -*-
# @Time    : 2019-09-05  13:20
# @File    : class_method.py
# @Author  : 啊啊

class Student(object):
    count = 0
    @classmethod
    def update_count(cls,num):
        return cls.count+num

s1 = Student()

print(s1.count)
print(s1.update_count(21))


