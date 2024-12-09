
class A():
    def __init__(self,name,key):
        self.__name = name
        self.__key = key

    # 获取私有方法
    @property
    def key(self):
        return self.__key

    # 修改私有方法
    @key.setter
    def key(self,new_key):
        if new_key <=100:
            self.__key = new_key
        else:
            print('不允许设置大于100的值')

    # 控制删除对象属性的时候回触发
    @key.deleter
    def key(self):  # del(a.key)
        print('触发了删除')


a = A('tom',100)
a.key=99
print(a.key)

a.name = 'xx'
print(a.name)

print(a.key)

del(a.key)