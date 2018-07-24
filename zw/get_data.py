# coding=utf-8
import os, re, json, random, socket, codecs, chardet
import urllib.request
from bs4 import BeautifulSoup
import numpy as np
from itertools import islice

urls_path = os.path.dirname(os.path.abspath(__file__)) + '/urls.txt'
urls_data = open(urls_path, 'r')
data_path = os.path.dirname(os.path.abspath(__file__)) + '/data.txt'
data = open(data_path, 'a')

urls = []
for line in urls_data:
    line = line.strip()
    urls.append(line)
urls_data.close()

#爬虫参数
headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
headers2 = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'}
socket.setdefaulttimeout(10)#超时10s

for url in urls:
    try:
        if(random.randint(0,1)):
            headers = headers1
        else:
            headers = headers2
        req = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
        links=soup.find_all('div',class_='article')
        for n in links:
            temp = n.get_text()
            temp = re.sub(r"\s{2,}", " ", temp)
            temp = temp.strip().split(' ')
            lines = ''
            for line in temp[2:]:
                lines += line
            data.write(lines+'\n')
    except:
        continue
data.close()