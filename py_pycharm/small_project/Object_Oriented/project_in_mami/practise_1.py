# -*- coding: utf-8 -*-
# @Time    : 2019-08-04  23:20
# @File    : practise_1.py
# @Author  : 啊啊
'''
一：定义一个学生类。有下面的类属性：
1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
zm = Student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100
'''

class Students(object):
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.course)

zm = Students('zhangming', 20, [69, 88, 100])


'''
二：定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
'''

class Dictclass(object):
    def __init__(self, dict):
        self.dict = dict
    def get_dict(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return 'No key!'

    def del_dict(self, key):
        if key in self.dict:
            self.dict.pop(key)
        else:
            return 'No key!'
    def print_dict(self):
        return self.dict

    def update_dict(self, dict2):
        self.dict = dict(self.dict, **dict2)
        return self.dict.values()
#
# dict_a = {'a': 1, 'b': 2}
# A = Dictclass(dict_a)
# print(A.get_dict('c'))
# print(A.del_dict('a'))
# print(A.print_dict())
# A.update_dict({'c': 3})
# print(A.print_dict())

'''
定义一个列表的操作类：Listinfo
包括的方法:
1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key()
list_info = Listinfo([44,222,111,333,454,'sss','333'])
'''

class Listinfo(object):
    def __init__(self, list_val):
        self.varlist = list_val

    def print_varlist(self):
        return self.varlist

    def add_key(self, keyname):
        if isinstance(keyname, (int, str)):
            self.varlist.append(keyname)
            return self.varlist
        else:
            return 'error!'

    def get_key(self, num):
        if 0<= num <= len(self.varlist):
            return self.varlist[num]
        else:
            return 'error!'

    def update_list(self, list2):
        if isinstance(list2, list):
            self.varlist.extend(list2)
            return self.varlist
        else:
            return 'error!'

    def del_key(self, ):
        # 删除并且返回最后一个元素
        return self.varlist.pop()

list_info = Listinfo([44,222,111,333,454,'sss','333'])
#
# print(list_info.add_key('zsz'))
# print(list_info.get_key(3))
# print(list_info.update_list([2,5,5]))
# print(list_info.del_key())

'''
定义一个集合的操作类：Setinfo
包括的方法:
1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
set_info =  Setinfo(你要操作的集合)
'''

class Setinfo(object):
    def __init__(self, info):
        self.info = info
    def print_info(self):
        return self.info

    def add_setinfo(self, keyname):
        if isinstance(keyname, (str, int)):
            self.info.add(keyname)
            return self.info
        else:
            return "error!"

    def get_intersection(self, set1):
        if isinstance(set1, set):
            return self.info & set1
        else:
            return 'error!'

    def get_union(self, set1):
        if isinstance(set1, set):
            return self.info | set1
        else:
            return 'error!'

    def get_differents(self, set1):
        if isinstance(set1, set):
            return self.info - set1
        else:
            return 'error!'

A = set([1, 2, 3, 4, 5, 2])
B = set([5, 6, ])
set_info = Setinfo(A)
# print(set_info.print_info())
# print(set_info.add_setinfo(6))
# print(set_info.get_intersection(B))
# print(set_info.get_differents(B))


'''
题目一： 写一个网页数据操作类。完成下面的功能：
提示：需要用到urllib模块
get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int
get_htmlcontent() 获取网页的内容。返回类型:str
get_linknum()计算网页的链接数目。
'''
