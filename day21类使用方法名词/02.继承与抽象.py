
# 这里的把公共的部分提取处来并写成一个新的类叫做抽象是一个重构的过程
class Persion:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender

class Teacher(Persion):
    def __int__(self):
        super.__init__(self)

    def tech(self):
        print('tech')

class Student(Persion):
    def __init__(self,name,age,gender,id):
        super().__init__(name,age,gender)
        self.id = id

    def say_hi(self):
        print('你好啊!')



s = Student('tom',12,'male',123)
s.say_hi()

t = Teacher('tomas',23,'男')
t.tech()

class Phone:
    def __init__(self,price,color,type):
        self.price = price
        self.color = color
        self.type = type

    def call_num(self):
        print('打电话!')
