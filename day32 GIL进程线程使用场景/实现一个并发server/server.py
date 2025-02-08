"""
因为是网络传输减少资源消耗使用线程实现，现实场景中会用多进程和多线程混合使用，
来利用CPU多核优势。
服务端
    1.要有固定的IP和PORT
    2.24小时不间断提供服务
    3.能够支持并发
"""

import socket
from threading import Thread

server = socket.socket()
server.bind(('127.0.0.1',8081))
server.listen(5)  # 半连接池

"""
核心代码是这样实现，如果要实现多线程把关键部分进行解耦然后封装到函数中
while True:
    conn, addr = server.accept() # 监听等待客户端连接阻塞态
    print(addr)
    try:
        data = conn.recv(1024)
        if len(data) == 0:break
        print(addr)
        print(data.decode('utf-8'))
        conn.send(data.upper())
    except ConnectionResetError as e:
        print(e)
        break
    conn.close()
"""

def task(conn):
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()

if __name__ == '__main__':
    while True:
        conn, addr = server.accept() # 监听等待客户端连接阻塞态
        print(addr)
        t = Thread(target=task,args=(conn,))
        t.start()
