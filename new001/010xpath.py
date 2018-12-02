#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from lxml import etree
import requests
# 1. 指定url
url='https://ishuo.cn/joke'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
# 2 发请求
response=requests.get(url,headers=headers).text
# 3 获取页面内容
page_text = response.text
#4 解析
tree=etree.HTML(page_text)
# 获取所有li
li_list=tree.xpath('//div[@id="list"]/ul/li')
# 注意 Element类型对象可以继续用xpath函数，该对象表示的局部内容进行指定内容的解析

fp = open('./duanzi.txt','w',encoding='utf-8')

for li in li_list:
    content = li.xpath('./div[@class="content"]/text()')[0]
    title = li.xpath('./div[@class="info"]/a/text()')[0]
    # 5 持久化
    fp.write(title+':'+content+'\n\n')
    print('写入成功')
