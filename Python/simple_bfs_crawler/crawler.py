# coding : utf-8
import queue
import HTML
import math
from bs4 import BeautifulSoup
import os

inipool = []
with open('pool.txt', 'r') as f:
    for line in f.readlines():
        if line!='\n':
            inipool.append(line.replace('\n', ''))
pool = set()
q = queue.Queue()
for i in inipool:
    if i not in pool:
        pool.add(i)
        q.put((i, 1))
inp = input("请输入全网抓取还是站内抓取（1.全网抓取；2.站内抓取）：")
if inp == '1':
    flag_site = False
else:
    flag_site = True
inp = input("请输入最大网页抓取个数（无穷大请输入-1）：")
if inp == '-1':
    flag_most = math.inf
else:
    flag_most = int(inp)
inp = input("请输入宽度优先搜索最大抓取深度（无穷大请输入-1）：")
if inp == '-1':
    flag_depth = math.inf
else:
    flag_depth = int(inp)

now = 0
while not q.empty():
    try:
        front = q.get()
        link = front[0]
        depth = front[1]
        print('crawling:', link)
        html = HTML.save(link)
        if html is None:
            continue
        soup = BeautifulSoup(html, 'html.parser', from_encoding='gb18030')
        for a in soup.find_all('a'):
            try:
                url2 = a['href']
                fl = HTML.full_link(link, url2, flag_site)
                if fl is None:
                    continue
                if (fl not in pool) and (depth + 1 <= flag_depth):
                    pool.add(fl)
                    q.put((fl, depth + 1))
                    print('in queue:', fl)
            except Exception as e:
                print(e)
        now += 1
        if now >= flag_most:
            break
    except Exception as e:
        print(e)
