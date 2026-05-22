from concurrent.futures import ThreadPoolExecutor



def func(name):
    for i in range(1000):
        print("name",i)

if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1000):
            t.submit(func,name=f"线程{i}")
    #等待线程池中所有的线程任务执行完毕后，执行守护线程的任务
    print("333")