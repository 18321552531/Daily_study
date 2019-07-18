# -*- coding: utf-8 -*-
# @Time    : 2019-07-09  23:48
# @File    : 6.实例属性和类属性.py
# @Author  : 啊啊
'''
第六节 实例属性和类属性
 什么时候要加（）？？？？？？？？？？？
'''

#根据类创建的实例可以任意绑定属性，
#给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    name = 'Student'

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':

    print(Student.name)
    student = Student()
    student.name = 'aa'
    print(student.name)

'''
####啥时候要加括号啊啥时候不加括号啊？？？？？？？？？
##定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
'''

