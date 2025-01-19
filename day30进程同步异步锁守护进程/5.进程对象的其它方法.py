from multiprocessing import Process,current_process
import os
import time

def test(name):
    print('%s is running'%current_process().pid)
    time.sleep(3)
    print('%s is over.')


if __name__ == '__main__':
    p = Process(target=test,args=('gong',))
    p.start()
    p.terminate()      # 杀死当前进程其实是告诉操作系统帮你杀死一个进程，这个进程什么时候被杀死是由操作系统决定
    time.sleep(0.1)    # 让操作系统有反应杀死进程的时间
    print(p.is_alive())  # 判断进程是否存在
    print('主,主进程pid%s'%os.getpid(),'主主进程%s'%os.getppid())