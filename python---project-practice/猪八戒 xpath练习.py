from wsgiref import headers

import requests
from lxml import etree
url="https://www.zbj.com/fw/?k=sass"

headers={
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
"cookie":"_uq=1547939c2d6b4ae3b7f12af9b176e243; unionJsonOcpc=eyJvdXRyZWZlcmVyIjoiaHR0cHM6Ly9jbi5iaW5nLmNvbS8iLCJwbWNvZGUiOiIifQ==; uniqid=d016mlj7fnpps5; _suq=e80d9a9a-b81a-486e-8906-48c078039279; oldvid=; vid=f28864025fb3a9b59d2c5c8c3543a944; local_city_path=xian; local_city_name=%E8%A5%BF%E5%AE%89; local_city_id=3817; nodejs-zzgg-jinshi-web=s%3ASZqyBrpCvLKBj3FLfJ9oGAVMJ9DBZq-c.H0M%2FGPM8DBEp1rCRDOLEAwYyYlsDVLOLC6Hp4V6W66I; Hm_lvt_a360b5a82a7c884376730fbdb8f73be2=1775728997; HMACCOUNT=D966E6B86F19EF04; vidSended=1; pc_no_login_modal_last_show=1; newUserRegister=0; Hm_lpvt_a360b5a82a7c884376730fbdb8f73be2=1775729868; s_s_c=xXWAc4Eno6Jb0bz4%2Fej0DinVdJzUTuRlDX8U%2BMjcPNTip%2Bf0BK2TfY4bWVzwh%2BTjnetvbfIJwobvEmQe%2FxYkVw%3D%3D; _umv=21100adb9c9b05beff0a90e4b39d6c85; nickname=t_8777_Uo4ut7; brandname=t_8777_Uo4ut7; userid=39108019; userkey=78nsVq7GHOv%2F0fTBQLxq67%2F25Rk%2BcpMDUNcAMNe10HVz0RunM1%2BVSCWWEndPYVgSOVwClAXl9ocJsHlO03lE9V0JWE8y5Nq4Shp8kgAJg%2B499Y3P2syI1n2ukZ%2Ff2%2FVY1o9LI1CkzUQZMmAgPertKkIQ6MYaGVZ9WPIYF16CtpSsi5q3MWEfLzWrb6W8aQ9PeR3fcIkCLXKzpY%2BDGeBQSqSMbAbMhB8%2BzqDisn5xnNdXon12lmaMIB3gJzYjxX6kGpjB7FYv375WwmfeklkmD1QTEsUA4bsnIm5RQhF2cMGQ8heJJ23aFzMA2fKb8yLIcmiYRKk9Z7u41m3i2W7ZWoCk9z9C; orgMaster=0"
}

resp=requests.get(url=url,headers=headers)
print(resp.text)
