
"""
迭代器
有iter和next方法的对象。
当next拿完了的时候抛出一个StopIteration错误
"""

class MyItter:
    def __init__(self,num):
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    # next方法会不断的返回一个值，如果是for的方式取值就会导致死循环
    # 需要用条件去控制next方法的结束
    def __next__(self):
        self.count +=1
        if self.count <= self.num:
            return f'哈哈哈 +{self.count}'
        else:
            raise StopIteration

x = MyItter(10)
for i in x:
    print(i)

# 实现一个自定义的range


class MyRange:
    def __init__(self,start,end,sep=1):
        self.start = start
        self.end = end
        self.sep = sep

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.sep
        co = self.start - self.sep
        if co < self.end:
            return self.start
        else:
            raise StopIteration


myrange = MyRange(1,10,sep=2)
for num in myrange:
    print(num)



