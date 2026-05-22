import requests
import re
import csv


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
def getDouBan250(start):
    url = f'https://movie.douban.com/top250?start={start}&filter='
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    pageSource = resp.text

    obj = re.compile(
        r'<div class="item">.*?'
        r'<span class="title">(?P<name>.*?)</span>.*?'
        r'<p>.*?导演: (?P<dao>.*?)&nbsp;.*?<br>'
        r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
        r'(?P<score>.*?)</span>'
        r'.*?<span>(?P<num>.*?)人评价</span>',
        re.S
    )
    result = obj.finditer(pageSource)
    data_list=[]
    for item in result:
        row_data={
            "电影名": item.group("name"),
            "导演": item.group("dao").strip(),
            "上映时间": item.group("year").strip(),
            "评分": item.group("score").strip(),
            "评论数": item.group("num")
        }
        data_list.append(row_data)
    return data_list
if __name__=="__main__":
    
    with open('豆瓣250.csv', 'w', encoding='utf-8-sig', newline='') as file:
        fieldnames = ['电影名', '导演', '上映时间', '评分', '评论数']
        csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_dict_writer.writeheader() 
        for i in range(10):  #[0,9]
                i=i+1
                start_num = (i-1) * 25  
                print(f"正在抓取第 {i} 页")
                
                
                data = getDouBan250(start_num)
                print(start_num)
                if data:
                # 修正写入逻辑：遍历列表，逐行写入
                    for row in data:
                        csv_dict_writer.writerow(row)
                else:
                    print("未找到该数据")
    print("豆瓣250抓取数据完毕")            