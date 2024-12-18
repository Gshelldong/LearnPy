
"""
在框架设计中 我们不可能提前知道 框架的用户要提供类相关的信息
"""
import importlib
import abc

# 拿到模块 根据模块的路径
pl = importlib.import_module("libs.plugins")
print(pl)

# 从模块中取出类
cls = getattr(pl,"WinCmd")
print(cls)

# 实例化产生对象
windows = cls()
windows.tasklist()