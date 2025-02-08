from threading import Thread
import time

"""
GIL本质也是一把互斥锁:将并发变成串行牺牲效率保证数据的安全 
用来阻止同一个进程下的多个线程的同时执行(同一个进程内多个线程无法实现并行但是可以实现并发)
"""

n = 100

def task():
    global n
    tmp = n
    # time.sleep(0.1) 在这里如果没有io每次修改数据都会有锁，
    # 所以正常的结果是0，但是如果有IO,GIL锁会被释放，
    # 导致在恢复程序运行之后拿到的数据都是同一个数据
    # 所以使用GIL来保证程序的数据安全是有问题的，需要单独为数据加锁处理
    n = tmp -1

t_list = []
for i in range(100):
    t = Thread(target=task)
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print(n)   # -> 99