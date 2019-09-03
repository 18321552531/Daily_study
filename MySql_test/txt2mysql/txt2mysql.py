# -*- coding: utf-8 -*-
# @Time    : 2019-08-27  11:10
# @File    : txt2mysql.py
# @Author  : 啊啊

import pandas as pd
import numpy as np
import pymysql
import time
# 连接数据库
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'zszaa0805',
    'db': 'Mysql_test',
}

db = pymysql.connect(**db_config)
db.autocommit(1)
cursor = db.cursor()

# sql语句
sql = 'insert into jiaoyiliushui(kmh,dfkmh,hbh,zh,zhxh,zl,jgdm,dljg,jyrq,jysj,jym,jyje,zhye,' \
      'zhjs,zy,dycs,pzzl,pzhm,jdbz,pzbz,tdbz,jzgy,fhgy,gylsh,dyzh,dac) values ' \
      '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

month = ['01','02','03','04','05','06','07','08','09','10','11','12']

# 导入数据
load = '/Users/zhushengzu/python_load/MySql_test/data/188510/188510_2007%s.txt'



# values = (int(df.iloc[1,0]),str(df.iloc[1,1]),int(df.iloc[1,2]),str(df.iloc[1,3]),int(df.iloc[1,4]),
#           str(df.iloc[1,5]),int(df.iloc[1,6]),int(df.iloc[1,7]),str(df.iloc[1,8]),str(df.iloc[1,9]),
#           int(df.iloc[1,10]),float(df.iloc[1,11]),float(df.iloc[1,12]),float(df.iloc[1,13]),int(df.iloc[1,14]),
#           int(df.iloc[1,15]),int(df.iloc[1,16]),str(df.iloc[1,17]),int(df.iloc[1,18]),int(df.iloc[1,19]),
#           int(df.iloc[1,20]),int(df.iloc[1,21]),int(df.iloc[1,22]),int(df.iloc[1,23]),str(df.iloc[1,24]),
#           str(df.iloc[1,25]))
# cursor.execute(sql,values)
# df = pd.read_table(load % '03', header=None, sep='|', error_bad_lines=False, encoding='latin-1', low_memory=False)
#
# print(df.dtypes)

#
start_time =time.time()
for j in month[2:]:
    df = pd.read_table(load%j, header=None, sep='|', error_bad_lines=False, encoding='latin-1', low_memory=False)
    df = df.where(pd.notnull(df), None)
    for i in range(1,len(df)):
        values = (str(df.iloc[i, 0]), str(df.iloc[i, 1]), int(df.iloc[i, 2]), str(df.iloc[i, 3]), int(df.iloc[i, 4]),
                  str(df.iloc[i, 5]), str(df.iloc[i, 6]), str(df.iloc[i, 7]), str(df.iloc[i, 8]), str(df.iloc[i, 9]),
                  str(df.iloc[i, 10]), str(df.iloc[i, 11]), str(df.iloc[i, 12]), str(df.iloc[i, 13]),
                  str(df.iloc[i, 14]),
                  str(df.iloc[i, 15]), str(df.iloc[i, 16]), str(df.iloc[i, 17]), str(df.iloc[i, 18]), str(df.iloc[i, 19]),
                  str(df.iloc[i, 20]), str(df.iloc[i, 21]), str(df.iloc[i, 22]), str(df.iloc[i, 23]), str(df.iloc[i, 24]),
                  str(df.iloc[i, 25]))
        cursor.execute(sql,values)
        if i % 1000 == 0:
            print('第%s个月第%s行'%(j,i))
end_time = time.time()
print('ok')
print('总共用时%s分钟'%((end_time-start_time)/60))




