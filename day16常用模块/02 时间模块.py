# time
"""
三种表现形式
1.时间戳
2.格式化时间
3.结构化时间
"""
import time

# 打印时间戳
print(time.time())

# 打印格式化时间
t = time.strftime("%Y-%m-%d %H:%M:%S")
print(t)
print(time.strftime('%X'))    # X等价于时分秒
"""
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
"""


# 打印本地时间
print(time.localtime())   # 这是一个struct_time

local_time = time.localtime()   # 这个是struct_time time.struct_time(tm_year=2024, tm_mon=11, tm_mday=20, tm_hour=11, tm_min=25, tm_sec=47, tm_wday=2, tm_yday=325, tm_isdst=0)

# localtime 格式化
f_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
print(f_time)

# 格式化时间要告诉straptime传进来的是什么格式
print(time.strptime(f_time,'%Y-%m-%d %H:%M:%S'))  # 转换成struct_time 要在格式化的基础上


print(time.mktime(local_time))    # struct_time可以直接被转换成时间戳


