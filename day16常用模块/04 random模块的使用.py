import random  # 随机模块random
"""
 常用的三种使用方法：
 1.生成随机数。
 2.生成0-1之间的小数。
 3.从列表中随机取一个数字。
 4.洗牌。
"""

# 随机取1-6的整数
print(random.randint(1, 6))

# 生成0-1之间的小数
print(random.random())

# 选择列表中随机的一个元素
print(random.choice(['a', 'c', 'd', 'b']))

# 洗牌
l = [1,2,3,4,5,6,6]
random.shuffle(l)
print(l)


# 一个随机的五位数验证码生成器
code = ''
for i in range(5):
    num = str(random.randint(0,9))
    upper_case = chr(random.randint(65,90))
    lower_case = chr(random.randint(97,122))
    code += random.choice([num,upper_case,lower_case])
print(code)