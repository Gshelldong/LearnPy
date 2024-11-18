# d = {'name': 'jason', 'password': '123', 'hobby': '泡m'}
# for i in d:
#     print(i)
# for循环后面的in关键 跟的是一个可迭代对象

"""
for循环内部的本质
    1.将in后面的对象调用__iter__转换成迭代器对象
    2.调用__next__迭代取值
    3.内部有异常捕获StopIteration,当__next__报这个错 自动结束循环
"""


# 使用迭代的方式实现
l = ['a','b','c','d','red','blue','yellow']

res = l.__iter__()
while True:
    try:
        print(res.__next__())
    except StopIteration:
        break
