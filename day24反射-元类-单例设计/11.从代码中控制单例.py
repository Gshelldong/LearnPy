# 单例n元类
class Single(type):
    def __call__(self, *args, **kwargs):
        print(self)
        if hasattr(self,"obj"): #判断是否存在已经有的对象
            return getattr(self,"obj") # 有就返回

        obj = super().__call__(*args,**kwargs) # 没有则创建
        print("new 了")
        print(args)
        self.obj = obj # 并存入类中
        return obj


class Student(metaclass=Single):
    def __init__(self,name):
        self.name = name

class Person(metaclass=Single):
    pass

Student('w')
Student('ttom')
Student('jerry')

