def index():
    username = '我是局部命名空间的username.'
    print(username)
    print(locals())    # 查看局部名称空间
    print(globals())   # 查看全局名称空间

# index()


# s = 'hello'
# print(s.encode('utf-8'))
# print(bytes(s,encoding='utf-8'))

l = 'dashabi'

# print(callable(l))
# print(callable(index))
# print(dir(l))


# 取商和余数
# print(divmod(103,10))

# 实现一个分页器
# total_num,more = divmod(103,10)
# if more:
#     total_num +=1
# print(total_num)

# eval不支持逻辑代码,只支持一些简单的python代码
# s1 = """
# print(1 + 2)
# x = [i for i in range(10)]
# print(x)
# """
# eval(s1)
# exec(s1)

# format()
# print("我得名字是{},我今年{}岁，我喜欢{}.".format())

l = [1,2,3,4]
print(isinstance(l,list))

# 2的3次方
print(pow(2,3))

# 四舍五入 -> 3.142
print(round(3.14159,3))