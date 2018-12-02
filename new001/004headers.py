#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import requests

url = 'https://www.sogou.com/'

#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

# 将参数封装到字典里
params = {
    'query':'周杰伦',
    'ie':'utf-8'
}

response = requests.get(url=url,params=params,headers=headers)

print(response.text)
