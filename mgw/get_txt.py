# coding=utf-8
import os, random, socket
import urllib.request
from bs4 import BeautifulSoup


#爬虫参数
headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
headers2 = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'} 
socket.setdefaulttimeout(10)#超时10s


#更新urls，返回增量部分
def fun_urls(name):
    urls = set()
    old_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/urls/' + name + '_urls.txt'
    new_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/urls/' + name + '_new.txt'
    if os.path.exists(old_path):
        old_urls, new_urls = set(), set()
        old_data = open(old_path, 'r')
        for line in old_data:
            old_urls.add(line[:-1])
        old_data.close()
        new_data = open(new_path, 'r')
        for line in new_data:
            new_urls.add(line[:-1])
        new_data.close()
        urls = new_urls - old_urls
        os.remove(new_path)
        if not urls :
            pass
        else:
            old_data = open(old_path, 'a')
            for i in urls:
                old_data.write(i)
                old_data.write('\n')
            old_data.close()
    else:
        os.rename(new_path, old_path)
        old_data = open(old_path, 'r')
        for line in old_data:
            urls.add(line[:-1])
        old_data.close()
    return urls


###获取http://mongol.cctv.com/的增量正文
urls_cctv_add = fun_urls('cctv')
if not urls_cctv_add:
    pass
else:
    cctv_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/cctv.txt'
    cctv_data = open(cctv_path, "w")
    for url in urls_cctv_add:
        try:
            if(random.randint(0,1)):
                headers = headers1
            else:
                headers = headers2
            req = urllib.request.Request(url=url,headers=headers)
            response = urllib.request.urlopen(req)
            soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
            try:
                links=soup.find('div', id='htmltext').find_all('p')
                for link in links:
                    try:
                        data = link.get_text()
                        data = data + '\n'
                        cctv_data.write(data)
                    except:
                        continue
            except:
                continue
        except:
            continue
    cctv_data.close()


###获取http://www.mongolcnr.cn/的增量正文
urls_cnr_add = fun_urls('cnr')
if not urls_cnr_add:
    pass
else:
    cnr_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/cnr.txt'
    cnr_data = open(cnr_path, "w")
    for url in urls_cnr_add:
        try:
            if(random.randint(0,1)):
                headers = headers1
            else:
                headers = headers2
            req = urllib.request.Request(url=url,headers=headers)
            response = urllib.request.urlopen(req)
            soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
            try:
                links=soup.find('div', id='htmltext').find_all('p')
                for link in links:
                    try:
                        data = link.get_text()
                        data = data + '\n'
                        cnr_data.write(data)
                    except:
                        continue
            except:
                continue
        except:
            continue
    cnr_data.close() 


###获取http://mongol.people.com.cn/的增量正文
urls_people_add = fun_urls('people')
if not urls_people_add:
    pass
else:
    people_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/people.txt'
    people_data = open(people_path, "w")
    for url in urls_people_add:
        try:
            if(random.randint(0,1)):
                headers = headers1
            else:
                headers = headers2
            req = urllib.request.Request(url=url,headers=headers)
            response = urllib.request.urlopen(req)
            soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
            try:
                links=soup.find('td',class_='zhengwen').find_all('td', class_='td_content')
                for link in links:
                    try:
                        data = link.get_text()
                        data = data + '\n'
                        people_data.write(data)
                    except:
                        continue
            except:
                continue
        except:
            continue
    people_data.close()

    
###获取http://mongol.people.com.cn/306956/的增量正文
urls_cpc_add = fun_urls('cpc')
if not urls_cpc_add:
    pass
else:
    cpc_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/cpc.txt'
    cpc_data = open(cpc_path, "w")
    for url in urls_cpc_add:
        try:
            if(random.randint(0,1)):
                headers = headers1
            else:
                headers = headers2
            req = urllib.request.Request(url=url,headers=headers)
            response = urllib.request.urlopen(req)
            soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
            try:
                links=soup.find('td',class_='zhengwen').find_all('td', class_='td_content')
                for link in links:
                    try:
                        data = link.get_text()
                        data = data + '\n'
                        cpc_data.write(data)
                    except:
                        continue
            except:
                continue
        except:
            continue
    cpc_data.close()

 
###获取http://www.nmg.xinhuanet.com/mg/的增量正文
urls_xinhua_add = fun_urls('xinhua')
if not urls_xinhua_add:
    pass
else:
    xinhua_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/xinhua.txt'
    xinhua_data = open(xinhua_path, "w")
    for url in urls_xinhua_add:
        try:
            if(random.randint(0,1)):
                headers = headers1
            else:
                headers = headers2
            req = urllib.request.Request(url=url,headers=headers)
            response = urllib.request.urlopen(req)
            soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
            try:
                links=soup.find('div', class_='c_content').find_all('p')
                for link in links:
                    try:
                        data = link.get_text()
                        data = data + '\n'
                        xinhua_data.write(data)
                    except:
                        continue
            except:
                continue
        except:
            continue
    xinhua_data.close()


###获取http://www.xingandaily.com/的增量正文
urls_xingan_add = fun_urls('xingan')
if not urls_xingan_add:
    pass
else:
    xingan_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/xingan.txt'
    xingan_data = open(xingan_path, "w")
    for url in urls_xingan_add:
        try:
            if(random.randint(0,1)):
                headers = headers1
            else:
                headers = headers2
            req = urllib.request.Request(url=url,headers=headers)
            response = urllib.request.urlopen(req)
            soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
            try:
                links=soup.find('span',id='ctl00_cph_Description').find_all('span')
                for link in links:
                    try:
                        data = link.get_text()
                        data = data + '\n'
                        xingan_data.write(data)
                    except:
                        continue
            except:
                continue
        except:
            continue
    xingan_data.close()

