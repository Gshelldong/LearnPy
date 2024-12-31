
# 定义一个简单的Lambda函数，对传入的参数求平方
square = lambda x: x * x

# 调用Lambda函数
result = square(5)
print(result)  # 输出: 25


# x,y 作为参数传入，返回x,y的和
res = (lambda x,y:x+y)(1,3)

print(res)