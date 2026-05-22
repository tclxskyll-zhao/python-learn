from wsgiref import headers

import requests
from pyquery import PyQuery
# pyjuery 练习 懂车帝练习

#获取网页源码信息
def get_html_info(url,headers):
    resp = requests.get(url, headers=headers)
    return resp.text


#提取网页需要爬取的数据
def parse_page_html(html):
    doc=PyQuery(html)
    doc("css")
url="https://www.dongchedi.com/auto/series/score/80-x-x-x-x-x-x"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}
html=get_html_info(url,headers)
