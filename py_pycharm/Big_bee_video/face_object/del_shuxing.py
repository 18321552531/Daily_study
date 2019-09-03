# -*- coding: utf-8 -*-
# @Time    : 2019-09-03  21:47
# @File    : del_shuxing.py
# @Author  : 啊啊

class Animal(object):
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def print_animal(self):
        print(self.name, self.age, self.color)


cat = Animal('bob', 'black', 22)

'''
析构方法
__del__
'''
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('对象已创建！')
    # def __del__(self):
    #     print('对象已销毁！')

bob = Student('Bob', 10)

print(bob.__class__)
print(bob.__dict__)







