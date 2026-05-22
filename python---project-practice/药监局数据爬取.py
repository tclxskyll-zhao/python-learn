#药监局的网站改了，这里使用惠农网爬取数据
import requests
url='https://www.cnhnb.com/hangqing/sgzw/'
params={
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
resp=requests.get(url=url,params=params)


