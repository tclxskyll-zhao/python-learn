import threading
from concurrent.futures import ThreadPoolExecutor
import csv
import requests
from lxml import etree

f=open("data1.csv",mode="w",encoding="utf-8")
csv_writer=csv.writer(f)
#抓取单个页面的数据
def down_one_page(url):
    req= requests.get(url)
    req.encoding = 'utf-8'
    html=etree.HTML(req.text)
    table_list=html.xpath("//ul/li[@class='market-list-item']")
    data_to_write=[]
    for t in table_list:
            product = t.xpath("./a/span[@class='product']/text()")
            place=t.xpath("./a/span[@class='place']/text()")
            price=t.xpath("./a/span[@class='price']/text()")
            csv_writer.writerow([product, place, price])
    print(url,"爬取完毕")


#抓取所有页面的数据-使用线程池
if __name__ == '__main__':
    # url="https://www.cnhnb.com/hangqing/sgzw/"
    # data_list1=down_one_page(url)
    # for data in data_list1:
    #     csv_writer.writerow(data)

    with ThreadPoolExecutor(10)as t:
        for i in range(1,5):
            t.submit(down_one_page,f"https://www.cnhnb.com/hangqing/cdlist-2003191-0-0-0-0-{i}/")
    print("全部提取完毕")

