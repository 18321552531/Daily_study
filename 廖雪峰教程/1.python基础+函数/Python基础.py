# -*- coding: utf-8 -*-
# @Time    : 2019/6/26  下午11:30
# @File    : Python基础.py
# @Author  : 啊啊


####第一节 数据类型和变量
##python的数据类型主要有整数、浮点数、字符串
#在字符串中出现‘或者“的时候要加转义字符。例如：

print('I\'m OK')

####第二节 字符串和编码
##ASCII编码是一个字节的，Unicode编码是两个字节的，目前采用unicode统一编码。
##Unicode编码太长了所以出现了UTF-8：把Unicode字符根据不同的数字打下编成1-6个字节
#其中英文字母Wie1个字节，汉字通常为三个字节，生僻字为6个字节。
#………………python中ord（）获取字符的整数表示，char（）将编码转化为相应的字符。
print(ord('a'))
print(chr(97))
print('\u4e2d\u6587')
#Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
#……………………python中bytes的数据用带b前缀的单引号或者双引号表示
print(b'abc')
##把str变为bytes用.encode // 把bytes变为str使用decode
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print(b'ABC'.decode())
##计算str包含多少字符串的时候可以用 len()函数
print(len('ABC'))
print(len('中文'))
print(len('中文'.encode('utf-8')))
###在输出时候可以用%实现对内容的替代
##%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
print('hello! %s ,you are only %d years old.come on!'%('朱绳祖',24))


####第三节使用list和tuple
list = ['aa','bb','cc']
print(len(list))
#pop()用来删除末尾元素
list.pop()
print(list)
###tuple和list十分类似但是初始化之后不能修改


####使用dict和set
###dict查询快
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['aa'] = 40
print(d.get('bb'))

###set和dict相类似，是key的集合，但是key中间不重复且无序
s = set([1, 1, 2, 2, 3, 3])
print(s)


