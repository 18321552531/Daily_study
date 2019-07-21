# -*- coding: utf-8 -*-
# @Time    : 2019-07-21  00:06
# @File    : mami_test1.py
# @Author  : 啊啊
'''
编写程序, 编写一个学生类,
要求有一个计数器的属性, 统计总共实例化了多少个学生
'''

class Student(object):
    '''学生的类'''
    count = 0
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1  #要使得变量全局有效，则定义为类的属性

    def print_learn(self):
        print('%s is learning!' % (self.name))



stu1 = Student('jack', 99)
stu1.name = 'Lily'
stu2 = Student('Bob', 98)
print(stu1.count)

stu1.print_learn()



