# -*- coding: utf-8 -*-
# @Time    : 2019-07-09  14:33
# @File    : 3.限制访问.py
# @Author  : 啊啊
'''
第三节：限制访问
在Class的内部，有属性和方法，而外部的代码可以调用实际变量的方法来操作数据，外部的代码可以随意的修改里面的属性
如果为了让内部的属性不被外部访问，可以在属性的名称前面加两个__,使其变为私有变量。
'''

class Student(object):

    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def print_age(self):
        print("姓名：%s, 年龄：%s" % (self.__name, self.__age))

    def print_score(self):
        print("姓名：%s, 分数：%s" % (self.__name, self.__score))


#练习：请把下面的Student对象的gender字段对外隐藏起来，
#用get_gender()和set_gender()代替，并检查参数有效性：
class Student1(object):

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def print_gender(self):
        print("姓名：%s, 性别：%s" % (self.name, self.__gender))

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ['male', 'female']:
            self.__gender = gender
        else:
            raise ValueError('wrong gender')

if __name__ == '__main__':
    sam = Student1("sam", 'male')
    sam.set_gender('female')
    sam.print_gender()







