#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re
import random
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
keyname = "电视"
key = urllib.request.quote(keyname)
uapools = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
]


def ua(uapools):
    thisua = random.choice(uapools)
    print(thisua)
    headers = ("User-Agent", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 安装为全局
    urllib.request.install_opener(opener)

for i in range(1, 20):
    print("-----第" + str(i) + "页商品-----")
    #     https://search.smzdm.com/?c=home&s=%E7%94%B5%E8%A7%86&source=his&v=b&p=2
    url = "https://search.smzdm.com/?c=home&s=" + key + "&source=his&v=b&p=" + str(i)
    ua(uapools)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    # 正则表达式 获取标签内相关数据  pageid , 拼接跳转URL 用
    reg_for_pageid = "'pageid':'(.*?)'"
    pageid_list = re.compile(reg_for_pageid).findall(data)
    # list 去重复数据
    pageid_list = list(set(pageid_list))
    for i in range(0, len(pageid_list)):
        this_id = pageid_list[i]
        # https://www.smzdm.com/p/9968427/
        # 跳转到详情页面
        this_url = "https://www.smzdm.com/p/" + this_id + "/"
        item_data = urllib.request.urlopen(this_url).read().decode("utf-8", "ignore")
        # 获取部分title
        main_title_pat = '<em itemprop="name">(.*?)</em>'
        # 获取加个相关信息
        price_info_pat = '<span class="red">(.*?)</span>'
        main_title = re.compile(main_title_pat, re.S).findall(item_data)
        # 因为有文章的页面，所以去除文章相关的页面
        if len(main_title) > 0:
            main_title = main_title[0]
        else:
            continue
        price_info = re.compile(price_info_pat, re.S).findall(item_data)
        if len(price_info) > 0:
            # 判断加个相关的信息中是否有数字
            match_res = re.compile('[0-9]+').findall(price_info[0])
            if match_res:
                price_info = price_info[0]
            else:
                price_info = ""
        else:
            continue

        print("****************************")
        # 格式化输出一些信息
        print("主标题：%s" % main_title.strip())
        print("加个相关信息：%s" % price_info.strip())
