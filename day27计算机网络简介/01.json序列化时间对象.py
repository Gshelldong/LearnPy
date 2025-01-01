
"""
json 在序列化的时候 JSONEncoder不会对执定类型以外的对象进行序列化，
如果要增加自定义的对象类型可以修改序列化类的父类。
"""

import json