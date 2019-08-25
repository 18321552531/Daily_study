# -*- coding: utf-8 -*-
# @Time    : 2019-08-24  22:56
# @File    : while_.py
# @Author  : 啊啊

# 输入begin和end，输出之间的数值

'''
begin = int(input('输入一个开始的整数：'))
end = int(input('输入结束的数值:'))

while begin <= end:
    if begin % 5 == 0:
        print(begin)
        begin += 1
    else:
        print(begin, end=' ')
        begin += 1

'''

'''
用while打印出直角三角形
'''

# right_angle = int(input('输入直角三角形的直角边:'))
#
# i = 1
# while i <= right_angle:
#     print('*' * i)
#     i = i+1

# contine


for i in range(5):
    if i == 3:
        print(i)
        break

sum = 0
for i in range(1,101):
    if (i % 5 != 0)and(i % 7 != 0)and(i % 11 != 0):
        sum += i
print(sum)



