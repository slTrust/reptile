#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import requests

# 原始
# baseurl = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=40&limit=20'

url = 'https://movie.douban.com/j/chart/top_list'

# 封装ajax中  get参数
params = {
    'type':24,
    'interval_id':'100:90',
    'action':'',
    'start':40,
    'limit':20
}

#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

response = requests.get(url=url,params=params,headers=headers)

print(response.text)

