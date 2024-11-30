class Persion:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hi(self):
        print('hello word!')


class Student(Persion):
    def say_hi(self):
        print('student say hello!')  # 这里把父类中的say_hi方法覆盖了。

    def learnning(self):   # 比父类中更多的方法叫做派生
        print('student learnning')


s = Student('tom',23,'男')
s.say_hi()

s.learnning()

