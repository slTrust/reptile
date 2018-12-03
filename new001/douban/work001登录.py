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

#2.对个人主页发起请求（session（cookie）），获取响应页面数据
url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
response = session.get(url=url,headers=headers)
page_text = response.text

with open('./douban110.html','w',encoding='utf-8') as fp:
    fp.write(page_text)