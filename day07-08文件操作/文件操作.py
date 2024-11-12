
# 1.文件没有会直接报错。
# r 是取消转义在，在windows系统中是\开头的会被转义
# f 只是一个变量
# 下面的f1 看出来也是可以正常使用的。
# 默认打开的模式是r
# f.read()  是调用操作系统打开文件
# f.close()  是告诉操作系统关闭文件

# with open(r'a.txt',encoding='utf-8') as f,\
#         open(r'a.txt',encoding='utf-8') as f1:
#     print(f)
#     print(f.read())
#     print(f1)
#     print(f1.read())
# f.close()

# 修改文件，两种方式

'''
1.先把问文件读取到内存在内存中完成修改之后再写会硬盘，
这种方式在文件较大的情况下容易造成内存溢出。
只会存在一个文件不会占用太多的磁盘空间



with open(r'a.txt','r',encoding='utf-8') as f :
    data = f.read()
    print(data)
    print(type(data))

with open(r'a.txt','w',encoding='utf-8') as f:
    res = data.replace('gongxiaoliao','jerry')
    print(res)
    f.write(res)
'''

'''
2.创建一个新文件循环读取老文件的内容到内存进行修改，将修改后的内容写到新的文件中，
将老的删除，把新的改名为老的文件。
优点:内存中始终只有一行内容 不占内存
缺点:再某一时刻硬盘上会同时存在两个文件


import os

with open(r'a.txt','r',encoding='utf-8') as read_f, \
    open(r'a.txt.swap','a',encoding='utf-8') as write_f:
    for line in read_f:
        new_line = line.replace('jerry','Tom')
        write_f.write(new_line)
os.remove('a.txt')
os.rename('a.txt.swap','a.txt')

'''

# 文件的处理模式

"""
文件打开的模式
    r 只读模式
    w 只写模式
    a 追加写模式
操作文件单位的方式
    t 文本文件   t在使用的时候需要指定encoding参数 如果不知道默认是操作系统的默认编码
    b 二进制  一定不能指定encoding参数


with open('a.txt',mode='r',encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    print('>>>1 : ')
    print(f.read())  # 一次性读取全部的文件内容


with open('1.png',mode='rb') as f:
    print(f.readable())
    print(f.writable())
    print('>>>1 : ')
    print(f.read())  # 一次性读取全部的文件内容


with open(r'a.txt','r',encoding='utf-8') as f, \
    open(r'a.txt','r',encoding='utf-8') as f1:
    print(f.readable())
    print(f.writable())
    print('-----------1')
    print(f.read())    # 读取全部的内容
    print('-----------2')
    print(f.read())   # 第二次读取，已经到光标结尾了

    print('=======')
    res = f1.readlines()  # 返回的是一个列表
    for line in res:
        print(line,end='')


with open(r'a.txt','r',encoding='utf-8') as f, \
    open(r'a.txt','r',encoding='utf-8') as f1:
    print(f.readline(),end='')   # 读取一行
    print(f.readline(),end='')   # 读取第二行
    print(f.readline(),end='')   # 读取第三行

"""

'''
w模式： w模式慎用
1.不存在文件会自动创建文件
2.文件存在会清空之后再写入

with open(r'w.txt','w',encoding='utf-8') as f:
    print(f.readable())  # 查看文件是否可读
    print(f.writable())
    f.write('写入第一行\n')  # 一行一行的写
    f.write('写入第二行\n')
    f.write('写入第三行\n')
    l = ['line1\n','line2\n','line3\n']
    f.writelines(l)
    # 等价于
    for i in l:
        f.write(i)
'''

"""
# a 模式
1、文件不存在会创建文件 
2、问及爱你存在的情况下，不会清空文件，把文件的光标移动到最后
"""

with open(r'a.txt','w',encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    f.write('这是最后一行。\n')