# -*- coding: utf-8 -*-
# @Time    : 2019-07-24  23:58
# @File    : BeautifulSoup.py
# @Author  : 啊啊
'''
soup = BeautifulSoup(html, 'lxml')
'''
from bs4 import BeautifulSoup
import re

with open('web/new_index.html') as wb_data:
    html = BeautifulSoup(wb_data, 'lxml')
imgs = html.select('body > div.main-content > ul > li > img')
titles = html.select('body > div.main-content > ul > li > div > h3 > a')
tags = html.select('body > div.main-content > ul > li > div.article-info > p.meta-info ')
texts = html.select('body > div.main-content > ul > li > div.article-info > p.description')
sorces = html.select('body > div.main-content > ul > li > div.rate > span')
print(tags)
# print(img,title,tag,text,sorce, sep='\n------------------\n')
# print(zip(img,title,tag,text,sorce))

for img, title, tag, text, sorce in zip(imgs, titles, tags, texts,sorces):
    data = {
        'img': img.get('src'),
        'title': title.get_text(),
        'tag': list(tag.stripped_strings),
        'text': text.get_text(),
        'score': sorce.get_text()
    }
    print(data)