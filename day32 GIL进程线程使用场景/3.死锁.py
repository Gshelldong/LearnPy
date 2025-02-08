from threading import Thread,Lock,current_thread,RLock
import time
"""
Rlock可以被第一个抢到锁的人连续的acquire和release
每acquire一次锁身上的计数加1
每release一次锁身上的计数减1
只要锁的计数不为0 其他人都不能抢

"""
# mutexA = Lock()
# mutexB = Lock()
mutexA = mutexB = RLock()  # A B现在是同一把锁

class MyThread(Thread):
    def run(self):  # 创建线程自动触发run方法 run方法内调用func1 func2相当于也是自动触发
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('%s抢到了A锁'%self.name)  # self.name等价于current_thread().name
        mutexB.acquire()
        print('%s抢到了B锁'%self.name)
        mutexB.release()
        print('%s释放了B锁'%self.name)
        mutexA.release()
        print('%s释放了A锁'%self.name)

    def func2(self):
        mutexB.acquire()
        print('%s抢到了B锁'%self.name)
        time.sleep(1)
        mutexA.acquire()
        print('%s抢到了A锁' % self.name)
        mutexA.release()
        print('%s释放了A锁' % self.name)
        mutexB.release()
        print('%s释放了B锁' % self.name)

for i in range(10):
    t = MyThread()
    t.start()

# class Demo(object):
# #     pass
# #
# # obj1 = Demo()
# # obj2 = Demo()
# # print(id(obj1),id(obj2))
"""
只要类加括号实例化对象
无论传入的参数是否一样生成的对象肯定不一样
单例模式除外


自己千万不要轻易的处理锁的问题，除非做底层开发。
"""

