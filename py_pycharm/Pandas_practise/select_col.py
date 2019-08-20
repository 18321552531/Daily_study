#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: select_col.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-19 22:07:22
##########################################


import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[3,4,56,7,7,8,2],
                   'b':[4,5,6,7,8,9,0],
                   'c':[3,5,6,7,8,9,235]})
df_table = df[(6<df['b'])&(df['b']<9)]
print(df_table)
print(df)
