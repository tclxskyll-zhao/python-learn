from concurrent.futures import thread
from threading import Thread

# def func():
#     for i in range(1000):
#         print(f"func {i}")

class MyThread(Thread):
    def run(self):
        for i in range(1000):
            print("func",i)


if __name__ == '__main__':
    t=MyThread()
    t.start()

    for i in range(1000):
        print("main",i)