
# 1.定义一个基本函数实现一个实例功能
def outter(func):
    def runfc(*args,**kwargs):
        print("执行函数之前的动作！")
        res = func(*args,**kwargs)
        print("执行函数自后的动作！")
        return res
    return runfc



# index = outter(index)
# index()
@outter
def index():    # 这种方式等价于上面的两种调用方式
    print('执行了index函数')

"""
装饰器的两个特点：
    1、不能够改变原来函数的调用方式。
    2、不直接修改原来函数的内容。
在不改变给原来的可调用对象的情况下添加新的功能。
"""