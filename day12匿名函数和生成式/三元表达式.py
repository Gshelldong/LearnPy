'''
三元表达式固定表达式
    值1 if 条件 else 值2
        条件成立 值1
        条件不成立 值2
'''

# 三元表达式的应用场景只推荐只有两种的情况的可能

get_input = input('please input a passwd: ')

res_pass = '正确' if get_input == "1234" else "错误"

print(res_pass)