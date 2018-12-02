# -*- coding: utf-8 -*-
import scrapy

# 需求：百度翻译中指定词条的翻译结果 进行获取
class PostdemoSpider(scrapy.Spider):
    name = 'postDemo'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    # start_requests是父类的方法：对start_urls里的url进行get请求发送
    '''
    # 大概实现如下
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
    '''

    # 发起post
    '''
    1.将Request方法的method赋值成post
    2.FormRequest() 这个方法也可以发起post请求(推荐)
    '''
    def start_requests(self):
        # post请求参数
        data = {
            'kw':'dog'
        }
        for url in self.start_urls:
            # formdata :请求参数对应的字典
            yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)

    def parse(self, response):
        print(response.text)
        pass
