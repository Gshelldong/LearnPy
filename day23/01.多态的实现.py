"""
要管理 鸡 鸭 鹅
如何能够最方便的 管理,就是我说同一句话,他们都能理解
他们拥有相同的方法

"""

class Chiken():
    def bark(self):
        print('咯咯咯')

    def layeggs(self):
        print('生鸡蛋')

class Duck():
    def bark(self):
        print('嘎嘎嘎')


    def layeggs(self):
        print('生鸭蛋')

class Goose():
    def bark(self):
        print('鹅鹅鹅鹅')

    def layeggs(self):
        print('下鹅蛋')


ji = Chiken()
ya = Duck()
e = Goose()

def manage_layges(obj):
    obj.layeggs()

# 管理不同的对象下蛋
manage_layges(ji)
manage_layges(ya)
manage_layges(e)


