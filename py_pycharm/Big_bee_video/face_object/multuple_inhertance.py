# -*- coding: utf-8 -*-
# @Time    : 2019-09-09  13:11
# @File    : multuple_inhertance.py
# @Author  : 啊啊


class Car(object):
    def run(self,speed):
        print('car speed is %s'%speed)

class Plane(object):
    def fly(self,speed):
        print('plane speed is %s'%(speed))
    def run(self,speed):
        print('plane speed is %s' % speed)


class PlaneCar(Plane,Car):
    pass

p = PlaneCar()

p.fly(23)
p.run(33)


#
# MRO查找示例
# print(PlaneCar.__mro__)


class Mylist(list):
    def insert_head(self,value):
        return self.insert(0,value)

l = Mylist([1,2,34,3])
l.insert_head(0)
print(l)




