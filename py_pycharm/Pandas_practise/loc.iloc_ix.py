# -*- coding: utf-8 -*-
# @Time    : 2019-09-10  21:30
# @File    : loc.iloc_ix.py
# @Author  : 啊啊

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20).reshape(4, 5),
                  index=['a', 'b', 'c', 'd'],
                  columns=['A', 'B', 'C', 'D', 'E'])

print(df.ix['d', 'B'])
