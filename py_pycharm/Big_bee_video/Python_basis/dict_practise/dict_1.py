# -*- coding: utf-8 -*-
# @Time    : 2019-08-25  00:08
# @File    : dict_1.py
# @Author  : 啊啊

'''
字典 dict
1.字典是一种可变的容器，可以存储任意的数据类型
2.字典中的数据都是用键（key）来进行索引的
3.字典的存储是无序的
4.字典中的数值主要通过 key-value 进行映射。
5.字典的键不能重复，且只能是不可变的值作为字典的键
'''
'''
不可变类型有:
int, float, complex, bool, str, tuple, frozenset(固定集合), bytes(字节串)
可变类型：
list, dict, set(集合)[frozenset 不可变], bytearry(字节数组)
'''

# d = {['aa','bb'], ['11','22']}
d = dict()
d['name'] = 'zszaa' #增
d['age'] = 18   #增
d['age'] = 134  #改
del d['age']    #删

'''
可以用in/not in来判断键是否存在于字典中
'''

if 'name' in d:
    print('name is in d')

'''
字典的迭代访问
字典只能对键进行迭代访问
'''
d['age'] = 12
d['address'] = 'china'
for i in d:
    print(d[i])
'''
可用于字典的内建函数
len()    字典中键值对的个数
max()    字典中键的最大值
min()    字典中键的最小值
sum()    字典中所有键的和
any()    真值测试，只对键进行操作，其中一个为True则为真
all()    真值测试，全为真是，返回true
update() 将新字典合并到旧字典，则此键的值取新字典的值
'''
d2 = {'school':'quzhouy1zhong', 'money':'no'}
d[''] = 3
# print(len(d))
# print(any(d))
# print(all(d))
d.update(d2)
new_dic = d
# print(d.get('naa','无此键'))

# for k, v in d.items():
#     print('键：%s, 值：%s'%(k,v), end=' ')


'''
输入一串字符，输出出现过的字符和他出现过的次数
'''

# input_str = input('输入一串字符:')

# 方法一：
example_str = 'aasdfbfdsaf'
list_str = list(set(list(example_str)))
freq_lis = []
for i in list_str:
    freq = 0
    for j in list(example_str):
        if i == j:
            freq += 1
    freq_lis.append(freq)
dic = dict(zip(list_str, freq_lis))




# 方法二
d = dict()
for i in example_str:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] = d[i]+1

'''
字典推导式
{键表达式：值表达式 for 变量 in 可迭代对象 [if 真值表达式]}
d = {x: x**2 for x in range(1,4)}
'''

l = ['fsadf', 'fasdf','fsad']

d = {x: len(x) for x in l}
print(d)


