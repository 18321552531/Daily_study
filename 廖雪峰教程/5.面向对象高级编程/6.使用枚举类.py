# -*- coding: utf-8 -*-
# @Time    : 2019-07-13  00:04
# @File    : 6.使用枚举类.py
# @Author  : 啊啊
'''
第六节 使用枚举类
from enum import Enum
'''

from enum import Enum

Weekend = Enum('weekend',
               ('Sun', 'Mon', 'Tue', 'Wed',
                'Thu', 'Fri', 'Sat'))
# for name, member in Weekend.__members__.items():
#     print(name, '===>', member, ',', member.value)

for date in Weekend:
    print(date.name, '====>', date, ',', date.value)


print(Weekend)


