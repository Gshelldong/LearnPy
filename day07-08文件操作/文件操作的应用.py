# 写日志
"""
import time

res = time.strftime('%Y-%m-%d %X')
# print(res)

with open(r't.log',mode='a',encoding='utf-8') as f:
    f.write('%s 今天记录了一行日志.\n' %res)


# 检测文件内容
with open(r'test01.txt','rb') as f:
    # 先将光标移动到文件末尾
    f.seek(0,2)
    while True:
        res = f.readline()
        if res:
            print("新增的文件内容:%s"%res.decode('utf-8'),end='')


# 截断文件
with open(r'test01.txt','a',encoding='utf-8') as f:
    f.truncate(6)
    # 接收的字节的长度 整型
    # 保留0~6字节数 后面的全部删除(截断)

"""

