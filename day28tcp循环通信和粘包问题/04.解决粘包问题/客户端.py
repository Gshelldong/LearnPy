import socket
import struct
import json

client = socket.socket()
client.connect(('127.0.0.1',8080))

while True:
    msg = input('>>>: ').strip()
    msg = msg.encode('utf-8')
    if len(msg) == 0:continue
    client.send(msg)
    # 1.先接收字典报头
    header_dict = client.recv(4)
    # 2.解析报头
    dict_size = struct.unpack('i',header_dict)[0]  # 解包的时候一定要加上索引0
    # 3.接收字典数据
    dict_bytes = client.recv(dict_size)
    dict_json = json.loads(dict_bytes.decode('utf-8'))
    # 4.获取字典中的信息
    print(dict_json)
    recv_size = 0
    real_data = b''
    while recv_size < dict_json.get('file_size'):  # 服务端执行cmd返回结果的长度
        data = client.recv(1024)
        real_data += data
        recv_size += len(data)
    print(real_data.decode('gbk'))
