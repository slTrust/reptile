import urllib.request
import re
import random

# 爬http://www.iqianyue.com首页所有文章，然后进入文章详情页爬各文章的标题，作者，文章内容等信息。
uapools = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    ]
def UA():
    opener = urllib.request.build_opener()
    thisua = random.choice(uapools)
    ua = ("User-Agent",thisua)
    opener.addheaders = [ua]
    urllib.request.install_opener(opener)
    print("当前使用UA："+str(thisua))
for i in range(0,1):
    UA()
    thisurl = "http://www.iqianyue.com/ar?page="+str(i+1);
    data = urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
    authorRule = '<div class="pet_list_one_info_name">(.*?)</div>'
    titleRule = '<h3 class="am-list-item-hd pet_list_one_bt"><a href="(.*?)" class="">(.*?)</a></h3>'
    print(data)
    res1 = re.compile(authorRule,re.S).findall(data)
    res2 = re.compile(titleRule,re.S).findall(data)
    for j in range(0,len(res1)):
        print("---title----")
        print(res2[j][1])
        print("---link----")
        print(res2[j][0])
        # 根据文章链接爬取内容
        UA()
        deepdata = urllib.request.urlopen(res2[j][0]).read().decode("utf-8","ignore")
        title2 = '<h1 class="pet_article_title">(.*?)</h1>'
        content2 = '<p>(.*?)</p>'
        deepres1 = re.compile(title2,re.S).findall(deepdata)
        deepres2 = re.compile(content2,re.S).findall(deepdata)
        print(deepres2)
        print("-------")
        