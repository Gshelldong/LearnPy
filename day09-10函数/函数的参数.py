def func(x,y):
    """
    这个函数是输入x,y然后返回它们两个整数的值。
    :param x: 整数
    :param y: 整数
    :return: x+y
    """
    return x + y

z= func(1,2)
print(z)

# 注意函数使用的顺序
# 所有参数可任意组合使用，但定义顺序必须是：位置参数、默认参数、*args 、**kwargs
def func(x,y=1,*args,z=3,m,**kwargs):
    print(x,y)
    print(args)
    print(z,m)
    print(kwargs)
func(1,2,1,2,3,4,5,6,7,78,8,9,0,z=69,m=999,o=666999,l = 999666)