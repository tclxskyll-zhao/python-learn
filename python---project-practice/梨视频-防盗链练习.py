
import requests
#拉取视频的网址
url="https://www.pearvideo.com/video_1805756"
contId=url.split("_")[1]

VideoStatusUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.7085540787559746"

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    # 防盗链
    "referer":"https://www.pearvideo.com/video_1805756"
}

resp=requests.get(url=VideoStatusUrl,headers=headers)
dic=resp.json()
srcUrl=dic["videoInfo"]["videos"]["srcUrl"]
systemTime=dic["systemTime"]
print(srcUrl)
srcUrl=srcUrl.replace(systemTime,f"cont-{contId}")
print(srcUrl)

#下载视频
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl,headers=headers).content)