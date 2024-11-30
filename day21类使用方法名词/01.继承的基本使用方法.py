

class Base:
    money = 12

    def say_hi(self):
        print('hello word!')

class SubCls(Base):
    pass

a = SubCls()
a.say_hi()
