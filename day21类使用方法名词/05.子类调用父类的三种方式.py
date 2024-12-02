
class BaseClass():
    money = '2233'

    def say_hi(self):
        print('hello word!')


class A(BaseClass):

    def show_info(self):
        print('第一种方式.')
        print(super(A, self).money)
        super(A, self).say_hi()
        print('第二种方式,直接使用super()方法不传参.')
        # 大多数使用这种方式，方便简单
        print(super().money)
        super().say_hi()

        print('第三种方式使用单独的类传参，这种方式和继承就没有太大关系了。')
        print(BaseClass.money)
        # 这里传的self是A类
        BaseClass.say_hi(self)





a = A()
a.show_info()
