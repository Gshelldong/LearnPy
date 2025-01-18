
import socket

server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))
print('服务端已经监听udp 8080端口......')

while True:
    data,addr = server.recvfrom(1024)
    print(data)