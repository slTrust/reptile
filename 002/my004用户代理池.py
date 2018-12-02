import urllib.request
import random
#用户代理池
userAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    ]
def UA():
    opener = urllib.request.build_opener()
    currentUaInfo = random.choice(userAgents)
    ua = ("User-Agent",currentUaInfo)
    opener.addheaders = [ua]
    urllib.request.install_opener(opener)
    print("当前使用UA："+str(currentUaInfo))

url = "https://www.qiushibaike.com/"

for i in range(0,10):
    UA()
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")