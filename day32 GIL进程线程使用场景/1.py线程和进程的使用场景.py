
"""
研究python的多线程是否有用需要分情况讨论
四个任务 计算密集型的  10s
单核情况下
    开线程更省资源
多核情况下
    开进程 10s,可以利用多核优势
    开线程 40s

四个任务 IO密集型的
单核情况下
    开线程更节省资源
多核情况下
    开线程更节省资源
"""

# 计算密集型
from multiprocessing import Process
from threading import Thread
import os,time
def work():
    res=0
    for i in range(100000000):
        res*=i

if __name__ == '__main__':
    l=[]
    print(os.cpu_count())  # 本机为4核
    start=time.time()
    for i in range(4):
        p=Process(target=work) #耗时  4.732933044433594
        # p=Thread(target=work) #耗时 22.83087730407715
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))




# IO密集型
# from multiprocessing import Process
# from threading import Thread
# import threading
# import os,time
# def work():
#     time.sleep(2) 对比线程的话差不多每个线程几乎同时执行的2s,所用的时间在2s多一点
#
#
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count()) #本机为6核
#     start=time.time()
#     for i in range(4000):
#         p=Process(target=work) #耗时9.001083612442017s多,大部分时间耗费在创建进程上
#         # p=Thread(target=work) #耗时2.051966667175293s多
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))