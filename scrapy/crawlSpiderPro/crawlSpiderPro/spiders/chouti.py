# -*- coding: utf-8 -*-
import scrapy
# 链接提取器
from scrapy.linkextractors import LinkExtractor
# 规则解析器
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    # allowed_domains = ['dig.chouti.com']
    start_urls = ['https://dig.chouti.com/']

    # 实例化一个链接提取器
    # 链接提取器：用来提取指定的链接 (url)
    # allow参数：赋值一个正则表达式
    # 链接提取器就可以根据正则在页面中提取指定的链接
    # 提取到的链接会全部交给规则解析器
    link = LinkExtractor(allow=r'/all/hot/recent/\d+')
    rules = (
        # 实例化一个规则解析器
        # 规则解析器接收了 链接提取器发送的链接后，就会对这些链接发起请求，获取链接对应的页面内容，就会根据指定的规则对页面内容中指定的数据值进行解析
        # callback:指定一个解析规则(方法/函数)
        # follow: 先设置为False 后期详细说明
        # follow代表 是否将提取器继续作用到 链接提取器取出的链接所表示的页面数据中
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
