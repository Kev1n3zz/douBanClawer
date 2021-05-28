# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os
import sqlite3
import csv
import pandas as pd

conn = sqlite3.connect('comment(1)(1).db')   # 链接到表格：
cursor = conn.cursor()  # 执行查询语句：
cursor.execute('select comment from comment')  # 使用featchall获得结果集（list）
values = cursor.fetchall()
cursor.close()  # 关闭cursor
conn.close()    # 关闭conn
# print(values)   # result:[('1', 'Michael')]


data = pd.DataFrame(values)
data.to_csv('douBanComment.txt', sep='\t',index=0,header=0)


source = open('douBanComment.txt', "r", encoding='gb18030', errors='ignore')
line = source.readlines()   # 获取情感分数

sentimentslist = []
for i in line:
    s = SnowNLP(i.encode("utf-8").decode("utf-8"))
    # print(s.sentiments)
    sentimentslist.append(s.sentiments)

#区间转换为[-0.5, 0.5]
result = []
i = 0
while i<len(sentimentslist):
    result.append(sentimentslist[i]-0.5)
    i = i + 1

#可视化画图
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(0, 100, 1), result, 'k-')
plt.xlabel('PeopleID')
plt.ylabel('Sentiment')
plt.title('Analysis of Sentiments')
plt.show()
