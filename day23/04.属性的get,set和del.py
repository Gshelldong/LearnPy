

class A:

    # 对象在设置属性的时候调用
    def __setattr__(self, key, value):
        print('setattr',key,value)
        self.__dict__[key] = value
        print(self.__dict__)


    # 在删除属性del()的时候会执行这个
    def __delattr__(self, item):
        print('执行了删除delattr')
        pass

    # 用来获取属性，__getattribute__会先执行，如果没有才会执行getattr
    def __getattr__(self, item):
        print('getattr')
        return 1


    # 这里覆盖了父类中的方法，如果不调用super()会导致常用的方法报错
    def __getattribute__(self, item):
        print('getattribute')
        # return self.__dict__[item]
        return  super().__getattribute__(item)

a = A()
a.name = 'aaa'
del(a.name)
print(a.name)