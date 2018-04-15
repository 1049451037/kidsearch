# 基于set，速度较快，但是只能处理字符串长度为5以内的敏感词。
# coding : utf-8

biao = set()
with open("keywords", "r", encoding="utf-8") as f:
    for line in f.readlines():
        word = line.replace("\n", "")
        if word not in biao:
            biao.add(word)

# s = input("请输入待过滤字符串：")
# seg = jieba.cut(s)
# res = ""
# for i in seg:
    # if i in biao:
        # res += "*"*len(i)
    # else:
        # res += i
# print(res)
s = input("请输入待过滤字符串：")
l = len(s)
v = [True]*l
for ll in range(5):
    for i in range(l-ll):
        if v[i] and s[i:i+ll+1] in biao:
            for j in range(i,i+ll+1):
                v[j]=False
res = ""
for i in range(l):
    if v[i]:
        res += s[i]
    else:
        res += "*"
print(res)