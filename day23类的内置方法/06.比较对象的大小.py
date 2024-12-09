"""
1.在比较对象时候，的内部实现方法。
__gt__
__ge__
__lt__
__le__
这个文档可以参考int对象的实现.
"""

class Student:
    def __init__(self,name,age,hight,source):
        self.name = name
        self.age = age
        self.hight = hight
        self.source = source

    # other传入的另外一个对象
    # 比较大小返回的是布尔值
    # 下面的方法会自动的实现大于小于符号的反转
    # 使用相同的方法可以实现gt ge le eq等方法
    def __lt__(self, other):
        if self.source < other.source:
            return True
        return False


a = Student('a',23,145,88)
b = Student('b',45,190,90)

print(a<b)
print(a>b)








