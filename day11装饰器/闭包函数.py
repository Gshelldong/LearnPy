"""
闭包函数
    1.闭:定义在函数内部的函数
    2.包:内部函数引用了外部函数作用域的名字

"""


def outter():
    x = 111
    def inner():
        print(x)
    return inner
res = outter()  # res就是inner函数内存地址

def func():
    x = 333
    res()
func()

# 就是在函数外给函数传递参数还是在函数内传递参数，闭包就是在函数内定义的变量传递给函数。