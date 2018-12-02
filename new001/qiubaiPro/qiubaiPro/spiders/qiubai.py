#!/usr/bin/env python
#-*- encoding:utf-8 -*-

# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # 最好注释这个允许域名   因为图片如果是其他域名的就获取不到了
    # allowed_domains = ['www.qiushibaike.com/text']

    # 默认生成的协议是http的需要手动修改为 https
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 推荐xpath(scrapy里集成了xpath解析接口)

        # 每个段子的外层容器
        div_list = response.xpath('//div[@id="content-left"]/div')

        for div in div_list:
            author = div.xpath('./div/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()

            # step001 将解析到的数据 存到items对象
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            # step002 将item对象提交给管道
            yield item