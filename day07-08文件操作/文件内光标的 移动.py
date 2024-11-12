
# 在rt模式下 read内的数字 表示的是字符的个数
# 除此之外,数字表示的都是字节
'''
with open(r'a.txt','r',encoding='utf-8') as f:
     print(f.read(5))


with open(r'a.txt','rb') as f:
    res = f.read(3)  # 读的是三个字节bytes
    print(res)
    print(res.decode('utf-8'))
'''

# 文件内光标的移动
"""
f.seek(offset,whence)
offset:相对偏移量  光标移动的位数
whence:
    0:参照文件的开头   t和b都可以使用
    1:参照光标所在的当前位置  只能在b模式下用
    2:参照文件的末尾  只能在b模式下使用


with open(r'a.txt',mode='rt',encoding='utf-8') as f:
    print(f.read(1))
    f.seek(6,0)   # seek移动的都是字节数
    print(f.read(1))
    f.seek(4,0)
    print(f.read(1))
    f.seek(0,0)
    print(f.read(1))

with open(r'a.txt',mode='rb') as f:
    print(f.read(3).decode('utf-8'))
    f.seek(0,0)
    print(f.read(3).decode('utf-8'))
    f.seek(6,0)
    print(f.read(1).decode('utf-8'))
    f.seek(4,0)
    print(f.read(1).decode('utf-8'))
    f.seek(4,1)
    print(f.read(1).decode('utf-8'))

"""

# a.txt -> abc1234567890
# 读取都是向后读取的

# with open(r'a.txt',mode='rb') as f:
#     f.seek(3,0)
#     print(f.read(1).decode('utf-8'))
#     f.seek(4,1)
#     print(f.read(1).decode('utf-8'))


