def func4():
    return [[1,2,3,4],[4,5,6,7],[2,3,4,5]]

res = func4()
print(res)



import socket

server= socket.socket()
server.bind(('127.0.0.1',8000))
server.listen()

conn, addr = server.accept()
data = conn.recv(1024)