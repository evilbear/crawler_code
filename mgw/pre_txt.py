# coding=utf-8
import os, socket, random
import urllib.request
from bs4 import BeautifulSoup

###去空格，切分
###cctv和cnr网站正文相似
def pre_cctv_cnr(input_name, output_name):
    open_path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + input_name +'.txt'
    open_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + output_name + '.txt'
    open_data1 = open(open_path1, 'r')
    open_data2 = open(open_path2, 'a')
    lines = open_data1.readlines()
    for line in lines:
        data = line.strip()
        if len(data) != 0:
            for j in data:
                open_data2.write(j)
                if j == '' or j == '᠃' or j == '!' or j == '?' or j == '᠁' :
                    open_data2.write('\n')
            if data[-1:] == '' or data[-1:] == '᠃' or data[-1:] == '!' or data[-1:] == '?' or data[-1:] == '᠁' :
                pass
            else:
                open_data2.write('\n')
    open_data1.close()
    open_data2.close()
    
###people和cpc网站正文相似
def pre_people_cpc(input_name, output_name):
    open_path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + input_name +'.txt'
    open_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + output_name + '.txt'
    open_data2 = open(open_path2, 'a')
    open_data1 = open(open_path1, 'r')
    lines = open_data1.readlines()
    for line in lines:
        data = line.strip()
        if len(data) != 0:
            for j in data:
                if j == '' or j == '':
                    open_data2.write(j)
                    open_data2.write(' ')
                elif j == '' or j == '' or j == '':
                    open_data2.write(' ')
                    open_data2.write(j)
                elif j == '' or j == '᠃' or j == '!' or j == '?' or j == '᠁' :
                    open_data2.write(' ')
                    open_data2.write(j)
                    open_data2.write('\n')
                else:
                    open_data2.write(j)
    open_data1.close()
    open_data2.close()
    
###xingan和xinhua网站正文相似
def pre_xingan_mgyxw(input_name, output_name):
    open_path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + input_name +'.txt'
    open_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + output_name + '.txt'
    open_data2 = open(open_path2, 'a')
    open_data1 = open(open_path1, 'r')
    lines = open_data1.readlines()
    for line in lines:
        data = line.strip()
        if len(data) != 0:
            for j in data:
                open_data2.write(j)
                if j == '' or j == '᠃' or j == '!' or j == '?' or j == '᠁' :
                    open_data2.write('\n')
    open_data1.close()
    open_data2.close()

###调用函数处理，其中mgyxw为国标码，不需要蒙特立编码转换
cctv_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/cctv.txt'
cnr_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/cnr.txt'
people_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/people.txt'
cpc_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/cpc.txt'
xingan_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/xingan.txt'
xinhua_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/xinhua.txt'
if os.path.exists(cctv_path):
    pre_cctv_cnr('cctv','data_add')
    os.remove(cctv_path)
if os.path.exists(cnr_path):
    pre_cctv_cnr('cnr','data_add')
    os.remove(cnr_path)
if os.path.exists(people_path):
    pre_people_cpc('people','data_add')
    os.remove(people_path)
if os.path.exists(cpc_path):
    pre_people_cpc('cpc','data_add')
    os.remove(cpc_path)
if os.path.exists(xingan_path):
    pre_xingan_mgyxw('xingan','data_add')
    os.remove(xingan_path)
if os.path.exists(xinhua_path):
    pre_xingan_mgyxw('xinhua','data')
    os.remove(xinhua_path)
     
###data_add  蒙特立编码转换
data_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data_add.txt'
save_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data.txt'
data_file = open(data_path, "r")
save_file = open(save_path, "a")
#爬虫参数
headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
headers2 = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'} 
socket.setdefaulttimeout(10)#超时10s 
url = 'http://mtg.mglip.com/'
tag, txt= 0, ''
for line in data_file:
    tag += 1
    txt += line
    if tag == 100:
        try:
            params = urllib.parse.urlencode({
                                    '__VIEWSTATE':'/wEPDwULLTEyMjA2MDAyOTJkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBRFCdXR0b25UcmFuX0lEQmFjawUNQnV0dG9uVHJhbl9JRPCzb3uVDl5G8nD1zvyUhU5wMUnbC2zYh3+8Wld2ogB2',
                                    '__EVENTVALIDATION':'/wEdAAU30dcFl6Eqz9lyNLRaEnQ5Taw2keI+7zV+INMO8AHzSUHIbZyaqTF+z9onQgXSv3QGd75SsxXhlZrnKIv47ot/SFXHjTDBqsCa3dYPptywffSmvx+0qadnMZ/QXHQ6lJoNQ/nGVxuVrJSpK02v6qy6',
                                    'inputCyrillic_ID':txt,
                                    'ButtonTran_ID.x':28,
                                    'ButtonTran_ID.y':10
                                    }).encode('utf-8') 
            if(random.randint(0,1)):
                headers = headers1
            else:
                headers = headers2
            req = urllib.request.Request(url=url,data=params,headers=headers)
            response = urllib.request.urlopen(req)
            soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
            links=soup.find_all('textarea',id='outPutTraditonalM_ID')
            for n in links:
                data = n.get_text()
                if data != '\n':
                    save_file.write(data)
        except:
            tag, txt= 0, ''
            continue
        tag, txt= 0, ''
data_file.close()
save_file.close()
os.remove(data_path)

