
# 静态绑定方法
# 就是即不需访问类的数据,也不需要访问对象的数据
# 语法:@staticmethod

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

    @staticmethod
    def pt_info():  # 如果不绑定静态方法会直接报错
        print('打印一个info函数.')

car = Student('tomas',12)
car.pt_info()
