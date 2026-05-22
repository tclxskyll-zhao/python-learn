# 网页爬取 百度小说-剑来
import json
from asyncio import wait

import requests
import asyncio
import aiohttp
import aiofiles
import os


#获取小说的网页章节信息
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4305547728"}  章节-title-cid
# 章节的内容
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4305547728","cid":"4305547728|10364019","need_bookinfo":1}
#下载剑来的每个章节-使用 异步操作


async def aioDownLoad(cid,b_id,title):
    data = {"book_id": b_id,
            "cid": f"{b_id}|{cid}",
            "need_bookinfo": 1
            }
    data=json.dumps(data)
    url=f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic=await resp.json()

            file_path = os.path.join(save_dir, f"{title}.txt")

            # 4. 将保存路径传递给 open 函数
            async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
                await f.write(dic["data"]["novel"]["content"])

async def getCatalog(url):
    resp=requests.get(url)
    dic=resp.json()
    task=[]
    for item in dic["data"]["novel"]["items"]:
        title=item["title"]
        cid=item["cid"]
        #准备每个章节的下载任务
        task.append(asyncio.create_task(aioDownLoad(cid, b_id, title)))


    await asyncio.wait(task)





if __name__=='__main__':
    b_id="4305547728"
    save_dir = "剑来"
    os.makedirs(save_dir, exist_ok=True)
    url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    asyncio.run(getCatalog(url))
