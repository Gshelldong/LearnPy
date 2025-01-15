import socket

server = socket.socket()                    # 创建一个socket
server.bind(("127.0.0.1",8080))             # 给socket 绑定IP和端口

server.listen(5)              # 半连接池允许客户端的连接数 允许最大6个客户端同时连接
conn,addr = server.accept()   # 等待客户端连接

data = conn.recv(1024)        # 接收客户端的数据从内存空间1024那么大的数据去拿数据
print(data)

conn.send(b'xixi')            # 像客户端回复一句话

# 关闭连接
conn.close()
server.close()

