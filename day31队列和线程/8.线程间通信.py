from threading import Thread

money = 666

def task():
    global money
    money = 999

t = Thread(target=task)
t.start()
t.join()
print(money)

"""
task是主进程的子进程，主进程中的变量money是666，线程能够获取到主进程的名称空间中的变量，所以修改的是money.
"""