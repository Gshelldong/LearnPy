from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time
import os

pool = ThreadPoolExecutor(5)  # 括号内可以传参数指定线程池内的线程个数

"""
池子中创建的进程/线程创建一次就不会再创建了
至始至终用的都是最初的那几个
这样的话节省了反复开辟进程/线程的资源
"""

def task(n):
    print(n,os.getpid())  # 查看当前进程号
    time.sleep(2)
    return n**2


def call_back(n):
    print('拿到了异步提交任务的返回结果:',n.result())

"""
提交任务的方式
    同步：提交任务之后 原地等待任务的返回结果 期间不做任何事
    异步：提交任务之后 不等待任务的返回结果(异步的结果怎么拿？？？) 直接执行下一行代码
"""

"""
异步回调机制:当异步提交的任务有返回结果之后，会自动触发回调函数的执行.
"""
if __name__ == '__main__':
    t_list = []
    for i in range(20):
        # 提交任务的时候绑定一个回调函数,一旦该任务有结果立刻执行对于的回调函数
        # 因为每个任务完成的时间不同所以返回的结果是无序的
        res = pool.submit(task,i).add_done_callback(call_back)
"""
0 4816
1 4816
2 4816
3 4816
4 4816
拿到了异步提交任务的返回结果: 0
拿到了异步提交任务的返回结果: 4
拿到了异步提交任务的返回结果: 569
7  4816 4816
................................
"""
