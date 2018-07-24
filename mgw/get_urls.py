# coding=utf-8
import os, re, json, random, socket
import urllib.request
from bs4 import BeautifulSoup


#爬虫参数
headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
headers2 = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'}
socket.setdefaulttimeout(10)#超时10s


#存入获取的urls
if not os.path.exists(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/urls'):
    os.mkdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/urls')
def save_urls(name, urls):
    save_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/urls/'+ name + '_new.txt'
    save_data = open(save_path, 'w')
    for i in urls:
        save_data.write(i)
        save_data.write('\n')
    save_data.close()   


###获取http://mongol.cctv.com/的urls
'''不同栏目地址:
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000251
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000253
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000255
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000257
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000259
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000263
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000265
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000271
    http://mongol.cctv.com/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000652
'''
urls_cctv=set()
list_cctv = ['100000251','100000253','100000255','100000257','100000259','100000263','100000265','100000271','100000652']
for j in list_cctv:
    try:
        url_json = 'http://mongol.cctv.com/contantroot/more/' + j + '.json'
        if(random.randint(0,1)):
            headers = headers1
        else:
            headers = headers2
        req = urllib.request.Request(url=url_json,headers=headers)
        response = urllib.request.urlopen(req)
        jsonString = response.read()
        jsonObject = json.loads(jsonString.decode())
        for i in range(len(jsonObject)):
            totalpage = jsonObject[i]['totalpage']
        for page_num in range(totalpage, 0, -1):
            try:
                url_1 = 'http://mongol.cctv.com/contantroot/more/' + j + '_' + str(page_num) + '.json'
                if(random.randint(0,1)):
                    headers = headers1
                else:
                    headers = headers2
                req = urllib.request.Request(url=url_1,headers=headers)
                response = urllib.request.urlopen(req)
                jsonString = response.read()
                jsonObject = json.loads(jsonString.decode())
                for i in range(len(jsonObject)):
                    url_2 = 'http://mongol.cctv.com/'
                    staticurl = jsonObject[i]['staticurl']
                    uuid = jsonObject[i]['uuid']
                    url_2 = url_2 + staticurl + '/' + uuid + '.html'
                    urls_cctv.add(url_2)        
            except:
                continue
    except:
        continue
save_urls('cctv', urls_cctv)


###获取http://www.mongolcnr.cn/的urls
'''不同栏目地址:
    http://www.mongolcnr.cn/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000051
    http://www.mongolcnr.cn/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000055
    http://www.mongolcnr.cn/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000057
    http://www.mongolcnr.cn/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000059
    http://www.mongolcnr.cn/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000061
    http://www.mongolcnr.cn/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000065
    http://www.mongolcnr.cn/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000071
    http://www.mongolcnr.cn/contantroot/c/ee11dcd1-0b6d-41cb-b6f6-62a3387bca7b.html?musk=100000093
'''
urls_cnr=set()
list_cnr = ['100000051','100000055','100000057','100000059','100000061','100000065','100000071','100000093']
for j in list_cnr:
    try:
        url_json = 'http://www.mongolcnr.cn/contantroot/more/'+ j + '.json'
        if(random.randint(0,1)):
            headers = headers1
        else:
            headers = headers2
        req = urllib.request.Request(url=url_json,headers=headers)
        response = urllib.request.urlopen(req)
        jsonString = response.read()
        jsonObject = json.loads(jsonString.decode())
        for i in range(len(jsonObject)):
            totalpage = jsonObject[i]['totalpage']
        for page_num in range(totalpage, 0, -1):
            try:
                url_1 = 'http://www.mongolcnr.cn/contantroot/more/' + j + '_' + str(page_num) + '.json'
                if(random.randint(0,1)):
                    headers = headers1
                else:
                    headers = headers2
                req = urllib.request.Request(url=url_1,headers=headers)
                response = urllib.request.urlopen(req)
                jsonString = response.read()
                jsonObject = json.loads(jsonString.decode())
                for i in range(len(jsonObject)):
                    url_2 = 'http://www.mongolcnr.cn/'
                    staticurl = jsonObject[i]['staticurl']
                    uuid = jsonObject[i]['uuid']
                    url_2 = url_2 + staticurl + '/' + uuid + '.html'
                    urls_cnr.add(url_2)        
            except:
                continue
    except:
        continue
save_urls('cnr', urls_cnr)


###获取http://mongol.people.com.cn/的urls
'''不同栏目地址:
    http://mongol.people.com.cn/306955/306999/index.html, http://mongol.people.com.cn/306955/307001/index.html
    http://mongol.people.com.cn/306955/307002/index.html, http://mongol.people.com.cn/306955/307003/index.html
    http://mongol.people.com.cn/306955/307004/index.html, http://mongol.people.com.cn/306955/307005/index.html
    http://mongol.people.com.cn/306955/307010/index.html, http://mongol.people.com.cn/306955/307011/index.html
    http://mongol.people.com.cn/306955/307031/index.html, http://mongol.people.com.cn/306955/307032/index.html
    http://mongol.people.com.cn/306955/309001/index.html, http://mongol.people.com.cn/306955/310698/index.html
    http://mongol.people.com.cn/306955/310704/index.html, http://mongol.people.com.cn/306955/310868/index.html
'''
urls_people=set()
urls_people_mid=set()
list_people = ['306999','307001','307002','307003','307004','307005','307010','307011','307031','307032','309001','310698','310704','310868']
for i in list_people:
    for j in ['/index', '/index1']:
        url_1 = 'http://mongol.people.com.cn/306955/' + i + j + '.html'
        urls_people_mid.add(url_1)
for url in urls_people_mid:
    try:
        if(random.randint(0,1)):
            headers = headers1
        else:
            headers = headers2
        req = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
        links=soup.find('div',class_='ej_center').find_all('a')
        for n in links:
            url_2 = n.get("href")
            url_2 = 'http://mongol.people.com.cn' + url_2
            urls_people.add(url_2)
    except:
        continue
save_urls('people', urls_people)


###获取http://mongol.people.com.cn/306956/的urls
'''不同栏目地址:
    http://mongol.people.com.cn/306956/306963/index.html, http://mongol.people.com.cn/306956/306964/index.html
    http://mongol.people.com.cn/306956/306965/index.html, http://mongol.people.com.cn/306956/306967/index.html
    http://mongol.people.com.cn/306956/306966/index.html, http://mongol.people.com.cn/306956/308678/index.html
'''
urls_cpc=set()
urls_cpc_mid=set()
list_cpc = ['306963','306964','306965','306967','306966','308678']
for i in list_cpc:
    for j in ['/index', '/index3', '/index2', '/index1']:
        url_1 = 'http://mongol.people.com.cn/306956/' + i + j + '.html'
        urls_cpc_mid.add(url_1)
for url in urls_cpc_mid:
    try:
        if(random.randint(0,1)):
            headers = headers1
        else:
            headers = headers2
        req = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
        links=soup.find_all('a')
        for n in links:
            url_2 = n.get("href")
            if re.match(r'^/\d{8}\.html$', url_2):
                url_2 = 'http://mongol.people.com.cn' + url_2
                urls_cpc.add(url_2)
    except:
        continue
#人民网和中国共产党新闻网有部分网页重复，需加去重操作
urls_people_old = set()
try:
    people_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/urls/people_url.txt'
    people_data = open(people_path, 'r')
    for line in people_data:
        urls_people_old.add(line[:-1])
    people_data.close()
except:
    pass
urls_cpc_need = urls_cpc - urls_people - urls_people_old
save_urls('cpc', urls_cpc_need)


###获取http://www.nmg.xinhuanet.com/mg/的urls
'''不同栏目地址:
    http://mongolian.news.cn/ls/gnxw.htm, http://mongolian.news.cn/ls/gjxw.htm, http://mongolian.news.cn/ls/yw.htm
    http://mongolian.news.cn/ls/zz.htm,   http://mongolian.news.cn/ls/jj.htm,   http://mongolian.news.cn/ls/jy.htm
    http://mongolian.news.cn/ls/wh.htm,   http://mongolian.news.cn/ls/sh.htm,   http://mongolian.news.cn/ls/jk.htm
    http://mongolian.news.cn/ls/ndm.htm,  http://mongolian.news.cn/ls/bsq.htm,  http://mongolian.news.cn/ls/xx.htm
'''
urls_xinhua=set()
urls_xinhua_mid=set()
list_xinhua = ['gnxw','gjxw','yw','zz','jj','jy','wh','sh','jk','ndm','bsq','xx']
for i in list_xinhua:
    url = 'http://mongolian.news.cn/ls/' + i +'.htm'
    urls_xinhua_mid.add(url)
for url in urls_xinhua_mid:
    try:
        if(random.randint(0,1)):
            headers = headers1
        else:
            headers = headers2
        req = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
        links=soup.find('ul', id='list-content').find_all('a')
        for n in links:
            url_1 = n.get("href")
            urls_xinhua.add(url_1)
    except:
        continue
save_urls('xinhua', urls_xinhua)

 
###获取http://www.xingandaily.com/的urls
'''不同栏目地址:
    http://www.xingandaily.com/mdls/am/alv.aspx?pid=0&alias=xingandaily&mid=9831&wv=U
    http://www.xingandaily.com/mdls/am/alv.aspx?pid=0&alias=xingandaily&mid=9881&wv=U
    http://www.xingandaily.com/mdls/am/alv.aspx?pid=0&alias=xingandaily&mid=9883&wv=U
    http://www.xingandaily.com/mdls/am/alv.aspx?pid=0&alias=xingandaily&mid=9886&wv=U
    http://www.xingandaily.com/mdls/am/alv.aspx?pid=0&alias=xingandaily&mid=9887&wv=U
    http://www.xingandaily.com/mdls/am/alv.aspx?pid=0&alias=xingandaily&mid=9888&wv=U
    http://www.xingandaily.com/mdls/am/alv.aspx?pid=0&alias=xingandaily&mid=9889&wv=U
'''
urls_xingan=set()
urls_xingan_mid=set()
list_xingan = ['9831','9881','9883','9886','9887','9888','9889']
for i in list_xingan:
    url = 'http://www.xingandaily.com/mdls/am/alv.aspx?pid=0&alias=xingandaily&mid=' + i +'&wv=U'
    urls_xingan_mid.add(url)
for url in urls_xingan_mid:
    try:
        if(random.randint(0,1)):
            headers = headers1
        else:
            headers = headers2
        req = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
        links=soup.find_all('span')
        for n in links:
            span_txt = n.get_text()
            if span_txt.isdigit():
                totalpage = span_txt
        totalpage = int(totalpage)
        for page_num in range(totalpage, -1, -1):
            try:
                params = urllib.parse.urlencode({
                        'ctl00$cph$ctl02':page_num,
                        '__VIEWSTATE':'/wEPDwUKLTMxNTY2Njc3OA9kFgJmD2QWAgIED2QWAgIBD2QWBAIDD2QWBAIDDxYCHgdWaXNpYmxlaGQCBw8WAh8AaBYCZg8VAQBkAgUPZBYEAgEPDxYCHgRUZXh0BV7ujJXuib7ui5zuipHui7ruiagg7oux7om27oyT7om27our7om1IC0gIO6Lvu6Kie6Kt+6Jvu6KtSDui7HuibbujJPuibbui6vuibjuirXuiaPuiqMg7oyJ7oqp7ouDZGQCBQ8PFgIeC1JlY29yZENvdW50BQQ2Njc4ZBYCAgMPDxYCHwEFATFkZBgBBRljdGwwMCRUQmFubmVyJFBvcnRhbFBhZ2VzDxQrAA5kZGZkZGRkPCsAEQACEWRkZGYC/////w9kVOEYFP3mlYLSYJOz4XCNG00d0W3DXrq00UDr/ae4+84='
                        }).encode('utf-8')
                if(random.randint(0,1)):
                    headers = headers1
                else:
                    headers = headers2
                req = urllib.request.Request(url=url,data=params,headers=headers)
                response = urllib.request.urlopen(req)
                soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
                links=soup.find('div',id='mk_mr_ctt_tp').find_all('a')
                for n in links:
                    url_2 = n.get("href")
                    url_2 = 'http://www.xingandaily.com' + url_2
                    urls_xingan.add(url_2)
            except:
                continue
    except:
        continue
save_urls('xingan', urls_xingan)

