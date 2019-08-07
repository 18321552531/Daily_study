# -*- coding: utf-8 -*-
# @Time    : 2019-08-07  20:56
# @File    : sort1.py
# @Author  : 啊啊


import pandas as pd
#数据集
df = pd.DataFrame({'word':['a','b','b'], 'num':[2,6,1,]})
print(df)
#自定义排序顺序，此顺序对应为升序ascending=True
list_sorted = ['b', 'a', 'c']
#对相关列进行自定义排序
df['word'] = df['word'].astype('category').cat.set_categories(list_sorted)
#结果
df_sortes = df.sort_values(by=['word'], ascending=True)

print(df_sortes)

