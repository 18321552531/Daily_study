# -*- coding: utf-8 -*-
# @Time    : 2019-08-30  13:16
# @File    : try_except.py
# @Author  : 啊啊

def average_apple(n):
    '''

    :param n:苹果的个数
    :return:
    '''
    member = int(input('有几个人：'))
    average = n/member
    print('没人分到%s'%(average))
    pass


# try:
#     print('开始分苹果')
#     average_apple(29)
#     print('结束分苹果')
# except ValueError:
#     print('输入的值不为整数')
# else:
#     print('正常分完')
# finally:
#     print('结束！')

'''
练习：创建一个函数get_score()来获取学生的成绩（1-100）
如果出现异常返回0，否则返回用户输入的成绩。
'''

def get_score():
    try:
        s = int(input('请输入一个成绩：'))
    except ValueError:
        return 0
    return s

score = get_score()
print(score)
