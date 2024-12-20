

"""
new 方法和实例没有太大的关系，主要是在创建类的时候会先执行元类中的new方法,
再执行init方法,同样的道理可以在new方法中控制类的创建。

"""

class Meta(type):
    def __new__(cls, *args, **kwargs):
        print(cls) # 元类自己
        print(args) # 创建类需要的几个参数  类名,基类,名称空间
        if not args[0].istitle():
            raise Exception('类名称请大写.')
        print(kwargs) #空的
        print("new run")
        # return super().__new__(cls,*args,**kwargs)
        obj = type.__new__(cls,*args,**kwargs)
        return obj

    def __init__(self,a,b,c):
        super().__init__(a,b,c)
        print("init run")


class Persion(metaclass=Meta):
    def __init__(self,name):
        self.name = name


# p = Persion('john')

