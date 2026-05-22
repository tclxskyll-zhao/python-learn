import time
from multiprocessing.dummy import Pool
from time import sleep

def get_page(str):
    print('正在爬取：',str)
    sleep(2)
    print('爬取成功',str)

if __name__ == '__main__':

    tmp_list=['aaa','bbb','ccc','ddd']
    start_time=time.time()
    
    pool=Pool(4)
    pool.map(get_page,tmp_list)
    end_time=time.time()
    print(end_time-start_time)




