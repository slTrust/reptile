#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import requests

# post请求的url
url = 'https://accounts.douban.com/login'

# 封装post请求参数数据
data = {
    "source":'movie',
    'redir':'https://movie.douban.com/',
    'form_email':'15027900535',
    'form_password':'bobo@15027900535',
    'login':'登录'
}

#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

response = requests.post(url=url,data=data,headers=headers)

# 获取响应对象中的页面数据

page_text = response.text

with open('movie.html','w',encoding='utf-8') as f:
    f.write(page_text)