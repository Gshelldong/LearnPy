


# 定义一个类
# 类的定义命名通常使用大驼峰的方式命名
class Student():
    school = 'self-study'   #定义一个类的属性

    def __init__(self,name,age):   # 定义初始化属性,初始化属性会在实例化的时候执行类中的__init__方法。
        self.name = name
        self.age = age
        print(self)   # self就是类本身
        print(f'初始化了name')
        print(f'初始化了age')


    def say_hi(self):
        print(f'大家好我叫 {self.name}!')   # 为对象定制行为

    # 类绑定方法
    # cls是类
    # 在调用方法的时候会传入对象本身，在调用类.方法的时候不需要再传参数。
    @classmethod
    def show_school(cls):
        print(cls.school)  # 访问类的属性


a = Student('zhangsan',18)
print(a.school)

print('*'*100)


# 调用对象方法
a.say_hi()


print('-'*100)
# 调用类绑定方法
a.show_school()

# 函数在类中叫做类方法
print(a.show_school)
print('-'*100)


# 另外一种调用方式
z = Student
# 这里要求在对象传入一个obj
Student.__init__(z,'wangwu',44)
