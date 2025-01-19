"""
创建进程就是在内存中重新开辟一块内存空间
将允许产生的代码丢进去
一个进程对应在内存就是一块独立的内存空间

进程与进程之间数据是隔离的 无法直接交互
但是可以通过某些技术实现间接交互
"""

# 第一种方式创建进程
from multiprocessing import Process
import time

def test(name):
    print('%s is running'%name)
    time.sleep(3)
    print('%s is end' % name)

"""
windows创建进程会将代码以模块的方式从上向下执行一遍
linux会直接将代码完完整整的拷贝一份

windows 创建进程一定要在if __name__ == '__main__':否则会报错
"""

if __name__ == '__main__':
    p = Process(target=test,args=('gong',))  # 固定的使用方式target传入函数名称，args用元组传入函数的参数
    p.start()    # 启动一个子进程
    print('运行主进程')
    # 会等到子进程结束，同步
    print('等待子进程结束...')