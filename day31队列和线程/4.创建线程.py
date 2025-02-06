from threading import Thread

import time

def task(name):
    print('%s is running '%name)
    time.sleep(3)
    print('%s is over '%name)

if __name__ == '__main__':
    # 启动线程不一定要在main里面，但是习惯性的写在这里
    t = Thread(target=task,args=('gong',))
    t.start()   # 告诉操作系统启动的一个线程，线程的开销远远小于进程
    # 代码执行完线程就已经执行了
    print('主')