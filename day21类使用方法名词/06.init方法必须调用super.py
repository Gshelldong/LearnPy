'''
为什么要在初始化方法中调用 父类的初始化方法?
子类继承了父类的方法，但是子类的实例化的时候没有执行父类中的init方法导致有的变量没有生成，
那么在子类中调用父类方法的时候就可能会导致报错
'''

class Person:
    def __init__(self,name,gender,age,*args):
        self.name = name
        self.gender = gender
        self.age = age
        self.aa()

    def aa(self):
        print("aa run")

    def say_hi(self):
        print("name:%s ，gender:%s,age:%s" % (self.name,self.gender,self.age))


class Student(Person):

    def __init__(self,name,gender,age,number):
        super().__init__(name,gender,age)
        self.number= number

    def say_hi(self):
        super().say_hi()  # 这里用了覆盖的方法，新增了功能，如果在init方法中没有调用父类的init必然会报错。
        print("numnber:%s" % self.number)

stu = Student("rose","mael",20,"old01")
# stu = Student("old01")
stu.say_hi()