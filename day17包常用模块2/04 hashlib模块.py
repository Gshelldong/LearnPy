# hashlib 模块是用来加密数据的，里面有各种加密算法
# 在加密的时候只接收二进制流

import hashlib

# 应用场景密码加密
# md = hashlib.md5()
# md.update(b'admin123')
# res = md.hexdigest()
# print(res)  # 返回加密之后的内容 0192023a7bbd73250516f069df18b500

"""
1.不用的算法 使用方法是相同的
密文的长度越长 内部对应的算法越复杂
但是
    1.时间消耗越长
    2.占用空间更大
通常情况下使用md5算法 就可以足够了

"""

# 同样的内容分多次传入得到的结果都是一样的

# say = 'howareyou'
# md = hashlib.md5()
# md.update(say.encode('utf-8'))
# res_say = md.hexdigest()
# print(res_say)
#
#
# say1= 'how'
# say2= 'are'
# say3= 'you'
# md1 = hashlib.md5()
# md1.update(say1.encode('utf-8'))
# md1.update(say2.encode('utf-8'))
# md1.update(say3.encode('utf-8'))
# res_count = md1.hexdigest()
# print(res_count)


# 应用场景文件校验
# content = hashlib.md5()
# with open(r'my.log',mode='rb') as f:
#     for line in f.readlines():
#         content.update(line)
#     print(content.hexdigest().upper())   # md5 -> 8aa9844d3f3c4af7d9cbe7eb60e659ae
# f.close()


# 加盐,为了防止MD5被撞库,我们在原本的明文基础之上再进行添加一点内容
# 这样久可以保证加密之后的内容不会很容易的算出结果。
# 这样就保证密码admin123不能够被随便解密

md = hashlib.md5()
password='admin123'
md.update(b'Mypas.11122@')
md.update(password.encode('utf-8'))
res_pas = md.hexdigest()
print(res_pas)


