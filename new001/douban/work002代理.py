#! -*-coding: utf-8 -*-

import requests

session = requests.session()
#1.发起登录请求：将cookie获取，切存储到session对象中
login_url = 'https://accounts.douban.com/login'
data = {
    "source": "None",
    "redir": "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=",
    "form_email": "15027900535",
    "form_password": "bobo@15027900535",
    "login": "登录",
}
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
#使用session发起post请求
login_response = session.post(url=login_url,data=data,headers=headers)

#2.对电影排行榜-->剧情分类>子页面  发起请求（session（cookie）），获取响应页面数据
url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='

#3.将代理ip封装到字典
proxy = {
    'http':'77.73.69.120:3128',
    # 'http':'125.39.9.34:9000',
    # 'http':'106.75.14.190:9998',
    # 'http':'117.169.38.56:80',
    # 'http':'121.69.42.82' # 本机
}

response = session.get(url=url,proxies=proxy,headers=headers)
page_text = response.text

with open('./douban111.html','w',encoding='utf-8') as fp:
    fp.write(page_text)