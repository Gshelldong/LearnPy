import socket

client = socket.socket(type=socket.SOCK_DGRAM)
server_address = ('127.0.0.1',8080)

while True:
    msg = input('>>>:')
    msg = '来自客户端1的消息%s'%msg
    client.sendto(msg.encode('utf-8'),server_address)
    data, server_address = client.recvfrom(1024)
    print(data.decode('utf-8'))