
"""
两个对象在使用对象继承的关系不太合理的时候，又想把两个功能的关系联系起来。
使用组合的方式把两个对象的功能组合起来。
比如学生和手机对象，学生打电话，这使用继承的关系显然不太合适。
"""

class Phone():
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price


    def call(self):
        print('打电话...')

    def sms(self):
        print('正在发短信!')

class Student():
    def __init__(self,name,male,age,phone):
        self.name = name
        self.male = male
        self.age = age
        self.phone = phone

    def say_hi(self):
        print('你好！')


phone = Phone('SANSUNG','black',5889)

mari = Student('mari','女',18,phone)

mari.phone.call()

