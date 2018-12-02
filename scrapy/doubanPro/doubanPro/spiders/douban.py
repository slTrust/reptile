# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/accounts/login']

    # 重写 start_requests
    def start_requests(self):
        # 将请求参数封装到 字典中
        # 豆瓣登陆页面 https://accounts.douban.com/login
        data = {
            'source': 'index_nav',
            'form_email': '15027900535',
            'form_password': 'bobo@15027900535',
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)
    def parse(self, response):

        # 登陆成功后的页面数据进行存储

        fp = open('main.html','w',encoding='utf-8')
        fp.write(response.text)

        # 获取当前用户个人主页对应的页面数据
        url = 'https://www.douban.com/people/185687620/'

        yield scrapy.Request(url=url,callback=self.parseSecondPage)

    # 定义跳转指定页面的 parse方法
    def parseSecondPage(self,response):
        fp = open('second.html', 'w', encoding='utf-8')
        fp.write(response.text)

        # 可以对当前用户的个人主页的页面数据进行解析操作

