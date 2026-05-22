# 使用 xpath 对数据进行爬取
from wsgiref import headers

import requests
from lxml import etree

if __name__=='__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }
    url='https://bj.58.com/zufang/'

    resp_data=requests.get(url=url,headers=headers).text
    rt=etree.HTML(resp_data)

    house_list=rt.xpath("//ul[@class='house-list']/li")
    print(house_list)
    for li in house_list:
        house_name=li.xpath("./div[2]/h2/a/text()")
        print(house_name)


