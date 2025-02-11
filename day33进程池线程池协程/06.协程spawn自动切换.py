# gevent模块

from gevent import monkey;monkey.patch_all()  # 由于该模块经常被使用 所以建议写成一行
from gevent import spawn
import time

"""
注意gevent模块没办法自动识别time.sleep等io情况
需要你手动再配置一个参数
"""

def heng():
    print("哼")
    time.sleep(2)
    print('哼')

def ha():
    print('哈')
    time.sleep(3)
    print('哈')

def heiheihei():
    print('嘿嘿嘿')
    time.sleep(5)
    print('嘿嘿嘿')

start = time.time()
g1 = spawn(heng)
g2 = spawn(ha)  # spawn会检测所有的任务
g3 = spawn(heiheihei)
g1.join()
g2.join()
g3.join()
# heng()
# ha()
print(time.time() - start)  # 5.025497913360596 因为自动切换上下文所以总的用时是用时最长任务的时间多一点