import requests


station_url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9367'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}
resp=requests.get(station_url,headers=headers)
s_data=resp.text[resp.text.find('='):-1]
s_data=s_data.split('|')
num=len(s_data)//5
station_name={}
k1=1
k2=2
for i in range(num):
    station_name[s_data[k1]]=s_data[k2]
    k1+=5
    k2+=5
print(station_name)