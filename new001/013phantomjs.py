#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from selenium import webdriver
import time

# phantomjs路径
path = r'/Users/almost/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs'
browser = webdriver.PhantomJS(path)

# 打开百度
url = 'http://www.baidu.com/'
browser.get(url)

time.sleep(3)

browser.save_screenshot(r'phantomjs\baidu.png')

# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里面写文字
my_input.send_keys('美女')
time.sleep(3)
#截屏
browser.save_screenshot(r'phantomjs\meinv.png')

# 查找搜索按钮
button = browser.find_elements_by_class_name('s_btn')[0]
button.click()

time.sleep(3)

browser.save_screenshot(r'phantomjs\show.png')

time.sleep(3)

browser.quit()