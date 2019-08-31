#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: raise.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-30 23:49:45
##########################################


# raise 练习


# 自动定义一个MyException的类,继承与Exceptin：
class MyException(Exception):
    def __init__(self, message):
        self.message = message

# 输入成绩如果不在0-100之间的话返回一个异常


def get_score():
    score = int(input('输入一个学生成绩:'))
    if score > 100:
        raise MyException('你输入的成绩太高了')
    if score < 0:
        raise MyException('你输入的成绩太低了')
    else:
        return score


try:
    a = get_score()
except MyException as err:
    print(err)
else:
    print(a)


