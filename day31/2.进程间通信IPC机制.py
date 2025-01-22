from multiprocessing import Process,Queue

"""
子进程放数据主进程获取数据，或者两个子进程互相放、取数据
"""


def provider(q):
    q.put('hahaha')

def consumer(q):
    print(q.get_nowait())  # 因为get会不断的等待所以在下面的进程中不管是消费者先启动还是生产者先启动都会把生产者的消息打出来
    # print(q.get()) 但是这种情况久不一定了，因为不知道操作系统到底是控制那个子进程先启动，如果是消费者先启动且不等待，就会直接导致报错

if __name__ == '__main__':
    q = Queue(5)
    p = Process(target=provider,args=(q,))
    p1= Process(target=consumer,args=(q,))
    p.start()
    p1.start()
    print('主')