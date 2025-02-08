import queue
"""
同一个进程下的多个线程本来就是数据共享 为什么还要用队列
因为队列是管道+锁  使用队列你就不需要自己手动操作锁的问题 
因为锁操作的不好极容易产生死锁现象
"""

# q = queue.Queue()  # 普通队列
# q.put('hahha')
# print(q.get())


q = queue.LifoQueue()  # 类似堆的功能，先进后出
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())


# q = queue.PriorityQueue()  # 优先级队列
# # 数字越小 优先级越高
# q.put((10,'haha'))
# q.put((100,'hehehe'))
# q.put((0,'xxxx'))
# q.put((-10,'yyyy'))
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())