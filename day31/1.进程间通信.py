"""
使用队列来进行进程间的通信。
队列: 先进先出
堆： 先进后出
"""
import queue
from multiprocessing import Queue

q = Queue(5)   # 这个队列的最大长度是5，如果不设置参数会有一个默认值
# 向队列中添加数据
q.put(1)
q.put(2)
print(q.full())   # 判断队列是否满了
q.put(3)
q.put(4)
q.put(5)
# q.put(6)   # 当队列满了之后再放入数据不会报错会原地等待知道队列中有数据被取走（阻塞态）
             # 比如现在这个示例程序就会一直卡在这里不会动



print(q.get())
print(q.get())
print(q.empty())   # 判断队列是否取完
print(q.get())
print(q.get())
print(q.get())
print(q.empty())

try:
    print(q.get_nowait())  # 取值没有值不等待直接报错
except queue.Empty as e:
    print('队列中没有数据了',e)

print(q.get())  # 当队列中的数据被取完之后再次获取程序会阻塞直到有人往队列中放入值