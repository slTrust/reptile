import requests
from bs4 import BeautifulSoup

headers={
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
     }
def parse_content(url):
    #获取标题正文页数据
    page_text = requests.get(url,headers=headers).text
    soup = BeautifulSoup(page_text,'lxml')
    #解析获得标签
    ele = soup.find('div',class_='chapter_content')
    content = ele.text #获取标签中的数据值
    return content

if __name__ == "__main__":
     url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
     reponse = requests.get(url=url,headers=headers)
     page_text = reponse.text

     #创建soup对象
     soup = BeautifulSoup(page_text,'lxml')
     #解析数据
     a_eles = soup.select('.book-mulu > ul > li > a')
     print(a_eles)
     cap = 1
     fp =  open('./sanguo.txt', 'w')

     for ele in a_eles:
         print('开始下载第%d章节'%cap)
         cap+=1
         title = ele.string
         content_url = 'http://www.shicimingju.com'+ele['href']
         content = parse_content(content_url)

         fp.write(title+":"+content+'\n\n\n')
         print('结束下载第%d章节'%cap)