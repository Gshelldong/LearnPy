import socket

"""
服务端固定的IP和port
7*24h不间断的提供服务
"""

server = socket.socket()           # 生成一个服务器对象
server.bind(('127.0.0.1',8080))    # 绑定IP和端口
server.listen(5)                   # 半连接池

while True:
    conn, addr = server.accept()  # 等别人来连接
    print(addr)    # 打印客户端的地址
    while True:
        try:
            data = conn.recv(1024)  # 获取客户端发过来的地址
            print(data)
            if len(data) == 0:break # 针对mac和linux客户端异常退出之后服务端不会报错会一直接收b''
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()