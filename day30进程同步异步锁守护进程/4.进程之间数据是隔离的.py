from multiprocessing import Process

money = 100

def test():
    global  money
    money = 9999

if __name__ == '__main__':
    p = Process(target=test)
    p.start()
    p.join()
    """
    在子进程中是一块完全的内存空间，因为进程之间是隔离的，所以在子进程中修改了数据
    在主进程中还是看不到改变的数据
    """
    print(money)