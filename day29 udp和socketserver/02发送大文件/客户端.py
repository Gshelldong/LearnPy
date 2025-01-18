import socket
import json
import os
import struct

client = socket.socket()
client.connect(('127.0.0.1',8080))

while True:
    # 获取电影列表并循环展示
    MOIVE_DIR=r'N:\老男孩教育_python视频\day29\视频'
    movie_list = os.listdir(MOIVE_DIR)
    for i,movie in enumerate(movie_list):
        print(f'{i}:{movie}')
    choice = input('请选择上传的电影编号: ')
    if choice.isdigit():
        choice = int(choice)
        if choice in range(0,len(movie_list)):
            # 获取文件的路径
            file_name = movie_list[choice]
            file_path = os.path.join(MOIVE_DIR,file_name)

            # 获取文件大小
            file_size = os.path.getsize(file_path)
            # 定义文件信息的字典
            res_d = {
                'file_name': '看完爽三天.MP4',
                'file_size': file_size,
                'msg': '注意身体'
            }
            # 序列化字典
            json_d = json.dumps(res_d)
            json_bytes = json_d.encode('utf-8')

            # 先制作字典格式的报头
            header = struct.pack('i', len(json_bytes))
            # 发送字典的报头,为了让服务端知道实际的字段长度
            client.send(header)
            # 再发送字典
            client.send(json_bytes)

            # 打开文件并循环发送
            with open(file_path,mode='rb') as f:
                for line in f:
                    client.send(line)
        else:
            print('请输入正确的序号.')
    else:
        print('请输入数字编号.')