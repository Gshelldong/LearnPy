
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data,sock = self.request
            print(self.client_address)  # 客户端的IP地址
            print(data.decode('utf-8'))
            sock.sendto(data.upper(),self.client_address)

if __name__ == '__main__':
    """只要有客户端连接  会自动交给自定义类中的handle方法去处理"""
    server = socketserver.ThreadingUDPServer(('127.0.0.1',8080),MyServer)  # 创建一个基于UDP的对象
    server.serve_forever()  # 启动该服务对象