from  multiprocessing import Process
import time

def test(name):
    print('%s总管活着'%name)
    time.sleep(3)
    print('%s总管死了'%name)


if __name__ == '__main__':
    p = Process(target=test,args=('gong',))
    p.daemon = True  # 将该进程设置为守护进程，守护的程序挂了就直接挂了，p必须在start语句之前否则报错。
    p.start()
    time.sleep(6) # 在cpu特别繁忙的情况下，这里的时间如果很短不会触发守护进程的内容
    print('挂了')  # 这里启动的就是守护的进程