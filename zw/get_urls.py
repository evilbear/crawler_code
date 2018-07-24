# coding=utf-8
import os, re, json, random, socket
import urllib.request
from bs4 import BeautifulSoup
import numpy as np

#爬虫参数
headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
headers2 = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'}
socket.setdefaulttimeout(10)#超时10s

year_url = 'http://www.laoziliao.net/rmrb/'
year_req = urllib.request.Request(url=year_url,headers=headers1)
year_response = urllib.request.urlopen(year_req)
year_soup = BeautifulSoup(year_response,'html.parser',from_encoding='utf-8')
year_links=year_soup.find('div',id='box').find_all('a')
years_url = []
for link in year_links:
    years_url.append(link.get("href"))

print(years_url[0])
months_url = []
for year_ in years_url:
    try:
        month_req = urllib.request.Request(url=year_,headers=headers2)
        month_response = urllib.request.urlopen(month_req)
        month_soup = BeautifulSoup(month_response,'html.parser',from_encoding='utf-8')
        month_links=month_soup.find('div',id='month_box').find_all('a')
        for link in month_links:
            months_url.append(link.get("href"))
    except:
        pass

print(len(months_url))
days_url = set()
for month_ in months_url:
    day_req = urllib.request.Request(url=month_,headers=headers1)
    day_response = urllib.request.urlopen(day_req)
    day_soup = BeautifulSoup(day_response,'html.parser',from_encoding='utf-8')
    day_links=day_soup.find('div',class_='box').find_all('a')
    for link in day_links:
        temp = link.get("href")
        days_url.add(re.sub(r'#.*$', '', temp))
        

urls_path = os.path.dirname(os.path.abspath(__file__)) + '/urls.txt'
urls_data = open(urls_path, 'w')
for i in days_url:
    urls_data.write(i+'\n')
urls_data.close()


