#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.sina.com.cn/china/')
res.encoding = "utf-8"
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
for news in soup.select('a'):
    if len(news.select('img')) > 0:
        h2 = news.select('img')[0]
        print(h2)
