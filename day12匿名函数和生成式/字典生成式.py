l1 = ['name','password','hobby']
l2 = ['jason','123','DBJ','egon']

"""
# 这种方式生成需要 l1 >= l2的长度，不然会报错。
d = {}
for i,j in enumerate(l1): # enumerate 可以生成列表的索引和相对应的值
    d[j] = l2[i]    # 把d[j]的值 = i是d[j]所在的索引值
print(d)



l1 = ['jason','123','read']
d = {i:j for i,j in enumerate(l1) if j != '123'} # 这里的i是索引 {0: 'jason', 2: 'read'}
print(d)
"""

res = {i for i in range(10) if i != 4}
print(res)
res1 = (i for i in range(10) if i != 4)  # 这样写不是元组生成式 而是生成器表达式
print(list(res1))
for i in res1:
    print(i)
