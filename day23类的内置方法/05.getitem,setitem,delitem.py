
class A:
    #  在给对象使用 对象[key] = value赋值的时候回触发
    def __setitem__(self, key, value):
        print('setitem')
        self.__dict__[key] = value
        print(self.__dict__)

    # 使用 对象['key'] 获取值的时候会触发
    def __getitem__(self, item):
        print('__getitem__')
        print(item)
        return self.__dict__

    # 在使用del()方法删除对象的时候会触发
    def __delitem__(self, key):
        print('delitem')
        self.__dict__.pop(key)


a = A()

a['name'] = 'jack'
print(a['name'])
del(a['name'])
