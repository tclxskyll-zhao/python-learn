#使用 正则表达式进行图片爬取
import requests
import re
import os

from 药监局数据爬取 import params

if __name__=='__main__':
    if not os.path.exists('./qiuTuLibs'):
        os.mkdir('./qiuTuLibs')
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }
    for pageNum in range(1,5):
        new_url=f'https://qiushidabaike.com/pic_{pageNum}.html'
        print(new_url)

        resp_data=requests.get(url=new_url,headers=headers).text  #获取网页的字符串信息

        #使用正则表达式提取图片信息
        ex='<dd class="content content-pic">.*?<img src="(.*?)" alt.*?</dd>'
        img_url_list=re.findall(ex,resp_data,re.S)
        for img_url in img_url_list:
            img_url='https://qiushidabaike.com'+img_url
            img_data=requests.get(img_url,headers=headers).content #获取图片-这里使用 二进制 格式进行接收

            img_name=img_url.split('/')[-1]
            img_path='./qiuTuLibs/'+img_name
            with open(img_path,'wb') as fp:
                fp.write(img_data)
                print(img_name+'爬取成功')


    print("爬取成功")



