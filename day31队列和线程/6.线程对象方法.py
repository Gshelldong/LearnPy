from threading import Thread,current_thread,active_count
import time
import os

def task(name,i):
    print('%s is running'%name)
    print('子current_thread:',current_thread().name)  # 线程的名称
    print('进程的pid: ',os.getpid())  # 获取进程的pid
    time.sleep(i)

    print('%s is over'%name)

t = Thread(target=task,args=('egon',1))
t1 = Thread(target=task,args=('gong',2))
print('主进程的pid: %s'%os.getpid())
t.start()  # 线程的开销远小于进程
t1.start()

t1.join()     # 主线程等待子线程完成任务
print('当前正在活跃的线程数',active_count())

# 小的代码执行完 线程就已经开启了
print('主')
# print('主current_thread:',current_thread().name)
