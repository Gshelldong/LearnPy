

class Persion:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


p  = Persion('john', 23, 'man')


# 判断是否有某个属性，返回布尔值
print(hasattr(p, 'name'))

# 给对象添加新的属性
setattr(p,'id','123')
print(p.id)
print(p.__dict__)

# 删除对象的属性
delattr(p,'id')
print(p.__dict__)  # id 被删除了 {'name': 'john', 'age': 23, 'gender': 'man'}

# 获取对象属性，如果没有这个属性可以定义返回值
print(getattr(p, 'id', '1222222'))