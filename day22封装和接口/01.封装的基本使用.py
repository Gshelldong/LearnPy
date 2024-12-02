
class Persion():
    def __init__(self,name,age,id,gender):
        self.name = name
        self.age = age
        self.__id = id
        self.gender = gender


    def see_id(self):
        print('身份id: %s'%self.__id)


p  = Persion('john',32,1122334,'male')

# print(p.__id)   # 私有方法无法在外部直接访问.
p.see_id()