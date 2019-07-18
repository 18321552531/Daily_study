# -*- coding: utf-8 -*-
# @Time    : 2019-07-12  22:25
# @File    : 4.多重继承.py
# @Author  : 啊啊
'''
第四节 多重继承
继承是面向对象编程的重要方式，通过继承子类可以继承父类的功能。
'''
'''
对下面四种动物分类。
Dog-----狗
Bat-----蝙蝠
Parrot---鹦鹉
Ostrich---鸵鸟
'''
#___________________#
'''
本节的后面提到了多线程和多进程的问题以后要继续回来看看。
多线程和多进程？？？？
'''

class Animal(object):
    def __init__(self):
        self.age = 12
        self.sex = 'male'
    pass

class Mammal(Animal):
    def __init__(self):
        self.age = 13
        self.sex = 'male'

    def mammal(self):
        print('它属于哺乳动物！')

class Bird(Animal):
    def bird(self):
        print('它属于鸟类！')

class Runable(Animal):
    def __init__(self):
        self.age = 14
        self.sex = 'male'

    def running(self):
        print('它会跑！')

class Flyable(Animal):
    def flying(self):
        print('它会飞！')

##对动物进行分类
class Dog(Mammal, Runable):
    pass
dog_type = Dog().mammal()
dog_active = Dog().running()
dog_age = Dog().age
print(dog_age)


class Bat(Mammal, Flyable):
    pass
class Parrot(Bird, Flyable):
    pass
class Ostrich(Bird, Runable):
    pass



