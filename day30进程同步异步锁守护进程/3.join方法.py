from multiprocessing import Process
import time

def test(name,i):
    print('%s is running'%name)
    time.sleep(i)
    print('%s is over'%name)

if __name__ == '__main__':
    # 使用循环的方式可以减少代码量
    # p_list = []
    # for i in range(3):
    #     p = Process(target=test,args=('进程%s'%i,i))
    #     p.start()
    #     p_list.append(p)
    # for p in p_list:
    #     p.join()


    p = Process(target=test,args=('gong',1))
    p1 = Process(target=test,args=('xiao',2))
    p2 = Process(target=test,args=('app',3))
    start_time = time.time()
    p.start() # 仅仅是告诉操作系统帮你创建一个进程至于这个进程什么时候创操作系统随机决定
    p1.start()
    p2.start()

    p.join()
    p1.join()
    p2.join()
    # 主进程代码等待子进程运行结束 才继续运行
    # p.join()  # 主进程代码等待子进程运行结束
    # 因为启动的每一个进程都互不影响，主进程又要等待子进程完成之后才执行，所以程序
    # 消耗的时间一定大于用时最久的那个子进程。
    print('主')
    print(time.time() - start_time)