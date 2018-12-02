#!/usr/bin/env python
#-*- encoding:utf-8 -*-


import requests

# 指定url
url = 'https://www.sogou.com/'

# 发get请求,get方法会返回请求成功的响应内容
response = requests.get(url=url)

# 获取响应中的数据值：text可以获取响应对象中字符串形式的页面数据
page_data = response.text

# print(page_data)
# 获取响应对象中二进制(byte)类型的数据
# print(response.content)

# 返回响应的状态码
print(response.status_code)

# 获取响应的头信息(字典的形式)
print(response.headers)

# 获取请求的url
print(response.url)

# 持久化存储
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(page_data)



