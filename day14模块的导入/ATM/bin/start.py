"""
1.实现一个简单的商城功能。
用户登陆记录用的状态
用户在必要操作的时候检测用户状态
如果没有登陆需要用户进行登陆操作
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)
sys.path.append(BASE_DIR)

"""
pycharm会自动将新建的最顶层的目录自动添加到环境变量中。
设置代码运行目录的basedir是针对用户，因为你不知道用户要把整个软件放在哪里运行。
"""

# 文件在导入只会在当前目录开始去找包然后再去导，直接在当前目录下找core
# 是肯定找不到的，所以需要告诉这里的执行文件把项目路径加入到环境变量中
# 这样就可以直接找到项目所在的分级代码目录。
from core import src


if __name__ == '__main__':
    src.run()