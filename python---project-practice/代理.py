import  requests

#学会使用 代理爬取网页信息
url="https://www.baidu.com"
proxy={
    "http":"102.39.232.252:8080",
    "https":"102.39.232.252:8080"
}

resp=requests.get(url=url,proxies=proxy)
resp.encoding="utf-8"
print(resp.text)