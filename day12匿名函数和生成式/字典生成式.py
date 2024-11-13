l1 = ['name','password','hobby']
l2 = ['jason','123','DBJ','egon']

d = {}
for i,j in enumerate(l1):
    d[j] = l2[i]
print(d)


l1 = ['jason','123','read']
d = {i:j for i,j in enumerate(l1) if j != '123'}
print(d)


# res = {i for i in range(10) if i != 4}
# print(res)
# res1 = (i for i in range(10) if i != 4)  # 这样写不是元组生成式 而是生成器表达式
# print(res1)
# for i in res1:
#     print(i)
