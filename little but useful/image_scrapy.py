import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re
import os
 
i=0
num=10   #按需更改
for j in range(num):
    url='http://www.meinv.tw/index_{0}.html'.format(j+2)
#     print(url)
    res=requests.get(url)
    # print(res.text)
    soup=BeautifulSoup(res.content)
    # print(soup)
    # print(soup.find_all('div',{'class':'image-list'}))
    links=soup.find_all('a')
 
    for item in links:
        i+=1
        item=str(item)
#         print(item)
        try:          
            m=re.search('href="(.+)" target="_blank',item)
            sublinks=m.group(1)         #m.group(1)只给出括号内匹配的内容  
            print(len(sublinks))        #m.group(0)给出匹配的内容
            if(len(sublinks)==18):
                sublinks_all='http://www.meinv.tw'+sublinks
#                 print(sublinks_all)
                
                subresponse=requests.get(sublinks_all)
                subsoup=BeautifulSoup(subresponse.content)
#                 print(subsoup)
                links_in=subsoup.find_all('p')
#                 print(links_in)
#                 print('1')
                try:
#                     print(links_in)
                    m1=re.search('src="(.+)jpg"',str(links_in))
                    sub_image_links=m1.group(1)+'jpg'  #m.group(1)只给出括号内匹配的内容  
#                     print(sub_image_links)
                    response=requests.get(sub_image_links)
                    if response.status_code==200:
                        file_path='{0}/{1}.{2}'.format(os.getcwd()+'/images',str(i),'jpg')
                        if not os.path.exists(file_path):
                            with open(file_path,'wb') as f:
                                f.write(response.content)
                                f.close()
                except:
                    pass
        
                
        except:
            pass