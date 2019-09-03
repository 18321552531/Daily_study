#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: object_02.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-09-02 22:27:04
##########################################


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    
    def show_info(self):
        print(self.name,'今年', self.age,'分数', self.score)

student1 = Student('xiaoming', '20', '99')

student1.show_info()
