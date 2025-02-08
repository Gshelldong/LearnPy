import socket
import time

client = socket.socket()
client.connect(('127.0.0.1',8081))

while True:
    client.send(b'hello')
    time.sleep(1)
    data = client.recv(1024)
    print(data.decode('utf-8'))