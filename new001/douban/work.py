#! -*-coding: utf-8 -*-

'''
动态爬取豆瓣电影中“更多”电影详情数据

需求:

1.使用任意代理IP进行如下操作
2.使用requests模块进行豆瓣电影的个人用户登录操作
3.使用requests模块访问个人用户的电影排行榜->分类排行榜->任意分类对应的子页面
4.爬取需求3对应页面的电影详情数据
5.爬取3对应页面中滚动条向下拉动2000像素后加载出所有电影详情数据，存储到本地json文件中或者相应数据库中
【备注】电影详情数据包括：海报url、电影名称、导演、编剧、主演，类型，语言，上映日期，片长，豆瓣评分
踩分点:

1234=>75
1235=>90
'''

'''
1。 代理ip使用
2。 登录使用
3。 个人用户的电影排行榜->分类排行榜->任意分类对应的子页面
4。 3对应页的电影详情数据
5。 3对应页  下拉2000px后 加载出所有电影详情数据  存到本地json文件中
【备注】电影详情数据包括：海报url、电影名称、导演、编剧、主演，类型，语言，上映日期，片长，豆瓣评分


海报url、
电影名称、
导演、
编剧、
主演，
类型，
语言，
上映日期，
片长，
豆瓣评分
'''

import requests
import re
import time

# url = 'https://www.baidu.com/s?ie=utf-8&wd=ip'
# # url = 'http'
#
# headers={
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
# }
#
# #将代理ip封装到字典
# proxy = {
#     'http':'77.73.69.120:3128',
#     # 'http':'125.39.9.34:9000',
#     # 'http':'106.75.14.190:9998',
#     # 'http':'117.169.38.56:80',
# }
# #更换网路IP
# response = requests.get(url=url,proxies=proxy,headers=headers)
#
# with open('./daili.html','w',encoding='utf-8') as fp:
#     fp.write(response.text)

import requests
import re
import time
key="Python"
url="https://bj.lianjia.com/ershoufang/pg"
# data=requests.get(url,params={"q":key}).text
data=requests.get(url).text
# pat1='<div class="_search-info">找到(.*?)条关于'
pat1 = '<h2 class="total fl">共找到<span> (.*?) </span>'
allline=re.compile(pat1,re.S).findall(data)[0]
allpage=int(allline)//30+1
for i in range(0,int(allpage)):
    print("----------------------------------正在爬第"+str(i+1)+"页--------------------------------------")
    index=str(i+1)
    data=requests.get(url+''+str(index)+'').text
    pat_title = '<div class="title"><a.*?>(.*?)</a>'
    title = re.compile(pat_title,re.S).findall(data)

