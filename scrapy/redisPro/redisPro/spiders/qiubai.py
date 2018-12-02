# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_redis.spiders import RedisCrawlSpider
# class QiubaiSpider(CrawlSpider):
#     name = 'qiubai'
#
#     # 此时要注释掉 allowed_domains 和 start_urls
#     # allowed_domains = ['https://www.qiushibaike.com/pic']
#     # start_urls = ['http://https://www.qiushibaike.com/pic/']
#
#     # redis_key 它代表调度器队列的名称
#     redis_key = 'qiubaispider' # 该行代码和 start_urls 一样
#     rules = (
#         Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
#     )
#
#     def parse_item(self, response):
#         i = {}
#         #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
#         #i['name'] = response.xpath('//div[@id="name"]').extract()
#         #i['description'] = response.xpath('//div[@id="description"]').extract()
#         return i

from redisPro.items import RedisproItem

class QiubaiSpider(RedisCrawlSpider):
    name = 'qiubai'

    # 此时要注释掉 allowed_domains 和 start_urls
    # allowed_domains = ['https://www.qiushibaike.com/pic']
    # start_urls = ['http://https://www.qiushibaike.com/pic/']

    # redis_key 它代表调度器队列的名称
    redis_key = 'qiubaispider' # 该行代码和 start_urls 一样

    # 糗百糗图  底部分页器
    '''
    <a href="/pic/page/2?s=5145873" rel="nofollow">
    解析规则
    /pic/page/2/?s=5145873
    为啥有个s=5145873  刷新下页面后  发现 s会变化 所以可以把s参数忽略
    /pic/page/\d+
    '''
    link = LinkExtractor(allow=r'/pic/page/\d+')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            img_url = 'https:'+ div.xpath('.//div[@class="thumb"]/a/img/@src').extract_first()
            item = RedisproItem()
            item['img_url'] = img_url

            # 这个是 scrapy的管道， 此时要使用 scrapy_redis 提供的管道
            yield item
