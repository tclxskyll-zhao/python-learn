import random
import re
import requests
from lxml import etree
from multiprocessing.dummy import Pool
import os
# 使用 多线程爬取梨视频视频
if __name__ == '__main__':
     # 生成一个存视频的文件夹
    if not os.path.exists('./video'):
         os.mkdir('./video')
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    #线程池处理的是较为 阻塞和耗时 的操作

    url='https://www.pearvideo.com/category_1'
    page_text=requests.get(url=url,headers=headers).text

    tree=etree.HTML(page_text)
    li_list=tree.xpath('//*[@id="listvideoListUl"]/li')

    urls=[]
    #视频url      https://video.pearvideo.com/mp4/short/20260429/cont-1806001-16076017-hd.mp4
    #接口返回的url https://video.pearvideo.com/mp4/short/20260429/1777708299502-16076017-hd.mp4
    for li in li_list:
        detail_url='https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
        name=li.xpath('./div/a//div[@class="vervideo-title"]/text()')[0]+'.mp4'
        #这里的方法失效，网站目前需要动态加载这个接口，无法直接使用 正则表达式提取结果
        contId=detail_url.split('_')[-1]
        print(contId)


        #使用 AJAX 技术爬取视频
        ajax_url='https://www.pearvideo.com/videoStatus.jsp'
        params={
            "contId":contId,
            "mrd":str(random.random())
        }
        ajax_headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
            "referer":f"https://www.pearvideo.com/video_{contId}"
        }
        dic_data=requests.get(url=ajax_url, params=params, headers=ajax_headers).json()
        video_url=dic_data['videoInfo']['videos']['srcUrl']
        rep_str=re.search(r'(\d{13})',video_url).group()
        video_url=video_url.replace(rep_str,'cont-'+contId)
        print(video_url)

        #使用 字典对数据进行存储
        dic_v={
            "name":name,
            "video_url":video_url
        }
        urls.append(dic_v)

    #持久化存储结果
    def get_video(dic):
        url_=dic['video_url']
        print(dic['name'],"正在下载")
        video_data=requests.get(url=url_,headers=headers).content
        video_path='./video/'+dic['name']
        video_path=video_path.replace('"','')
        video_path=video_path.replace(':',' ')
        with open(video_path,'wb') as f:
            f.write(video_data)
            print(dic['name'],"下载完毕")

    #使用 线程池 提高 阻塞/耗时操作
    pool=Pool(4)
    pool.map(get_video,urls)

    pool.close()
    pool.join()





    # detail_page_text=requests.get(url=detail_url,headers=headers).text
    # #这里发现页面做了修改直接在 XHR/AJAX 技术接收到了 前端渲染的效果
    # video_url='https://www.pearvideo.com/videoStatus.jsp?contId=1806001&mrd=0.4173496326895778'

