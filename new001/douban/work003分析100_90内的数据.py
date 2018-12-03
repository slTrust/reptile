#! -*-coding: utf-8 -*-

'''
获取对应剧情   总页码数 每页20条
获取 100-90的  总页码数  用于分页处理 get  请求
url = https://movie.douban.com/j/chart/top_list_count?type=11&interval_id=100%3A90
param = {
    type:11,
    interval_id:'100:90'
}

分页url数据
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

params = {
    type: 11
    interval_id: 100:90
    action:
    start: 0
    limit: 20
}

'''
import requests
import time
import json
import re
from bs4 import BeautifulSoup
from lxml import etree

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


'''
response = session.get(url=url,proxies=proxy,headers=headers)
page_text = response.text
'''

# 上面的url 实际没啥用  就是空页码结构
'''
实际的情况是 到这个剧情子页码的时候发送两个请求
第一个请求获取该类型  100-90的总条数total

第二个是分页数据 的第一页

以后下拉加载  对应分页数据
'''
totalUrl = 'https://movie.douban.com/j/chart/top_list_count/'

params = {
    'type':'11',
    'interval_id':'100:90'
}
response = session.get(url=totalUrl,params=params,proxies=proxy,headers=headers)

res = json.loads(response.text)

total = res.get('total',0)
total = 20
# 电影列表 容器
avi_list = []
if total > 0:
    fp = open('json_array.json', 'w')
    # 分页请求url
    pageUrl = 'https://movie.douban.com/j/chart/top_list/'
    # 豆瓣的规则是每页 20条
    # 所有我们只要处理   页码就行了
    pageSize = 20
    maxPage = total//pageSize
    curPage = 0



    detailUrls = [];
    for i in range(total):
        print(i)
        params2 = {
            'type': '11',
            'interval_id':'100:90',
            'action':'',
            'start': i,
            'limit': 20
        }
        # 1秒20条  防止被认为是爬虫
        # time.sleep(1)
        response = session.get(url=pageUrl, params=params2, proxies=proxy, headers=headers)

        # 每次请求里面是20部电影的简要信息
        '''
        一部电影数据如下，这里唯独没有导演和编剧 所以我们在详情页  在拿所有需要的数据这里只要详情页的地址url
        海报url、cover_url
        电影名称、title
        导演、
        编剧、
        主演，actors
        类型，
        语言，
        上映日期，
        片长，
        豆瓣评分 score
        [{
            "rating": ["9.2", "45"],
            "rank": 21,
            "cover_url": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p579729551.jpg",
            "is_playable": false,
            "id": "3793023",
            "types": ["剧情", "喜剧", "爱情", "歌舞"],
            "regions": ["印度"],
            "title": "三傻大闹宝莱坞",
            "url": "https:\/\/movie.douban.com\/subject\/3793023\/",
            "release_date": "2011-12-08",
            "actor_count": 8,
            "vote_count": 869683,
            "score": "9.2",
            "actors": ["阿米尔·汗", "卡琳娜·卡普尔", "马达范", "沙尔曼·乔希", "奥米·瓦依达", "博曼·伊拉尼", "莫娜·辛格", "拉杰夫·拉宾德拉纳特安"],
            "is_watched": false
        }]
        '''
        resData = response.text;

        infoObj = json.loads(resData)

        for j in infoObj:
            detailUrls.append(j.get('url',''))

    # 详情的所有url
    print(detailUrls)
    # detailUrls = ['https://movie.douban.com/subject/1292052/']
    for item in detailUrls:
        response = session.get(url=item,  proxies=proxy, headers=headers)
        content = response.text
        '''
        海报url、
        电影名称
        导演、
        编剧、
        主演，actors
        类型，
        语言，
        上映日期，
        片长，
        豆瓣评分 score
        '''
        #
        tree = etree.HTML(content)
        img_url = tree.xpath('//div[@id="mainpic"]/a/img/@src')
        title = tree.xpath('//div[@id="content"]/h1/span[1]/text()')
        daoyan = tree.xpath('//div[@id="info"]/span[1]/span[2]/a/text()')
        bianju = tree.xpath('//div[@id="info"]/span[2]/span[2]/a//text()')
        zhuyan = tree.xpath('//div[@id="info"]/span[3]/span[2]/a//text()')
        leixing = tree.xpath('//div[@id="info"]/span[@property="v:genre"]//text()')
        # 语言没有对应的 属性  只有一个 text节点  无法定位
        # yuyan = tree.xpath('//div[@id="info"]/span[@class="pl"][3]/text()')

        shangyingriqi = tree.xpath('//div[@id="info"]/span[@property="v:initialReleaseDate"]/text()')
        pianchang = tree.xpath('//div[@id="info"]/span[@property="v:runtime"]/text()')
        pingfen = tree.xpath('//div[@id="interest_sectl"]//strong[@property="v:average"]/text()')

        print(img_url)
        print(bianju)
        print(title)
        print(daoyan)
        print(zhuyan)
        print(leixing)
        print(shangyingriqi)
        print(pianchang)
        print(pingfen)

        avi_list.append({
            "img_url":img_url,
            "title":title,
            "daoyan":daoyan,
            "bianju":bianju,
            "zhuyan":zhuyan,
            "leixing":leixing,
            "shangyingriqi":shangyingriqi,
            "pianchang":pianchang,
            "pingfen":pingfen
        })


json.dump(avi_list, fp)

fp.close()
print('爬取结束')



