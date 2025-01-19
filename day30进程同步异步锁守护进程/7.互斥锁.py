from multiprocessing import Process,Lock
import time
import json

# 查票
def search(i):
    with open('data','r',encoding='utf-8') as f:
        data = f.read()
    t_d = json.loads(data)
    print('用户%s查询余票为:%s'%(i,t_d.get('ticket')))

# 买票
def buy(i):
    with open('data','r',encoding='utf-8') as f:
        data = f.read()
    t_d = json.loads(data)
    time.sleep(1)
    if t_d.get('ticket') > 0:
        # 票数减一
        t_d['ticket'] -= 1
        # 更新票数
        with open('data','w',encoding='utf-8') as f:
            json.dump(t_d,f)
        print('用户%s抢票成功'%i)
    else:
        print('没票了')


def run(i,mutex):
    search(i)
    mutex.acquire()  # 抢锁只要有人抢到了锁其他人必须等待该人释放锁
    buy(i)
    mutex.release()  # 释放锁

"""
如果不加锁根据多进程的原理，在启动多个run()进程操作系统会为每一个进程分配独立的内存空间
这个时候大家都会去读取data中的数据获得的票数的结果都是1，就会造成数据混乱。
所以现在加一把锁，让某个进程竞争到锁就独享这个资源，在这个进程操作完之后其它进程才能继续使用这个资源，
之后的进程获取到的资源已经是上一个资源操作完之后的结果，这样就不会造成数据混乱。
"""

if __name__ == '__main__':
    mutex = Lock()  # 生成了一把锁
    for i in range(10):
        p = Process(target=run,args=(i,mutex))
        p.start()



