# -*- coding: utf-8 -*-
# @Time    : 2019-07-08  22:34
# @File    : 1.面向对象编程简介.py
# @Author  : 啊啊
'''
第一节 面向对象编程（Object Oriented Programming）
数据封装、继承和多态是面向对象的三大特点
'''

student1 = {'name': 'Sam', 'score': '99'}
student2 = {'name': 'Bob', 'score': '97'}

#面向过程
# def print_score(student):
#     print('%s: %s' % (student['name'], student['score']))
#
# print_score(student1)

#面向过程
class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


Bob = student('Bob', 39)
Bob.print_score()

