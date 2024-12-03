class A:
    def __init__(self,key):
        self.__key = key

    @property
    def key(self):
        return self.__key

    @key.deleter
    def key(self):
        del self.__key


a = A("123")
print(a.key)
print(a.__dict__)

print(a._A__key)

a.__name = 1

print(a.__dict__)

"""
就是把原来的__变量，替换成了_类__变量
"""
print("__key".replace("__","_A__"))