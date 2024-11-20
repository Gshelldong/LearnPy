"""
序列化
    序列:字符串
    序列化:其他数据类型转换成字符串的过程

写入文件的数据必须是字符串
基于网络传输的数据必须是二进制

    d = {'name':'jason'}   字典
    str(d)

    序列化:其他数据类型转成字符串的过程
    反序列化:字符串转成其他数据类型

    json模块(******)
        所有的语言都支持json格式
        支持的数据类型很少  字符串 列表 字典 整型 元组(转成列表)  布尔值

    pickle模块(****)
        只支持python
        python所有的数据类型都支持

dumps:序列化 将其他数据类型转成json格式的字符串
loads:反序列化 将json格式的字符串转换成其他数据类型

dump load
"""

import json
# 将一个字典类型序列化
# d = {'tom': '123456'}
#
# res = json.dumps(d)
# print(res,type(res))
#
# print('='*100)
# 序列化之后直接写入文件
# with open(r'userinfo.json',mode='w',encoding='utf-8') as f:
#     json.dump(res,f)  # dump可以序列化之后直接写入文件。

# 加载序列化之后的文件
# with open(r'userinfo.json',mode='r',encoding='utf-8') as f:
#     res_json = json.load(f)  # 从文件中读取json
#     a = json.loads(res_json) #把json转换为python中的对象.
#     print(a,type(a))
#     # print(type(res_json))


# with open('userinfo.json','r',encoding='utf-8') as f:
#     for line in f:
#         res = json.loads(line)
#         print(res,type(res))
# t = (1,2,3,4)
# print(json.dumps(t))

import pickle
# 将对象直接转成二进制

d = {'name': 'tom'}
res = pickle.dumps(d)
print(res,type(res))

print('反序列化二进制!')
res1 = pickle.loads(res)
print(res1,type(res1))

print("="*100)

# 用pickle操作文件的时候 文件的打开模式必须是b模式
with open(r'bin_userinfo',mode='wb') as f:
    pickle.dump(d,f) # 直接把内容以二进制方式写入文件

with open(r'bin_userinfo',mode='rb') as f:
    re = pickle.load(f)
    print(re,type(re))




