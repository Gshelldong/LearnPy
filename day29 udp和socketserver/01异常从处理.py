"""
异常处理
1、用处当代码中存在不确定的因素让代码报错，但是又不想影响代码继续运行，所以使用异常处理。
2、使用的场景，比如网络连接异常如果不进行异常处理就会导致程序崩溃

"""

# res = {'name':''}
# print(res['password'])
# print(res.get('password','fdjdsfk'))

# int('sdjajsd')
# l = [1,2,3,4]
# # l[111]



# try:
#     name
#     l = [1,2,3]
#     l[111]
#     d = {'name':'jason'}
#     d['password']
# except NameError:
#     print('NameError')
# except IndexError:
#     print('indexerror')
# except KeyError:
#     print('keyerror')
"""
错误发生之后  会立刻停止代码的运行
执行except语句 比对错误类型
"""

try:
    # name
    l = [1,2,3]
    l[111]
    d = {'name':'jason'}
    d['password']
    # Exception
except BaseException:  # 万能异常  所有的异常类型都被捕获
    print('老子天下无敌')





# try:
#     # name
#     l = [1,2,3]
#     l[111]
#     # d = {'name':'jason'}
#     # d['password']
# except Exception:  # 万能异常  所有的异常类型都被捕获
#     print('老子天下无敌')
# else:
#     print('被检测的代码没有任何的异常发生 才会走else')
# finally:
#     print('无论被检测的代码有没有异常发生 都会在代码运行完毕之后执行我')


# 主动抛异常
# if 'egon' == 'DSB':
#     pass
# else:
#     raise TypeError('尽说大实话')
# 关键字raise就是主动抛出异常


# l = [1,2,3]
# assert len(l) < 0  # 断言  预言
# 猜某个数据的状态 猜对了 不影响代码执行 正常走
# 猜错了  直接报错

# 自定义异常
#9 自定义异常
# class MyError(BaseException):
#      def __init__(self,msg):
#          super().__init__()
#          self.msg=msg
#      def __str__(self):
#          return '<dfsdf%ssdfsdaf>' %self.msg
#
# raise MyError('我自己定义的异常')  # 主动抛出异常其实就是将异常类的对象打印出来,会走__str__方法
#












