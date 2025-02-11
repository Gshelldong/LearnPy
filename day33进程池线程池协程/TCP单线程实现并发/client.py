import socket
from threading import Thread,current_thread


def client():
    client = socket.socket()
    client.connect(('127.0.0.1',8081))
    n = 0
    while True:
        data = '%s %s'%(current_thread().name,n)
        client.send(data.encode('utf-8'))
        res = client.recv(1024)
        print(res.decode('utf-8'))
        n += 1

for i in range(400):  # 启动400个线程
    t = Thread(target=client)
    t.start()

