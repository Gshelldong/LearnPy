import sys

class Persion:

    # 优化内存的，指定要初始化多少参数
    # __slots__ = ['name','age','hight']
    def __init__(self,name,age,hight):
        self.name = name
        self.age = age
        self.hight=hight
        # print(self.__dict__)

    # 对象被直接调用的时候会执行这个函数
    def __call__(self, *args, **kwargs):
        print(f'执行了call方法,参数的内容是{args},{kwargs}')

    # 在对象传入str()函数的时候会执行这个
    def __str__(self):
        strf = '我是｛｝,我的年龄是｛｝'.format(self.name,self.age)
        print(strf)
        return strf

    # 对象指向完要释放的时候会执行这个
    def __del__(self):
        print('执行了__del__')


john = Persion('john',23,168)
john('aa',x= 22)
str(john)
print(sys.getsizeof(john))


print()
"""
del的使用案例
简化文件的读写操作.
"""

class ReadFile:
    def __init__(self,path):
        self.file = open(path,mode='rt',encoding='utf-8')

    def read(self):
        return self.file.read()

    def __del__(self):
        print('自动关闭文件')
        self.file.close()

file_a = ReadFile('a.txt')
print(file_a.read())

# slots的使用，声明类中的函数，减少变量占用的空间。




