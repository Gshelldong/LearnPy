str = 'string'
l=['a','b','c']
t=('b','gg','mm')
f1 = open('read.txt','w',encoding='utf-8')

res = str.__iter__()

print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
