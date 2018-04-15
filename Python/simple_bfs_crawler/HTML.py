# coding : utf-8
import requests
from urllib.parse import urlparse
from urllib.parse import urljoin
import re
import os
from bs4 import BeautifulSoup


def get_html(url):
    try:
        par = urlparse(url)
        Default_Header = {'X-Requested-With': 'XMLHttpRequest',
                          'Referer': par[0] + '://' + par[1],
                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
                          'Host': par[1]}
        html = requests.get(url, headers=Default_Header, timeout=10)
        if html.status_code != 200:
            return None
        return html.content
    except Exception as e:
        print(e)
        return None


def full_link(url1, url2, flag_site=True):
    try:
        if url2[0] == '#':
            return None
        filepat = re.compile(r'(.*?)\.(.*?)')
        htmpat = re.compile(r'(.*?)\.htm$|(.*?)\.html$|(.*?)\.php$|(.*?)\.aspx$')
        u1 = urlparse(url1)
        if filepat.match(u1.path) and not htmpat.match(u1.path):
            return None
        if url1[-1] == '/':
            url1 = url1+"index.html"
        elif filepat.match(u1.path) is None:
            url1 = url1+"/index.html"
        url2 = urljoin(url1,url2)
        u2 = urlparse(url2)
        if u1.netloc!=u2.netloc and flag_site:
            return None
        return url2
    except Exception as e:
        print(e)
        return None


def premake(url):  # 建立url所需要的目录
    if url[-1] == '/':
        url = url[:-1]
    up = urlparse(url)
    pat = re.compile(r'(.*?)\.htm$|(.*?)\.html$|(.*?)\.php$|(.*?)\.aspx$')
    path = up.path.split('/')
    name = 'index.html'
    if pat.match(up.path) is not None:
        name = path[-1]
        path = path[:-1]
    dirn = '/'.join(path)
    if up.query!='':
        name = up.query+' - '+name
    os.makedirs(up.netloc + dirn, exist_ok=True)
    return up.netloc + dirn + '/' + name


def save(url):
    url = url.replace('\n','')
    fn = premake(url)
    html = get_html(url)
    if html is not None:
        with open(fn, 'wb') as f:
            f.write(html)
    return html

