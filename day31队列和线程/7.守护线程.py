from threading import Thread,current_thread
import time

def task(i):
    print('线程的名称%s'%current_thread().name)
    time.sleep(i)
    print('GG')

t = Thread(target=task,args=(1,))
t.daemon = True  # 主线程结束就会直接结束,所以task函数还在执行的时候就会结束，不会打印GG。
t.start()
print('主')

# 主线程运行结束之后需要等待子线程结束才能结束呢?
"""
主线程的结束也就意味着进程的结束，同时会释放资源。
主线程必须等待其他非守护线程的结束才能结束，如果主线程直接释放，资源也就释放了，子线程就会异常。
(意味着子线程在运行的时候需要使用进程中的资源,而主线程一旦结束了资源也就销毁了)
"""