import random
import time


class Hero:

    def __init__(self,name,level,blood,att,q_hurt,w_hurt,e_hurt):
        # 简便写法
        lcs = locals()
        print(lcs)
        lcs.pop("self")
        self.__dict__.update(lcs)

    def attack(self,enemy):
        enemy.blood -= self.att
        print("%s对%s释放了普通攻击 造成了%s的伤害 敌人剩余血量%s" % (self.name, enemy.name, self.att, enemy.blood))
        if enemy.blood <= 0:
            print("%s被%s使用普通攻击击杀了" % (enemy.name,self.name))


    def Q(self,enemy):
        enemy.blood -= self.q_hurt
        print("%s对%s释放了Q 造成了%s的伤害 敌人剩余血量%s" % (self.name, enemy.name, self.q_hurt, enemy.blood))
        if enemy.blood <= 0:
            print("%s被%s使用Q技能击杀了" % (enemy.name, self.name))

    def W(self,enemy):
        enemy.blood -= self.w_hurt
        print("%s对%s释放了W 造成了%s的伤害 敌人剩余血量%s" % (self.name, enemy.name, self.w_hurt, enemy.blood))
        if enemy.blood <= 0:
            print("%s被%s使用W技能击杀了" % (enemy.name, self.name))

    def E(self,enemy):
        enemy.blood -= self.e_hurt
        print("%s对%s释放了E 造成了%s的伤害 敌人剩余血量%s" % (self.name,enemy.name,self.e_hurt,enemy.blood))

        if enemy.blood <= 0:
            print("%s被%s使用E技能击杀了" % (enemy.name, self.name))


h1 = Hero("亚索",20,2000,100,600,0,1000)
h2 = Hero("妲己",20,2000,100,600,500,1000)
h3 = Hero("鲁班",20,1500,700,100,200,300)
h4 = Hero("蔡文姬",20,2000,10,0,0,10)


# h1.attack(h2)
# h2.Q(h1)
# h2.E(h1)
# h2.W(h1)

#从字典中随机拿出一个值

def  random_hero(heros):
    hero_index = random.randint(1, len(heros))
    return heros[hero_index]


while True:
    # # 把所有的攻击方法装到字典里  为了随机取出一个
    funcs = {1: Hero.Q, 2: Hero.W, 3: Hero.E, 4: Hero.attack}
    func_index = random.randint(1, 4)
    func = funcs[func_index]


    # 把所有的英雄方法装到字典里  为了随机取出一个
    heros = {1: h1, 2: h2, 3: h3, 4: h4}
    hero = random_hero(heros)

    # 剩余的英雄们
    other_heros = {}
    new_index = 1
    for k, v in heros.items():
        if v != hero:
            other_heros[new_index] = v
            new_index += 1

    # 从剩余的英雄中随机挑出一个英雄来挨打
    enemy = random_hero(other_heros)
    # 打他
    func(hero, enemy)
    if enemy.blood <= 0:
        break
    time.sleep(0.5)






