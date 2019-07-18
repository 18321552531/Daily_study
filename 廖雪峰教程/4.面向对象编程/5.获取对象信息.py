# -*- coding: utf-8 -*-
# @Time    : 2019-07-09  23:19
# @File    : 5.获取对象信息.py
# @Author  : 啊啊
'''
第五节 获取对象信息
判断对象的类型一般可以用 type（）
也可以用isinstance（）(优先使用)
还有dir（），获得一个对象的所有属性和方法
'''

#使用type（）
print(type(enumerate))
print(type(12.2) == type(12))

#使用isinstance()优先使用

# a = isinstance([1, 2, 23], (tuple, list))
# print(a)

#使用dir()
#还要配合 getattr(); setattr(); hasattr()等
print(dir('ads'))

class Myobject(object):
    def __init__(self):
        self.x = 123
    def power_self(self):
        return self.x *self.x

obj = Myobject()

a = hasattr(obj, 'x') #有x属性吗？
b = setattr(obj, 'y', 10) #设置一个y属性
c = getattr(obj, 'y')
y = obj.y
print(y)
print(c)



