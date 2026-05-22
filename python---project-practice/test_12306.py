import requests
from config import begin_addr, end_addr
start_time='2026-03-12'

#获取城市信息
station_url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9367'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}
resp=requests.get(station_url,headers=headers)
s_data=resp.text[resp.text.find('='):-1]
s_data=s_data.split('|')
num=len(s_data)//5
station_name={}
station_name2={}
k1=1
k2=2
for i in range(num):
    station_name[s_data[k1]]=s_data[k2]
    station_name2[s_data[k2]]=s_data[k1]
    k1+=5
    k2+=5


#获取车票信息
ba=station_name.get(begin_addr)
ea=station_name.get(end_addr)
info_url=f'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={start_time}&leftTicketDTO.from_station={ba}&leftTicketDTO.to_station={ea}&purpose_codes=ADULT'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'cookie':'_uab_collina=177289636682873000808035; JSESSIONID=44DDBB184DA8252BC06B9551758A0F9E; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_wfdc_flag=dc; BIGipServerotn=1339621642.50210.0000; BIGipServerpassport=870842634.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_toDate=2026-03-10; _jc_save_fromDate=2026-03-10'
}
resp=requests.get(info_url,headers=headers)
resp_data=resp.json().get('data').get('result')
for r in resp_data:
    data=[a for a in r.split('|')]
    if(data!='列车停运'):
        print(f'{data[13]}---{data[8]}---{station_name2.get(data[6])}---{station_name2.get(data[7])}---{data[32]}---{data[31]}')

  