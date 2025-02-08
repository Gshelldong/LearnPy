"""
用途：
1. 用来让进程之间等待。
"""
import time
from threading import Thread,Event

# 生成一个事件对象
event = Event()

def light():
    print('红灯')
    time.sleep(3)
    event.set() # 发信号
    print('绿灯')

def car(name):
    print('%s正在等待红灯。'%name)
    event.wait()  # 等待信号
    print('%s加油门飙车了。'%name)

t = Thread(target=light)
t.start()

for i in range(10):
    t = Thread(target=car,args=('%s人员.'%i,))
    t.start()