import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('触发执行')
        while True:
            data = self.request.recv(1024)
            if len(data) == 0:break
            print(self.client_address)
            print(data.decode('utf-8'))
            self.request.send(data.upper())

if __name__ == '__main__':
    """
    只要有客户端连接  会自动交给自定义类中的handle方法去处理
    """
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)  # 创建一个tcp对象
    server.serve_forever()   # 启动服务对象