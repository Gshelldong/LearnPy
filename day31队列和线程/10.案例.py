from threading import Thread
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)
    t1.daemon=True
    t1.start()
    t2.start()
    print("main-------")

# 主进程会等待t2执行完成之后才会结束，t1因为运行的是1s时间是小于t2的，所以t1能够正常的结束。
# t1 在这里设置为守护进程对程序的打印结果没有太大影响