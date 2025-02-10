from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time
import os

pool = ThreadPoolExecutor(5)  # 括号内可以传参数指定线程池内的线程个数
# 也可以不传不传默认是当前所在计算机的cpu个数乘5

"""
池子中创建的进程/线程创建一次就不会再创建了
至始至终用的都是最初的那几个
这样的话节省了反复开辟进程/线程的资源
"""

def task(n):
    print(n,os.getpid())  # 查看当前进程号
    time.sleep(2)  # 这里睡了2s
    return n**2

"""
提交任务的方式
    同步：提交任务之后原地等待任务的返回结果期间不做任何事
    异步：提交任务之后不等待任务的返回结果(异步的结果怎么拿？？？) 直接执行下一行代码
"""
stat_time = time.time()
res1 = pool.submit(task,2)  # 朝线程池中提交任务异步提交
print(res1.result())
res2 = pool.submit(task,3)  # 朝线程池中提交任务异步提交
print(res2.result())
print('主')
print(time.time() - stat_time)  # 执行了4s多一点

"""
这种写法不太科学，因为如果说我要提交20的线程的话意味这我要把重复的代码写20次，
而且在使用result()函数之后，每个线程的执行都成了串行的。
"""


