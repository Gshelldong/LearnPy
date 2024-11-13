
# 判断一个列表中的特定元素如果符合条件就会新加的新的列表中。

l1 = ["tom_sb","jerry_sb","mary_sb","tomas",'zippe','band_sb']

l2 = [name for name in l1 if name.endswith("_sb")]  # 后面不支持加else的情况

print(l1)
print(l2)

# 先for循环依次取出列表里面的每一个元素
# 然后交由if判断  条件成立才会交给for前面的代码
# 如果条件不成立 当前的元素 直接舍弃