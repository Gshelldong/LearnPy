'''
必会的三种方法
findall
search
match
'''

import re

# 第一种方法findall把正则匹配到的内容用列表返回回来
# t = 'tom和jerry是猫和老鼠中的人物，tomas是小火车.'
# res = re.findall('[a-z]+',t)
# print(res)


# search 返回一个对象，使用group查看，匹配到第一个就会返回，没有匹配结果返回None.
# 返回None的时候没有 group方法就会报错。
# t = 'tom和jerry是猫和老鼠中的人物，tomas是小火车.'
# t1 = '测试文本.'
# res = re.search('[a-z]+',t1)
# print(res.group())

# math会匹配字符串的开头，然后返回一个对象，没有会返回None。
# 匹配字段是how的时候就正确。
# 匹配字段是are的时候就报错。
# t = 'how are you!'
# res = re.match('are',t)
# print(res.group())


# split根据匹配的内容分割文本，并返回一个列表。
# x = 'tom|25|zoom|source'
# res = re.split('zoom',x)   # -> ['tom|25|', '|source']  按照zoom为分隔符分割了两部分。
# print(res)


# sub 可以对匹配的内容进行批量替换。
# 最后一个参数是具体要替换几个字符，默认是0全部替换。
# res = re.sub('a','A','appleline application authiontication',0)
# print(res)

# l = ['apple','application','authontication','alpeline','alpha']
#
#
# res = map(lambda x:re.sub('a','A',x),l)
# print(list(res)) # -> ['Apple', 'ApplicAtion', 'AuthonticAtion', 'Alpeline', 'AlphA']

# 把正则匹配到的内容替换成自定义的内容，返回替换的结果和替换次数的有元祖。
# res = re.subn('a','A','aaaaaa',3)
# print(res)  # -> ('AAAaaa', 3)

# 将正则表达式编译成一个正则对象。
# reobj = re.compile('\d{3}') # 这里是匹配三个数字
#
# res = reobj.search('123456789111')
# res1 = reobj.findall('1235436')
#
# print(res.group())
# print(res1)


# finditer 返回一个存放匹配结果的迭代器, \d 匹配数字
'''
ret = re.finditer('\d','abc1ll3l4l1lll3')
print(ret.__next__().group())
print(ret.__next__().group())
print(ret.__next__().group())
print(ret.__next__().group())
print(ret.__next__().group())
'''

# 给正则表达式取别名
res = re.search('^[1-9](\d{14})(\d{2}[0-9x])?$','110105199812067023')

# ?P<password> 这个是给正则取一个别名在group('password')中获取。
res = re.search('^[1-9](?P<password>\d{14})(?P<username>\d{2}[0-9x])?$','110105199812067023')
print(res.group())
print(res.group('password'))
print(res.group(1))
print(res.group('username'))
print(res.group(2))
# print(res.group(2))
# print(res.group(1))
