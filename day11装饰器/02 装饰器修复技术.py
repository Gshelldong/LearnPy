"""
装饰器把函数装饰了之后，原函数不管是内存地址还是函数说明信息都被
修改成了装饰器的说明信息。通过装饰器修复保证通过help()和函数内存
地址都是原始函数的信息。
"""
import time
from functools import wraps


def outter(func):
    @wraps(func)
    def inner(*args,**kwargs):
        """
        这是一个装饰器内部实现的功能
        :param args: 传入任意位置参数
        :param kwargs: 传入任意关键字参数
        :return: 返回函数执行的结果
        """
        print("执行函数之前。")
        res = func(*args,**kwargs)
        print("执行函数之后。")
        return res
    return inner


@outter
def index():
    """
    这是index函数，打印index
    :return: index
    """
    time.sleep(3)
    print('index')
    return 'index'

# index()
"""

print(help(index))
print(index)
# ------在被修复之前的结果--------
Help on function inner in module __main__:

inner(*args, **kwargs)
    这是一个装饰器内部实现的功能
    :param args: 传入任意位置参数
    :param kwargs: 传入任意关键字参数
    :return: 返回函数执行的结果

None
<function outter.<locals>.inner at 0x0000028B6FAC8FE0>
"""

print(help(index))
print(index)

'''
修复之后的结果
Help on function index in module __main__:

index()
    这是index函数，打印index
    :return: index

None
<function index at 0x000001EB95318FE0>
'''