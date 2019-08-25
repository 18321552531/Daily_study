# -*- coding: utf-8 -*-
# @Time    : 2019-08-19  23:25
# @File    : Sql_test.py
# @Author  : 啊啊

import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'zszaa0805',
    'db': 'Mysql_test',
}
name = 'admin'
db = pymysql.connect(**config)
cursor = db.cursor()
cursor.execute('select max(ID) from signin_table')
id_max = cursor.fetchall()
print(id_max[0][0])
cursor.execute(r"select * from signin_table where username like '%s' " %name)
res = cursor.fetchall()
print(res[0][2])
# print(res.values())
if res == ():
    print('ok')
# if res[0]:
#     print('ok')
print(res)



