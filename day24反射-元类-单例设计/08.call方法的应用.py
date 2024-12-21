


# 1.把对象的所有属性变成大写

class MyType(type):
    def __call__(self, *args, **kwargs):
        """
        这里的for拿到了在实例化的时候传入的每个参数args，
        然后循环遍历，修改为大写之后，放入new_args列表
        最后调用父类中的call方法传入修改过后的args,这样
        就实现了控制对象参数的功能。
        :param args:
        :param kwargs:
        :return:
        """
        new_args = []
        for a in args:
            new_args.append(a.upper())

        print(new_args)
        print(kwargs)
        return super().__call__(*new_args,**kwargs)

class Persion(metaclass=MyType):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

p = Persion('wanghahah','man')
print(p.name)
print(p.gender)