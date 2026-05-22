#网易云音乐评论抓取
#1.找到未加密的参数  params  encSecKey
#2.相办法对参数进行加密参考 网易的加密逻辑
#3.请求到网易，拿到评论信息
from wsgiref import headers

import  requests

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token=4f75a57ac7a3250813118c147  841ce1e"
headers={
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
}
data={
"csrf_token":"4f75a57ac7a3250813118c147841ce1e",
"cursor": "-1",
"offset": "0",
"orderType":"1",
"pageNo": "1",
"pageSize":"20",
"rid":"R_SO_4_2134508204",
"threadId":"R_SO_4_2134508204"
}
requests.post(url=url,headers=headers)

e="010001"
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
i="XriLIbsxsZO7rtFs"

def getencSecKey():
    return "2d13c0f0ded5ae21e1028edf6d2c10a7766d164c99d5be6ef4b7b34e672a8e0b51f7ec50acc6feafb927ad0ac9630fe9f4885ffffd4b167dda3e62144f9e8be8470118798822c4a07c3a6274e5220d236a23eeaf8bc4885149835a7c28ca5f8ba1bcb6faa9d4035b20ecc5b3a571dd443d868e217e2f6d3f579a561505ce3c34"
"""
 function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),  #数据加密
        h.encSecKey = c(i, e, f),     #数据加密
        h
    }
"""
