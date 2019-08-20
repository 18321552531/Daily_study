#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################
# > File Name: hello.py
# > Author: zszaa
# > Mail: zszaa_0805@163.com
# > Created Time: 2019-08-18 16:29:41
##########################################

def application(environ, start_response):
    start_response('200 OK' ,[('Content_Type', 'text/html')])
    return [b'<h1>hello python</h1>']

