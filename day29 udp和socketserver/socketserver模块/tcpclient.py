import socket

client = socket.socket()
client.connect(('127.0.0.1',8080))

client.send(b'hello')
res = client.recv(1024)
print(res)