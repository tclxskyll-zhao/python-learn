import asyncio
from codecs import namereplace_errors

import aiohttp
urls=[
    "https://cdn.pixabay.com/photo/2015/03/12/12/58/woman-670119_1280.jpg",
    "https://cdn.pixabay.com/photo/2017/08/12/09/02/russia-2633851_1280.jpg",
    "https://cdn.pixabay.com/photo/2024/07/03/15/40/beauty-8870258_1280.png"
]

async def aio_download(url):
    name=url.rsplit('/',1)[1]
    #发送请求
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #写入文件
            with open(name,"wb") as f:
                f.write(await resp.content.read())

    print("下载完成")

    #获得图片内容
    #保存文件


async def main():
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(aio_download(url)))

    await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(main())


