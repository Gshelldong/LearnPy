
# subprocess 子进程模块

"""
1.用户通过网络连接上了你的这台电脑
2.用户输入相应的命令 基于网络发送给了你这台电脑上某个程序
3.获取用户命令 里面subprocess执行该用户命令
4.将执行结果再基于网络发送给用户
这样就实现  用户远程操作你这台电脑的操作
"""

import subprocess

while True:
    cmd = input('请输入想要执行的命令>>>: ').strip()
    obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE) # shell True
    print("标准输出: ",obj.stdout.read().decode('GBK'))
    print("标准错误输出: ",obj.stderr.read().decode('GBK'))

