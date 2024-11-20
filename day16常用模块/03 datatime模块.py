import datetime

print(datetime.date.today())  # 打印年月日
print(datetime.datetime.today())  # 年月日和时间

res = datetime.date.today()
print(res.year)
print(res.month)
print(res.day)
print(res.isoweekday())  # 从1开始数的1-7每周
print(res.weekday())     # 从0开始数的0-6每周


"""
(******)
日期对象 = 日期对象 +/- timedelta对象
timedelta对象 = 日期对象 +/- 日期对象
"""
print('='*100)
current_time = datetime.date.today()  # 日期对象
timetel_t = datetime.timedelta(days=7)  # timedelta对象
print('timetel_t:%s'%timetel_t)
res1 = current_time+timetel_t  # 日期对象
print('res1:%s'%res1)

print(current_time-timetel_t)
print(res1-current_time)

print('='*100)


# 小练习 计算今天距离今年过生日还有多少天
start_day = datetime.datetime(2025,1,1,0,0,0)
current_time = datetime.datetime.today()
print(start_day-current_time)

# UTC时间
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow,dt_now,dt_today)