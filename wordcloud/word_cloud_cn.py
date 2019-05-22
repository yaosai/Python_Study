#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @file: function_custom.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/10 18:10
# @desc: 中文词云


import os

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

path1 = os.path.abspath('.')  # 获取当前脚本所在的路径
path2 = os.path.abspath('..')  # 获取当前脚本所在路径的上一级路径
filename = path2 + "//wordCloudCN.txt"
with open(filename, encoding='utf-8') as f:
    mytext = f.read()
mytext = "  ".join(jieba.cut(mytext))
# print mytext
wordcloud = WordCloud(font_path=path2 + "//simsun.ttf").generate(mytext)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
