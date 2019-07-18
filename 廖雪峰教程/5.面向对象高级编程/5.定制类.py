# -*- coding: utf-8 -*-
# @Time    : 2019-07-12  23:07
# @File    : 5.定制类.py
# @Author  : 啊啊
'''
第五节 定制类
看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，
这些在Python中是有特殊用途的。(帮我们定制类)
'''

#__str__的功能：帮助打印好看的内部字符

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object:%s' % (self.name)
    __repr__ = __str__

# s = Student('bab')
# print(Student('Sam'))

# __iter__返回一个可以迭代的对象，法返回一个迭代对象，然后，
# Python的for循环就会不断调用该迭代对象的__next__(),遇到StopIteration之后退出循环
#写一个斐波那契数列

class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 20:
            raise StopIteration
        return self.a

print([i for i in Fib()])
# for i in Fib():
    # print(i)

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

class Fib_1(object):
    def __getitem__(self, item):
        a, b = 0, 1
        for i in range(item):
            a, b = b, a + b
        return a

print(Fib_1()[0])







