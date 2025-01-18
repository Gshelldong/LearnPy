import socket

"""
udp 没有粘包的问题，发什么服务端就接收什么
"""

client = socket.socket(type=socket.SOCK_DGRAM)

server_address = ('127.0.0.1',8080)

# 不需要建立连接直接发送数据
client.sendto(b'hello',server_address)
client.sendto(b'hello',server_address)
client.sendto(b'hello',server_address)