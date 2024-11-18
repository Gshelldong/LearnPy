# yield支持外界为其传参
def dog(name):
    print('%s 准备开吃'%name)
    while True:
        food = yield  # 这里没有返回值food就是空值
        print('%s 吃了 %s'%(name,food))


# 当函数内有yield关键字的时候,调用该函数不会执行函数体代码
# 而是将函数变成生成器
g = dog('egon')
g.__next__()  # 必须先将代码运行至yield 才能够为其传值
g.send('狗不理包子')  # 给yield左边的变量传参  触发了__next__方法
g.send('饺子')

"""
yield
    1.帮你提供了一种自定义生成器方式
    2.会帮你将函数的运行状态暂停住
    3.可以返回值

与return之间异同点
    相同点:都可以返回值,并且都可以返回多个
    不同点:
        yield可以返回多次值,而return只能返回一次函数立即结束
        yield还可以接受外部传入的值
"""
