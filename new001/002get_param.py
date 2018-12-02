#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import requests

url = 'https://www.sogou.com/web?query=周杰伦&ie=utf-8'

response = requests.get(url=url)

page_text = response.text

with open('./zhou.html','w',encoding='utf-8') as f:
    f.write(page_text)


