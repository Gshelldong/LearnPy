

class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def arrest(self,other_Animal):
        print(f'{self.name}抓住了{other_Animal.name}')



"""
这里主要是用了类的两种调用方式，实际得到的结果是一样的。
"""

tom = Animal('tom',10)
jerry = Animal('jerry',9)
Animal.arrest(tom,jerry)



tom.arrest(jerry)