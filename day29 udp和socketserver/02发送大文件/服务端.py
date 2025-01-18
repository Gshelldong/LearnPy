import socket
import json
import struct

server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        try:
            header_len = conn.recv(4)
            # 解析字典报头
            header_len = struct.unpack('i',header_len)[0]
            # 接收字典中的数据
            header_dict = conn.recv(header_len)
            real_dic = json.loads(header_dict.decode('utf-8'))
            print(real_dic)
            total_size = real_dic.get('file_size')
            # 循环写入文件
            recv_size = 0
            with open(real_dic.get("file_name"),'wb') as f:
                while recv_size < total_size:
                    data = conn.recv(1024)
                    f.write(data)
                    recv_size += len(data)
                print('上传成功')
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()
