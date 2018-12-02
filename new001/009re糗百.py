#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import requests
import re
import os
#1指定url
url = 'https://www.qiushibaike.com/pic/'

#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

#2发请求
response = requests.get(url=url,headers=headers)

#3获取页面数据
page_text = response.text

#4数据解析
'''
<div class="thumb">
    <a href="/article/121304175" target="_blank">
        <img src="//pic.qiushibaike.com/system/pictures/12130/121304175/medium/7RG0RFB30I0KWFMI.jpg" alt="要把下面烫卷">
    </a>
</div>
'''
# 该列表中存储的就是当前页面源码中所有图片的url
img_arr = re.findall('<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>',page_text,re.S)

# 创建存储图片数据的文件夹
if not os.path.exists('./imgs'):
    os.mkdir('imgs')
'''
# 发现是不含协议部分的
['//pic.qiushibaike.com/system/pictures/12130/121304185/medium/6X8SQWYH0BBUO1KV.jpg',....]'''
# 添加上协议
for url in img_arr:
    img_url = 'https:' + url
    # 持久化存储：存储的是图片的数据而不是url
    # 获取图片二进制数据值
    img_data = requests.get(url=img_url,headers=headers).content

    # 将 6X8SQWYH0BBUO1KV.jpg 当做图片的名字
    img_name = url.split('/')[-1]
    img_path = 'imgs/' + img_name
    with open(img_path,'wb') as f:
        f.write(img_data)
        print(img_name+'写入成功')
