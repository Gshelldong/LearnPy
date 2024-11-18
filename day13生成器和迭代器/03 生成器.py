def func():
    print('第一')
    yield 'first'  # 函数内如果有yield关键字,那么加括号执行函数的时候并不会触发函数体代码的运行
    print('第二')
    yield 'second'
    print('第三')
    yield 'thred'

res = func()  # 生成器初始化:将函数变成迭代器
print(res.__next__())
print(res.__next__())
print(res.__next__())


# range函数就是一个生成器函数
# 用生成器方法实现一个range函数

def my_range(start,end,sep=1):
    while start < end:
        yield start
        start+=sep

for i in my_range(1,20,3):
    print(i)