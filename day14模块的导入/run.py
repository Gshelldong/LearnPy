

"""
当被导入文件中声明了__all__的时候
使用from xxx import * 的时候只会
导入__all__包含的函数。

"""
from md1 import *

func1()
func3()   # 因为没有在__all__中调用直接报错