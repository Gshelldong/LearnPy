
class Persion(object):
    name = 'wanghahah'
    pass

p = Persion()
print(type(p))         # p 类是Persion
print(type(Persion))   # Persion的类是type


class Student:
    pass

print(type(Student))   #  返回<class 'type'>

# 直接调用type类来产生类对象
"""
# 一个类的三个基本组成部分
# 1.类的名字(字符类型)  
2.类的父类们  (是一个元组或列表)  
3.类的名称空间(字典类型)
"""

dog = type("Dog",(),{})  # 这种方式等同于使用class声明
print(dog)

class Person:
    pass