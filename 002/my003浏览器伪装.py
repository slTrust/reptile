import urllib.request
url = "https://www.qiushibaike.com/"
#data=urllib.request.urlopen(url).read().decode("utf-8","ignore")

opener = urllib.request.build_opener()
UA = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
opener.addheaders = [UA]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
print(data)