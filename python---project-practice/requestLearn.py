# request 库学习
import requests
if __name__=="__main__":
    #获取要爬取的网站连接
    url="https://www.sogou.com/"
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
    }
    #获取网页对象
    response=requests.get(url,headers)
    #获取网页字符串
    page_text=response.text
    print(page_text)
    #本地化存储
    with open('./sougou.html',"w",encoding='utf-8') as fp:
        fp.write(page_text)
    print(page_text)