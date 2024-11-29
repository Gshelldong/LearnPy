class Student():
    school = 'self-study'   #定义一个类的属性

    def __init__(self,name,age):   # 定义初始化属性,初始化属性会在实例化的时候执行类中的__init__方法。
        self.name = name
        self.age = age
        # print(self)   # self就是类本身
        # print(f'初始化了name')
        # print(f'初始化了age')


    def say_hi(self):
        print(f'大家好我叫 {self.name}!')   # 为对象定制行为


a = Student('tom',14)

print(Student.__dict__)

print(a.__dict__)   # 返回对象初始化时候的参数
print(a.__class__)  # 返回对象的所属的类
print(Student.__name__)   # 返回类的名称