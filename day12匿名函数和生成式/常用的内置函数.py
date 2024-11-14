# 最大值
#l = [1,2,3,454,56,0,8]   # 内部是基于for循环的

#print(max(l))

# 打印ascii索引对应的字符
#print(chr(97))  # -> a

# 比较工资打印人名
# d = {
#     'tom': 1000,
#     'jerry': 2099,
#     'mario': 1024,
#     'deban': 1234
# }

# max 函数传入一个可迭代对象d ,key是指定用什么来排序传入一个函数，这里
# 引用的是for i in d,r然后把i传入后面的lambda表达式，用d[i]对应的值
# 做比较。min()同理。
# res = max(d,key=(lambda name:d[name]))  # 基于for循环
# print(res)
#
# res1 = min(d,key=(lambda name:d[name]))
# print(res1)



# map 映射  ,把列表中的元素都加1
l = [1,2,3,4,5,6]

print(list(map(lambda x:x+1,l)))


# zip 拉链，把列表组合成元祖，返回在一个列表中，以最短的列表为准。
l1 = [1,2,3]
l2=['tom','jerry','brand']
l3=['zz','aa','bb']

z = zip(l1,l2,l3)
print(list(z))

# filter 把可迭代对象中符合条件的元素过滤出来

x = [1,2,3,4,5,6,7,8,9]
# 实现取余
y = list(filter(lambda i:i%2==0,x))
print(y)


# 排序
s1 = [1,23,4,2,65,7,2,54]
print(sorted(s1,reverse=True))

# 给列表中的元素求和
from functools import reduce
s1 = [1,23,4,2,65,7,2,54]
print(reduce(lambda x,y:x+y,s1,2))  # 最后一个参数是累加从2开始
