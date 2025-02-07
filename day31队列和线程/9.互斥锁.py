from threading import Thread,Lock
import time

n = 100


def task(mutex):
    global n
    mutex.acquire() # 加锁
    tmp = n
    time.sleep(0.1)
    n = tmp - 1
    mutex.release()  # 释放锁

t_list = []
mutex = Lock()
for i in range(100):
    t = Thread(target=task,args=(mutex,))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print(n)

"""
启动了多线程，但是在执行的时候，线程的开销很小，在sleep之后可能每个线程拿到的都是100，就导致每个tmp拿到的都是100
在-1之后还是99,要解决这个问题需要给数据加锁,保证操作这个数据的是某一个线程。
"""

