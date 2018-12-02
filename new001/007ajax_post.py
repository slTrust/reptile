#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'


# 封装ajax中  post参数
data = {
    'cname':'',
    'pid':'',
    'keyword': '上海',
    'pageIndex':2,
    'pageSize':10
}

#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

response = requests.post(url=url,data=data,headers=headers)

print(response.text)

