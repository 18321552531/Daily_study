# -*- coding: utf-8 -*-
# @Time    : 2019-07-09  14:58
# @File    : 4.继承和多态.py
# @Author  : 啊啊
'''
第四节：继承和多态
在OOP程序中，我们定义一个class的时候，可以从某个现有的class继承。
新的class称为子类，而被继承的class为父类或者基类。
'''

class Animal(object):

    def run(self):
        print('Animal is running....')

class Dog(Animal):
    pass

class Cat(Animal):

    def run(self):
        print('Cat is running.....')
    pass

if __name__ == '__main__':
    dog = Dog().run()
    cat = Cat().run()
    # print(isinstance(Dog(), Animal))
    def run_twice(animal):
        animal.run()
        animal.run()
    run_twice(Animal())




