"""
两个函数
isinstance 判断一个对象是否是指定的对象类型。
issubclass 判断一个类是否是另外一个类的子类。
"""
a = 'words'

# 判断a是否以字符串类型返回布尔值
res = isinstance(a,str)
print(res)

print('-------%s-------'%'分割线')



class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def eat(self):
        print(f'{self.name}是{self.color}颜色,吃食物了.')


class cat(Animal):
    def __int__(self,name,color):
        super().__init__(name,color)

    def zhua(self):
        print('抓老鼠')


mao = cat('huahua','red')
mao.zhua()

# cat 是不是 Animal的子类
res1 = issubclass(cat,Animal)
print(res1)


