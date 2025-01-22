"""
生产者：生产、制造数据
消费者：消费、处理数据

例子:做包子的,买包子的
        1.做包子远比买包子的多
        2.做包子的远比包子的少
        供需不平衡的问题
"""

from  multiprocessing import Process,Queue,JoinableQueue
import random
import time

def provider(name,food,q):
    for i in range(10):
        data = '%s生产了%s%i'%(name,food,i)
        time.sleep(random.random())
        q.put(data)
        print(data)

def consumer(name,q):
    while True:
        data = q.get()
        if data == None:break
        print('%s吃了%s'%(name,data))
        time.sleep(random.random())
        q.task_done() # 告诉队列你已经从队列中取出一个数据并且处理完了


if __name__ == '__main__':
    q = JoinableQueue()

    # 两个厨师
    p = Process(target=provider,args=('tom','fish',q))
    p1 = Process(target=provider,args=('jerry','cake',q))

    # 两个吃客
    c = Process(target=consumer,args=('xiyangyang',q))
    c1 = Process(target=consumer,args=('huitailang',q))

    p.start()  # 告诉操作系统要调度启动一个进程了
    p1.start()

    c.daemon = True   #店铺没了食客也就没了
    c1.daemon = True
    c.start()
    c1.start()
    p.join()    # 厨师会等待食客吃完
    p1.join()

    q.join()  # 等待队列中的数据全部取出
    print('食客吃完了')
