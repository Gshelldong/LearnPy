"""
通过一个从客户端输入命令发送到服务端，服务端执行命令之后把结果通过tcp返回给客户端的的案例
来详细的了解tcp的通信过程。

1.首先我们设置的缓存是1024bytes,但是如果返回的命令结果的长度大于1024bytes
就会导致我们从内存中拿到的数据只有1024bytes,再次从客户端输入命令的时候还是返回上次没有返回完的结果。

2.要解决这个问题我们首先要知道服务端返回数据的长度，然后发送给客户端，客户端根据长度来决定多次从内存中取出数据。
"""
import json
import socket
import struct
import subprocess


# 先创建一个server
server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn, addr = server.accept() # 等待客户端连接

    # 循环接收来自客户端的数据
    while True:
        try:
            cmd = conn.recv(1024)
            if len(cmd) ==0:break
            cmd = cmd.decode('utf-8')
            obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            res = obj.stdout.read() + obj.stderr.read()
            d = {'name': 'cmd_res','file_size':len(res),'info': 'asdfg'}
            json_d = json.dumps(d)
            # 1.先制作一个字典的报头
            header = struct.pack('i',len(json_d))
            # 2.发送字典报头
            conn.send(header)
            # 3.发送字典
            conn.send(json_d.encode('utf-8'))
            # 3.发送真实数据
            conn.send(res)
        except ConnectionResetError:
            break
    conn.close()




















