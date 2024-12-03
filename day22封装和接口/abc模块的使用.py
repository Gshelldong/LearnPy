"""
abc 不是随意取的 而是单词的缩写
abstract class
翻译为抽象类
抽象类的定义 :
类中包含 没有函数体的方法

但是在实际运用中因为代码功能的多样性，不推荐使用这样的方法。
"""
import abc

class AClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self):
        pass
    @abc.abstractmethod
    def run1(self):
        pass


class B(AClass):

    def run(self):
        print("runrunrurn...")

    def run1(self):
        print('运行了run1 run1 run1')

b = B()
b.run()
b.run1()