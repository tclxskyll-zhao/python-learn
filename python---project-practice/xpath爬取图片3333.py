import requests
from lxml import etree
import os

from test_station import headers

#需求：使用 xpath在 https://pic.netbian.com/4kmeinv/ 爬取图片

if __name__=='__main__':
    url='https://pic.netbian.com/4kmeinv/'
    headers = {
        # 修正了 User-Agent，使用一个较新但不过分超前的版本
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "referer":"https://pic.netbian.com/4kmeinv/",
        "cookie":"abymg_id=1_3CD81A25465E4DE6C663FD2C32456029D922F2DD88A349C9C9EC260AC783EA08; RcGFvecookieclassrecord=%2C54%2C85%2C; RcGFvcodeid=220278; RcGFvmlusername=wx26042915292773; RcGFvmluserid=8305536; RcGFvmlgroupid=1; RcGFvmlrnd=OgugdmVdfayoM83VJu2l; RcGFvmlrndt=7zrCkWhnz8fRMkUf6r6D3RUWgLdKmR; RcGFvmlinfo=%5B%22%22%2C%220%22%2C%22wx26042915292773%22%2Cnull%5D; RcGFvmlauth=9252e8c49a86e9b669069e64dea5ee6d; Hm_tf_wmdtrcgrgcv=1777447754; Hm_lvt_wmdtrcgrgcv=1777447754; Hm_lpvt_wmdtrcgrgcv=1777447760"
    }
    if not os.path.exists('./pictulibs'):
        os.mkdir('./pictulibs')

    resp_data=requests.get(url=url,headers=headers).text
    resp_data.encode('utf-8')
    print(resp_data)

    tree=etree.HTML(resp_data)
    li_list=tree.xpath('//div[@class="slist"]/ul/li')

    for li in li_list:
        img_src='https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
        print(img_src)
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'

        rep_pic=requests.get(url=img_src,headers=headers).content
        with open('./pictulibs/'+img_name,'wb') as fp:
            fp.write(rep_pic)
        print(img_name,'爬取成功')

