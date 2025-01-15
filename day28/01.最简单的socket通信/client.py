
import socket

client = socket.socket()

client.connect(('127.0.0.1',8080))  # 连接到服务端

client.send(b'hello word~')         # 给服务端发送一条信息
res = client.recv(1024)                   # 接收一条来自服务端的信息
print(res)
# 关闭连接
client.close()

"""
这种方式通常只能服务客户端一次就挂了，我们是希望服务端能够提供持续的服务。
所以使用连接循环来暂时解决这个问题
"""