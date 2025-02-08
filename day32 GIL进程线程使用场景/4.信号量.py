# 信号量在不同的领域有不同的意思

"""
互斥锁:一个厕所(一个坑位)
信号量:公共厕所(多个坑位)
"""

from threading import Semaphore,Thread
import time
import random


sm = Semaphore(5)  # 造了一个含有五个的坑位的公共厕所

def task(name):
    sm.acquire()
    print('%s占了一个坑位'%name)
    time.sleep(random.randint(1,3))
    sm.release()

for i in range(40):
    t = Thread(target=task,args=(i,))
    t.start()

"""
因为每个人上厕所的时间不同，所以每次占的留出来的坑位数量也不同
0占了一个坑位
1占了一个坑位
2占了一个坑位
3占了一个坑位
4占了一个坑位
---
5占了一个坑位6占了一个坑位
---
7占了一个坑位8占了一个坑位
---
9占了一个坑位
---
10占了一个坑位11占了一个坑位
"""