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


# 优化01.创建线程池
if __name__ == '__main__':
    t_list = []
    for i in range(20):
        res = pool.submit(task,i)
        # print(res.result())  # 如果在在这里执行resault就会变成串行，原地等待每个任务的返回结果之后再依次向下执行
        t_list.append(res)
    pool.shutdown()  # 关闭池子 等待池子中所有的任务执行完毕之后才会往下运行代码

    # 这里会在处理完成之后批量的把任务的结果返回，且结果是有序的
    for p in t_list:
        print('>>>:',p.result())  # resault函数会获取函数的return

"""
0 7460
1 7460
2 7460
3 7460
4 7460
5 7460
6 7460
789 7460 7460 
7460

10 7460
11 74601213
 7460
14  74607460

15 7460
16 7460
1718 7460
 746019
 7460
>>>: 0
>>>: 1
>>>: 4
>>>: 9
>>>: 16
>>>: 25
>>>: 36
............................
"""

