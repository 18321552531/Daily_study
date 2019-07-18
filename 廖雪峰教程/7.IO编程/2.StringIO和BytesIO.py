# -*- coding: utf-8 -*-
# @Time    : 2019-07-13  21:31
# @File    : 2.StringIO和BytesIO.py
# @Author  : 啊啊
'''
第二节 StringIO BytesIO
很多时候文件的读不一定是文件，也可以在内存中读写。
'''

'''
StringIO是指在内存中读写文件
'''

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
f.write('\nhello world!')

print(f.getvalue())

'''
BytesIO主要用来操作二进制数据。
'''

from io import BytesIO
b = BytesIO()
b.write('朱绳祖'.encode('utf-8'))
print(b.getvalue())