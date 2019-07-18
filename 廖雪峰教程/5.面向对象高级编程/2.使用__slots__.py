# -*- coding: utf-8 -*-
# @Time    : 2019-07-10  12:02
# @File    : 2.使用__slots__.py
# @Author  : 啊啊

'''
第二节 使用__slots__   ：slot（投放， 塞进）
可以用来限制class实例能添加的属性，
@@@@@@醉了 啥时候要加（）啥时候不加括号啊。
'''

class Student(object):
    pass

# 尝试给实例绑定一个属性：
student = Student()
student.name = 'Sam'

# 尝试给实例绑定一个方法：
def get_age(self, age):
    self.age = age


from types import MethodType
Student.get_age = get_age
student.get_age(16)
#另一个实例不起作用的
student2 = Student()
student2.get_age(19)
##添加__slots__  用来定义可以绑定的属性名称

class Animals(object):
    __slots__ = ('name', 'size')

animal = Animals()
animal.name = 'Flog'
animal.name = 'Dog'
animal.size = '16g'
# animal.age = '20'

class Animal(Animals):
    pass
a = Animal()
a.age = '16'
print(a.age)
# print(animal.age)
print(animal.name)




