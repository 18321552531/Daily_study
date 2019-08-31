#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: try_finally.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-30 23:36:15
##########################################


# try_finally的练习

'''
以煎鸡蛋为例子，
1.打开天然气
2.煎鸡蛋
3.关闭天然气（必须做）
'''

def fire_agg():
    try:
        print('打开天然气')
        agg = int(input('请输入鸡蛋个数：'))
        print('完成煎蛋。')
    finally:
        print('关闭天然气')

egg = fire_agg()
