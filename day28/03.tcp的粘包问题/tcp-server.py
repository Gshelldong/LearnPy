import socket

server = socket.socket()  # 创建服务端，默认使用tcp协议
server.bind(('127.0.0.1',8080))  # 创建监听地址
server.listen(5)  # 半连接池

conn, addr = server.accept()   # 等待客户端连接
data = conn.recv(1024)         # 从客户端拿到数据
print(data)
"""
这里会把客户端分三次发送过来的数据一次性打印了，因为tcp的特性是一次连接多次通信
b'firstsecendthred'
b''
b''
"""
data = conn.recv(1024)
print(data)
data = conn.recv(1024)
print(data)