

class A:

    # 对象在设置属性的时候调用
    def __setattr__(self, key, value):
        print('setattr',key,value)
        self.__dict__[key] = value
        print(self.__dict__)



    def __delattr__(self, item):

        pass


a = A()
a.name = 'aaa'
print(a.name)