# 递归函数不要考虑循环的次数 只需要把握结束的条件即可
# 循环遍历
l = [1,[2,[3,[4,[5,[6,[7,[8,[9,[10,[11,[12,[13,]]]]]]]]]]]]]

def get_num(l):
    for i in l:
        if type(i) is int:
            print(i)
        else:
            get_num(i)

get_num(l)