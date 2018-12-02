#!/usr/bin/env python
#-*- encoding:utf-8 -*-

# 编码流程
from selenium import webdriver
from time import sleep
# 创建一个浏览器对象 executable_path为驱动的路径
bro = webdriver.Chrome(executable_path='./chromedriver2')
# get 方法可以指定一个url，让浏览器进行请求
bro.get('https://www.baidu.com')
sleep(3)
# 让百度根据指定 搜索词进行搜索
text = bro.find_element_by_id('kw') # 定位文本框
text.send_keys('abc') # 向文本框录入指定内容
sleep(1)
button = bro.find_element_by_id('su')
button.click() # 表示点击操作
sleep(3)

bro.quit()# 退出浏览器


