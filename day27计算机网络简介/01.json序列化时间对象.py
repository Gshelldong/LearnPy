
"""
json 在序列化的时候 JSONEncoder不会对执定类型以外的对象进行序列化，
如果要增加自定义的对象类型可以修改序列化类的父类。
"""

import json
from datetime import datetime,date

# 返回日期 时分秒
# print(datetime.today())

# 返回日期
# print(date.today())

data = {
    'c1': datetime.today(),
    'c2': date.today()
}

# res = json.dumps(data)   # TypeError: Object of type datetime is not JSON serializable
# print(res)

class MyJson(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,datetime):
            return o.strftime('%Y-%m-%d %X')
        elif isinstance(o,date):
            return o.strftime('%Y-%m-%d')
        else:
            return super().default(self,o)

'''
这里通过修改父类中的实现来达到目的比较高级的用法，
普通的方式把日期通过str()转换为字符串也可达到相同的效果
'''
res = json.dumps(data,cls=MyJson)
print(res)  # {"c1": "2025-01-02 17:00:57", "c2": "2025-01-02"}