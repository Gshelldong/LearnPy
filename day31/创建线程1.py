"""
重写Thred模块的run方法
"""

from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running!'%self.name)
        time.sleep(3)
        print('%s is over!'%self.name)

if __name__ == '__main__':
    t = MyThread('gong')
    t.start()
    print('master')