# coding : utf-8
import os
import re

l = 0
with open('index.txt', 'w', encoding='utf-8') as f:
    for parent, dirnames, filenames in os.walk(".\\"):
        for fn in filenames:
            pat = re.compile(r'(.*?)\.htm$|(.*?)\.html$|(.*?)\.php$|(.*?)\.aspx$')
            if pat.match(fn) is None:
                continue
            fullname = parent + '\\' + fn
            # fulllink = fullname.replace('.\\', 'http://').replace('\\', '/').replace('noname.html', '')
            print(fullname)
            f.write(fullname)
            f.write('\n')
            l += 1
print(l)
input()