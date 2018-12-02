# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        print(response.text)  # 获取字符串类型的响应内容
        print(response.body)  # 获取字节类型的相应内容
        pass
