#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import time
key="Python"
url="https://bj.lianjia.com/ershoufang/pg"
# data=requests.get(url,params={"q":key}).text
data=requests.get(url).text
# pat1='<div class="_search-info">找到(.*?)条关于'
pat1 = '<h2 class="total fl">共找到<span> (.*?) </span>'
allline=re.compile(pat1,re.S).findall(data)[0]
allpage=int(allline)//30+1
for i in range(0,int(allpage)):
    print("----------------------------------正在爬第"+str(i+1)+"页--------------------------------------")
    index=str(i+1)
    data=requests.get(url+''+str(index)+'').text
    pat_title = '<div class="title"><a.*?>(.*?)</a>'
    pat_info = '<div class="houseInfo"><a.*?>(.*?)</a>.*?</div>'
    pat_info2 = '<div class="houseInfo"><a.*?/a>(.*?)</div>'
    title = re.compile(pat_title,re.S).findall(data)
    info = re.compile(pat_info,re.S).findall(data)
    info2 = re.compile(pat_info2, re.S).findall(data)
    index = 0
    for j in title:
        print('-----------')
        print(title[index])
        print(info[index])
        print(info2[index].split('<span class="divide">/</span>'))
        index +=1
