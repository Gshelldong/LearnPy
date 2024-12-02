
import os
import pickle


# 将数据存取操作和主要逻辑分开
class BaseClass():
    def save(self):
        cls_name = self.__class__.__name__
        if not os.path.exists(cls_name):
            os.makedirs(cls_name)
        print(self.name)

        path = os.path.join(cls_name, self.name)
        with open(path, "wb") as f:
            pickle.dump(self, f)


    @classmethod
    def get_obj(cls,name):
        # 拼接路径
        path = os.path.join(cls.__name__,name)
        # 判断路径是否存在
        if os.path.exists(path):
            #读取并返回对象
            with open(path,"rb") as f:
                return pickle.load(f)

class Coder(BaseClass):
    def __init__(self,name,gender,age):
        self.name = name
        self.gender =gender
        self.age = age

    def write_code(self):
        print('正在写代码!')


class Manager(Coder):
    def __init__(self,name,gender,age,bounds):
        super().__init__(name,gender,age)
        self.bounds = bounds

    def manage(self):
        print('管理程序员...')


if __name__ == '__main__':
    m1 = Manager('tom','男',23,10000)  # type:BaseClass
    m1.manage()
    m1.save()




