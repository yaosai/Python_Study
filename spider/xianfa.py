#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re

import requests

from bs4 import BeautifulSoup

res = requests.get("http://www.law-lib.com/law/law_view1.asp?id=327")
res.encoding = "gb2312"

newr = res.text.replace('<br/>', '')
print(newr)
pattern = re.compile(r'<br>[\s\S]<br>([\s\S]*?)。<br>[\s\S]<br>', re.S)
print(pattern)
soup = BeautifulSoup(newr, 'html.parser')
print(soup)
