import asyncio
import threading
from asyncio import wait


#给方法添加了 async 之后会直接返回一个携程对象需要进行接收
# async def get_data(url):
#     print("正在请求的url是 ",url)
#     print("请求成功... ",url)
#
# if __name__ == "__main__":
#     c=get_data("https://www.baidu.com")
#     # #这里可以将事件对象添加到run方法中直接运行
#     # loop = asyncio.run(c)
#
#     # task 的使用
#     loop=asyncio.get_event_loop()
#     task=loop.create_task(c)
#     print(task)
#     loop.run_until_complete(task)
#     print(task)


# # 传入name参数:
# async def hello(name):
#     # 打印name和当前线程:
#     print("Hello %s! (%s)" % (name, threading.current_thread))
#     # 异步调用asyncio.sleep(1):
#     await asyncio.sleep(1)
#     print("Hello %s again! (%s)" % (name, threading.current_thread))
#     return name
#
# async def main():
#     L = await asyncio.gather(hello("Bob"), hello("Alice"))
#     print(L)
#
# asyncio.run(main())

async def get_downLoad(url):
    print("开始下载",url)
    await asyncio.sleep(2) # await 挂起操作
    print("下载完毕",url)

async def main():
    tasks=[
        asyncio.create_task(get_downLoad("www.111.com")),
        asyncio.create_task(get_downLoad("www.123.com")),
        asyncio.create_task(get_downLoad("www.456.com"))
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
     asyncio.run(main())






