

__all__ = ["func1"]  # 默认情况下是全部的函数名

num = '123'
def func1():
    print('这是函数1')

def func2():
    print('这是函数2')

def func3():
    print('这是函数3')


if __name__ == '__main__':  # 这种方式只有在当前命名空间执行才会执行
    func1()
    func2()
    func3()