# -*- coding: utf-8 -*-
# @Time    : 2019-09-07  16:29
# @File    : practise_bike.py
# @Author  : 啊啊

"""
练习：
写一个Bicycle的类有run的方法
"""


class Bicycle(object):
    def run(self,km):
        print('自行车骑行了%s千米'%km)
        print('----------------------')

class EBicycle(Bicycle):
    def __init__(self,vol):
        self.vol = vol

    def vol_add(self,value):
        if value >= 0:
            self.vol = self.vol + value
        else:
            raise ValueError

    def show_vol(self):
        print('电瓶车目前的电量为 %s vol'%self.vol)
        print('----------------------')

    def run(self,km):
        max_dis = 10*self.vol
        if km <= max_dis:
            print('电瓶车行驶了%s千米'%km)
            print('----------------------')
            self.vol = self.vol - km/10
        else:
            print('电瓶车行驶了%s千米'%(self.vol*100))
            print('----------------------')
            super().run(km-max_dis)

b = Bicycle()
b.run(10)
e = EBicycle(5)
e.run(10)
e.show_vol()
e.run(100)
e.vol_add(10)
e.run(180)


