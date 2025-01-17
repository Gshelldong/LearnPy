# 把数据的长度打包成一个固定的大小，用于统一数据长度，方便告知客户端或者负端的数据传输大小。

import struct

res = 'abcdefghijklmn'
print('原始的长度',len(res))

"""
1、当数据长度太大的时候struct无法封装。
  使用一个字典再次把数据的长度进行封装，这样再打包就是字典的长度，自定义字典长度都是在自己的可控范围之内
  而且可以附加自定义的信息。
"""

d = {
    "name": 'jason',
    'file_size': 204800000000,
    'info': 'struct info'
}

import json
json_d = json.dumps(d)
print(len(json_d))   # 字典没有打包的长度

res1 = struct.pack('i',len(json_d))

res2 = struct.unpack('i',res1)[0]
print('解包之后的长度',res2)