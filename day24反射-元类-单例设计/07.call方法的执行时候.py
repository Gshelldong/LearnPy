
class MyMeta(type):

    # 元类中的init方法会在对象声明的时候执行元类的init方法。
    def __init__(self,name,bases,dict):
        super().__init__(name,bases,dict)
        print("init run")


    # call方法会在实例化的时候被执行。
    def __call__(self, *args, **kwargs):
        print("元类 call run")
        print(self)
        print(args)
        print(kwargs)
        return super().__call__(*args,**kwargs)

class Dog(metaclass=MyMeta): # ===    Dog = MyMate("Dog",(),{})

    def __init__(self,name,color='red'):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("call run")

d = Dog("大黄",color='red')