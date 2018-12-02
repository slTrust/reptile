#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import re

# 提取python
key = 'javapythonc++php'
res =re.findall('python',key)
print(res)

# 提取hello world
key = '<html><h1>hello world</h1></html>'
res =re.findall('<h1>(hello world)</h1>',key)
print(res)

# 提取170
key = '我喜欢身高170的女孩'
res =re.findall('\d+',key)
print(res)

# 提取 http 和 https
key = 'http://www.baidu.com and https://boob.com'
res =re.findall('https?',key)
res2 = re.findall('https{0,1}',key)
print(res,res2)

# 提取hit.
key = 'bobo@hit.edu.com'
res =re.findall('h.*\.',key)
print(res) # ['hit.edu.'] 贪婪模式（默认）尽可能多的提取数据
res2 =re.findall('h.*?\.',key)
print(res2)

# 提取 sas saas
key = 'saas and sas and saaas'
res =re.findall('sa{1,2}s',key)
print(res)


# 提取i开头的行
'''
re.S 基于单行
re.M 基于多行
'''
key = '''fall in love with you
i love you very much
i love she
i love her'''
res = re.findall('^i.*',key,re.M)
print(res)

# 匹配所有全部行
key = '''<div>静夜思
窗前明月光
疑是地上霜
举头望明月
低头思故乡
</div>'''
res = re.findall('<div>.*</div>',key,re.S)
print(res)
