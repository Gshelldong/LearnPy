"""
r
w
a
将上面的三个模式称为纯净模式
r+
w+
a+
"""

# 带上+号之后的只读模式能够被写入，写入不会清空原来的内容
'''
with open(r'a.txt',mode='r+',encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    print(f.readline())
    f.write('嘿嘿嘿')


# 清空了文件内的内容，与正常模式相同
with open(r'a.txt', mode='w+',encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    print(f.readline())
    f.write('哈哈哈哈!')
'''

with open(r'a.txt',mode='r+b') as f:
    print(f.writable())
    print(f.readable())
    res = f.read()
    print(res.decode('utf-8'))
    res1 = str(res.decode('utf-8'))
    print(res1)

