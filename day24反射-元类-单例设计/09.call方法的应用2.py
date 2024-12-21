
"""
要求创建对象时必须以关键字参数形式来传参
覆盖元类的__call__
判断你有没有传非关键字参数 == 不能有位置参数
有就炸
"""

class MyType(type):
    def __call__(self, *args, **kwargs):
        if args:
            raise Exception('禁止使用位置参数传参.')
        return super().__call__(*args,**kwargs)  # 注意这里必须把对象返回，不然就是空的

    # def __call__(self, *args, **kwargs):
    #     obj = object.__new__(self) # 创建一个空对象
    #     self.__init__(obj,*args,**kwargs) # 让对象去初始化
    #     return obj


class Persion(metaclass=MyType):
    def __init__(self,name):
        self.name = name

p = Persion(name='hahah')
print(p.name)
