# 基于结巴分词和set，速度较慢。
# coding : utf-8
import os
import jieba

biao = set()
with open("keywords", "r", encoding="utf-8") as f:
    for line in f.readlines():
        word = line.replace("\n", "")
        if word not in biao:
            biao.add(word)

s = input("请输入待过滤字符串：")
seg = jieba.cut(s)
res = ""
for i in seg:
    if i in biao:
        res += "*"*len(i)
    else:
        res += i
print(res)
