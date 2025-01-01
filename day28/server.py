import socket

server = socket.socket()                    # 创建一个socket
server.bind(("127.0.0.1",8080))             # 给socket 绑定IP和端口

server.listen(5)    # 半连接池

conn,addr = server.accept()   # 等待客户端连接