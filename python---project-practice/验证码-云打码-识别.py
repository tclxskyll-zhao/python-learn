import requests
from lxml import etree

from test_station import headers

import base64
import requests

# www.jfbym.com  注册后登录去用户中心

def verify():
    with open('./codeText.jpg', 'rb') as f:
        b = base64.b64encode(f.read()).decode()  ## 图片二进制流base64字符串
    url = "http://api.jfbym.com/api/YmServer/customApi"
    data = {
        ## 关于参数,一般来说有3个;不同类型id可能有不同的参数个数和参数名,找客服获取
        "token": "UQWIu8EcEjGABcmQ2N6bEaPbbkyT3kAFXT0_Z7ROTzo",
        "type": "10110",
        "image": b,
    }
    _headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, headers=_headers, json=data).json()
    print(response['data']['data'])


if __name__ == '__main__':
    # 获取验证码图片
    url='https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/wode.aspx'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }
    resp_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(resp_text)
    img_path='https://www.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data=requests.get(url=img_path,headers=headers).content
    with open('./codeText.jpg','wb') as f:
        f.write(img_data)

    pathPic='./codeText.jpg'
    #使用云打码平台将获取的验证码识别并打印
    verify()




