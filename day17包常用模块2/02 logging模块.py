# logging模块记录程序运行产生的日志

#配置一个基础日志记录器
import logging

"""
logging.basicConfig(filename='access.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=30,
                    )

# 日志的五个等级
logging.debug('debug日志')  # 10
logging.info('info日志')  # 20
logging.warning('warning日志')  # 30
logging.error('error日志')  # 40
logging.critical('critical日志')  # 50

会出现的问题
1.乱码
2.日志格式
3.如何既打印到终端又写到文件中
"""

# 第二种方式，实例化一个logger对象
'''
1.logger对象负责产生日志
2.filter过滤日志
3.hander对象控制日志硕儒位置
4.formmater对象规定呢日志内容格式
'''


# 1.logger对象:负责产生日志
logger = logging.getLogger('转账记录')
# 2.filter对象:过滤日志(了解)

# 3.handler对象:控制日志输出的位置(文件/终端)
hd1 = logging.FileHandler('a1.log',encoding='utf-8')  # 输出到文件中
hd2 = logging.FileHandler('a2.log',encoding='utf-8')  # 输出到文件中
hd3 = logging.StreamHandler()  # 输出到终端

# 4.formmater对象:规定日志内容的格式
fm1 = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p',
)

fm2 = logging.Formatter(
        fmt='%(asctime)s - %(name)s:  %(message)s',
        datefmt='%Y-%m-%d',
)

# 5.给logger对象绑定handler对象
logger.addHandler(hd1)
logger.addHandler(hd2)
logger.addHandler(hd3)

# 6.给handler绑定formmate对象
hd1.setFormatter(fm1)
hd2.setFormatter(fm2)
hd3.setFormatter(fm1)

# 7.设置日志等级
logger.setLevel(10)

# 8.记录日志
logger.debug('写了半天 好累啊 好热啊 好想释放')

# 日志的配置字典
