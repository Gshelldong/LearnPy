"""
只要继承了type 那么这个类就变成了一个元类

当创建的类，类名称不是大写的开头的时候抛出异常
"""

class MyType(type):
    def __init__(self,clss_name, bases,dict):
        super().__init__(clss_name,bases,dict)
        print(clss_name,bases,dict)   # 调用打印的结果 Pig () {'__module__': '__main__', '__qualname__': 'Pig'}
        if not clss_name.istitle():
            raise Exception('类名首字母必须大写.')


class Pig(metaclass=MyType):
    pass


