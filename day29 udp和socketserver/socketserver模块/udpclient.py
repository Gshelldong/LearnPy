import socket

# 创建一个udp连接
client = socket.socket(type=socket.SOCK_DGRAM)
client.connect(('127.0.0.1',8080))

client.send(b'hello')
data = client.recv(1024)
print(data.decode('utf-8'))