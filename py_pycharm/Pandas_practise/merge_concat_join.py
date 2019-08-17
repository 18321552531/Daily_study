# -*- coding: utf-8 -*-
# @Time    : 2019-08-17  14:39
# @File    : merge_concat_join.py
# @Author  : 啊啊
'''
merge/concat/join的练习(包括append)
'''
import pandas as pd
import numpy as np
import matplotlib as plt

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3'],},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7'],},
                   index=[0,1,2,4])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11'],},
                   index=[0,1,4,5])

df4 = pd.DataFrame({'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'F': ['D8', 'D9', 'D10', 'D11'],},
                   index=[2,3,5,6])
# concat部分
'''
df3.columns = df2.columns
result = pd.concat([df1, df4.reindex(df1.index)], join='inner', axis=1)

'''
s1 = pd.Series(['X0', 'X1', 'X2', 'X3'], name='X')
df_s1 = pd.concat([df1,s1,s1], axis=1)
result1 = pd.concat([df1, df2, df3],keys=['x','y','z'])
result2 = pd.concat({'x': df1, 'y': df2, 'z': df3})
# append部分
'''
result = df1.append(df4)
result1 = df1.append(df4, ignore_index=True)
'''
'传递dict'
'''
dicts = [{'A': 1, 'B': 2, 'C': 3, 'X': 4},]
df1 = df1.append(dicts)
print(df1)
'''

# merge部分

left = pd.DataFrame({'key': ['K0', 'K0', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'key1': ['A', 'A', 'C', 'E']},
                    index=[1,3,5,7])

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3'],
                     'key2': ['A', 'B', 'C', 'D']},
                     index=[1,2,3,4])

result = pd.merge(left, right, left_on='key1', right_on='key2', how='right')
result_a = pd.merge(left, right, left_on=['key','key1'], right_on=['key', 'key2'])
# print(result_a)

# join部分
# left.set_index('key', inplace=True)
right.set_index('key', inplace=True)
result_join = left.join(right, on='key')
print(result_join)


