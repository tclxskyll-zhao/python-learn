
from lxml import etree
import selenium
from selenium import webdriver
from time import sleep
#从 selenium 4.0 开始不用用户自动创建驱动对象

driver=webdriver.Chrome()
driver.get("https://china.nba.cn/statistics/playerstats")

print("正在等待数据加载...")
sleep(8)

page_text=driver.page_source
#解析数据 xpath
tree=etree.HTML(page_text)
tr_list = tree.xpath("//*[@id='app']/div[2]/div/div[2]/div/section[1]/div[3]/div/div/div/table/tbody/tr")
if not tr_list:
    print("未找到 tr_list")
for tr in tr_list:
    name_list = tr.xpath("./td[2]//span[2]/text()")
    if name_list:
        name = name_list[0].strip()
        print(f"球员: {name}")
    else:
        print(name_list,"未找到 name_list ")
sleep(4)





