import requests
from selenium import webdriver
from bs4 import BeautifulSoup
#ptt
ptturl = 'https://www.ptt.cc/bbs/Gossiping/index.html'
pttweb = requests.get(ptturl,cookies={'over18':'1'})
pttweb.encoding = 'utf-8'
pttsoup = BeautifulSoup(pttweb.text, "html.parser")
ptttitles = pttsoup.find_all('div',class_='title')
pttout = ''
for pttworm in ptttitles:
    if pttworm.find('a') != None:
       
        pttout = pttout + pttworm.find('a').get_text() + '\n'+ptturl+ pttworm.find('a')['href']+ '\n\n'

pttfile = open('C:/Users/user/Desktop/pttfile.txt','w')
pttfile.write(pttout)
pttfile.close()
#yahoo
yahoourl = 'https://www.ptt.cc/bbs/Gossiping/index.html'
pttweb = requests.get(ptturl,cookies={'over18':'1'})
pttweb.encoding = 'utf-8'
pttsoup = BeautifulSoup(pttweb.text, "html.parser")
ptttitles = pttsoup.find_all('div',class_='title')
pttout = ''
for pttworm in ptttitles:
    if pttworm.find('a') != None:
       
        pttout = pttout + pttworm.find('a').get_text() + '\n'+ptturl+ pttworm.find('a')['href']+ '\n\n'

pttfile = open('C:/Users/user/Desktop/pttfile.txt','w')
pttfile.write(pttout)
pttfile.close()
