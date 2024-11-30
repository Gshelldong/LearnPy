

class MyList(list):
    def __init__(self,set_type):
        super().__init__()  # 调用父类的初始化方法，更好的继承
        self.set_type = set_type

    def append(self, object):
        if type(object) == self.set_type:
            super(MyList,self).append(object)   # 调用父类中的方法
        else:
            print('你添加的元素不是%s类型.'%self.set_type)


l =MyList(int)
l.append(1)
print(l)