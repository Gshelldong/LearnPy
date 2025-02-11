from gevent import monkey;monkey.patch_all()
import socket
from gevent import spawn

server = socket.socket()
server.bind(('127.0.0.1',8081))
server.listen(5)

# 把连接循环和通信循环区分开

def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break

def server1():
    while True:
        conn, addr = server.accept()  # 阻塞
        spawn(talk,conn)  # 这里切换到talk执行并把conn作为参数传到函数里面

if __name__ == '__main__':
    g1 = spawn(server1)
    g1.join()  # 主线程一直等待子线程完成任务，不然程序会直接结束