import random
import time

class Animal():
    """
    name, 名字
    level, 等级
    lag, 腿攻击
    bite, 咬攻击
    grab, 抓攻击
    attack 普通攻击
    blood, 血量
    """
    def __init__(self,name,level,lag,bite,grab,attack,blood=20):
        lcs = locals()
        lcs.pop('self')
        self.__dict__.update(lcs)
        print(lcs)

    def lag_attack(self,endure):
        endure.blood -= self.lag
        print('%s被%s使用腿攻击了,血量减少了%s.'%(endure.name,self.name,self.lag))
        if endure.blood <= 0:
            print('%s被%s杀了.'%(endure.name,self.name))

    def bite_attack(self,endure):
        endure.blood -= self.bite
        print('%s被%s使用咬攻击了,血量减少了%s.'%(endure.name,self.name,self.bite))
        if endure.blood <= 0:
            print('%s被%s杀了.'%(endure.name,self.name))

    def grab_attack(self,endure):
        endure.blood -= self.grab
        print('%s被%s使用抓攻击了,血量减少了%s.'%(endure.name,self.name,self.grab))
        if endure.blood <= 0:
            print('%s被%s杀了.'%(endure.name,self.name))

    def attack(self,endure):
        endure.blood -= self.attack
        print('%s被%s使用普通攻击,血量减少了%s.'%(endure.name,self.name,self.attack))
        if endure.blood <= 0:
            print('%s被%s杀了.'%(endure.name,self.name))

    def say_hi(self):
        print('我是%s'%self.name)


def select_animal(animal_dic):
    num = random.randint(1,len(animal_dic))
    animal = animal_dic[num]
    return animal

cat = Animal('tom','9',8,9,10,5)
dog = Animal('spike','8',7,10,5,5)
mouse = Animal('jerry','7',3,7,3,2)
beard = Animal('zooper','6',5,8,8,6)


# 核心代码就是这个，让谁去攻击谁
# cat.lag_attack(dog)

# Animal.lag_attack(cat,dog)


"""
实现的思路是先随机选择一个动物然后再从剩下的动物中生成一个新的挨揍的动的字典，在随机选择一个挨揍的动物，如此循环
知道被挨动物的血量为0的时候游戏就停了。
"""

attack_type_dic = {1: Animal.attack, 2: Animal.lag_attack, 3: Animal.grab_attack, 4: Animal.bite_attack}

while True:
    animal_dic = {1:cat,2:dog,3:mouse,4:beard}
    # 先随机选出一个动物
    attack_animal = select_animal(animal_dic)

    # 生成挨揍动物的字典并随机选择一个动物
    endure_animal_dic = {}
    endure_animal_index = 1
    for k,v in animal_dic.items():
        if v != attack_animal:
            endure_animal_dic[endure_animal_index] = v
            endure_animal_index +=1
    endure_animal = select_animal(endure_animal_dic)

    # 随机的攻击方式
    attack_type = attack_type_dic[random.randint(1,4)]


    attack_type(attack_animal,endure_animal)
    if endure_animal.blood <= 0:
        break






