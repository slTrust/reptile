#爬网页
import urllib.request
import re
url="http://www.jd.com"
#爬到内存中
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
rule = "<title>(.*?)</title>"
result = re.compile(rule,re.S).findall(data)
print(result)