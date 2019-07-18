# -*- coding: utf-8 -*-
# @Time    : 2019-07-10  23:18
# @File    : 3.使用@property.py
# @Author  : 啊啊

'''
第三节 使用@property（） ：property意思是属性、财产、性质
在绑定属性时候，属性直接暴露可以直接改，使用@property可以防止属性被修改。
要多看看看装饰器
'''
#为了限制输入数值的范围可以设置，set_score()/get_score()

class Student(object):
    # def __init__(self, score):
    #     self.score = score

    def get_score(self):
        print('成绩为：%s'%(self.score))

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数应该为整数!')
        if value > 100 or value < 0:
            raise ValueError('分数应该在0-100之间！')
        self.score = value





student = Student()
student.set_score(40)
student.get_score()





