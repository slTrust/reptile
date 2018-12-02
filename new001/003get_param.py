#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import requests

# get请求方式二
url = 'https://www.sogou.com/web'

# 将参数封装到字典里
params = {
    'query':'周杰伦',
    'ie':'utf-8'
}

response = requests.get(url=url,params=params)

page_text = response.text

print(page_text)

