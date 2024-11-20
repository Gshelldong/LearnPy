"""
具名元祖
1.就是有名字的元祖
2.应用场景，坐标、扑克牌，地理位置

"""

# 表示一个坐标
from collections import namedtuple

d = namedtuple('坐标',('x','y'))  # 这里还可以传入z，只要是可迭代对象就行。
nd = d(1,2)
print(nd)
print(nd.x)
print(nd.y)

print('='*100)
# 表示一张扑克牌
card = namedtuple('扑克',('flower','colour'))
card1 = card('♥','red')
print(card1)
print(card1.flower)
print(card1.colour)

print('='*100)
# 表示一个城市的信息
city = namedtuple('城市','city_name people price')
city1 = city('上海','多','贵')
print(city1)
print(city1.people)
print(city1.city_name)
print(city1.price)

print('='*100)

# 队列
# 特点先进先出
# 当队列中没有值的时候会等待知道取到才会结束
import queue

q = queue.Queue()
q.put('a')  # 放
q.put('b')
q.put('c')

print(q.get()) # 取
print(q.get())
print(q.get())
# q.get()

print('='*100)

# 双端队列
# 两边都能够进和出
# 使用insert方法可以插队
"""
pop()
popleft()
"""
from collections import deque

dq = deque('abc')
dq.append('a')  # a先进入
dq.appendleft('b')
print(dq.popleft())  # 这里从同一个方向去取就先把b取出来了

print('='*100)

# 有序字典，字典默认是无序的
from collections import OrderedDict

od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
print(od['a'])
print(od['b'])
print(od['c'])

print('='*100)

# 默认字典
# 一个小应用把一个列表中的符合条件的组合成字典
# {'k1':(,1,23),'k2‘:(3,4,5)}的格式

from collections import defaultdict

values = [11, 22, 33,44,55,66,77,88,99,90]

my_dict = defaultdict(list)  # 后续该字典中新建的key对应的value默认就是列表
print(my_dict['aaa'])  # 这里相当于就是传入的一个key
for value in  values:
    if value>66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)
print(my_dict)


d1 = defaultdict(tuple)
d1['aaa']=(1,2,3,4)
d1['bbb']=2
print(d1)

print('='*100)

# 统计一个列表中重复的个数
l = ['a','a','c','b','c','app']
from collections import Counter

res = Counter(l)
print(res)