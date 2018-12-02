import urllib.request
#爬到硬盘的文件中
url="http://www.jd.com"
urllib.request.urlretrieve(url,filename="D:/pypac/test.html")