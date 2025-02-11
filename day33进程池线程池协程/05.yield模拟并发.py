#串行执行 0.8540799617767334
# import time
#
# def func1():
#     for i in range(10000000):
#         i+1
#
# def func2():
#     for i in range(10000000):
#         i+1
#
# start = time.time()
# func1()
# func2()
# stop = time.time()
# print(stop - start)


#基于yield并发执行  1.3952205181121826
import time
def func1():
    while True:
        10000000+1
        yield

def func2():
    g=func1()
    for i in range(10000000):
        # time.sleep(0.1)  # 模拟IO，yield并不会捕捉到并自动切换，如果是计算型的任务可以直接使用yeild的方式执行，
        # 但是无法自动识别io并切换
        i+1
        next(g)

start=time.time()
func2()
stop=time.time()
print(stop-start)

"""
需要找到一个能够识别IO的一个工具
"""














