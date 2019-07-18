# -*- coding: utf-8 -*-
# @Time    : 2019-07-08  23:28
# @File    : 2.类和实例.py
# @Author  : 啊啊

'''
第二节 面对对象最重要的就是类（class）和实例（instance）
'''

#在python中定义类是根据class关键字：
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def print_score(self):
        print('姓名：%s，成绩：%s' % (self.name, self.score))

    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score > 60:
            return 'B'
        else:
            return 'C'

if __name__ == '__main__':
    Bob = Student('Bob', 16, 85)
    Bob.print_score()
    print(Bob.get_grade())


