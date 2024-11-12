# 函数名可以被传递

def a():
    print('func a')

b = a
# b()

# 函数可以被当作参数传递给其它函数
def c():
    print('func c')

def d(fc):
    fc()

# d(c)

# 函数名可以当作函数的返回值
def funca():
    print('func a')
    return 'funca'

def funcb():
    return funca

res_func = funcb()
print(res_func)
a = res_func()
print(a)

# 一个循环菜单功能

def light():
    print('调节亮度...')

def voice():
    print('调节音量')

def menu():
    print('打印菜单')

def ex():
    print('退出')

content = {
    '1': light,
    '2': voice,
    '3': menu,
    '4': ex
}

while True:
     res_in  = input('请输入功能1-4: ').strip()
     if res_in in content:
         content[res_in]()
     else:
         exit(3)

