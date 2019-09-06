# -*- coding: utf-8 -*-
# @Time    : 2019-09-06  19:37
# @File    : super_.py
# @Author  : 啊啊

'''
此示例示意子类对象显示调用基类的__init__
'''

class Human(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print('name is :%s'%self.name)
        print('age id :%s'%self.age)


class Student(Human):
    def __init__(self, name, age, score):
        super().__init__(name,age)
        self.score = score

    def show_info(self):
        super().show_info()
        print('score is %s'%self.score)

bob = Student('bob',18, 99)
bob.show_info()
    # @show_info.setter
    # def show_info(self, values):
    #     self.name = values





