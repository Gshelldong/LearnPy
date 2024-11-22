
import os
import sys

# 这里声明一个环境变量才能找到这个包的位置
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

from m1 import f1
from m2 import *