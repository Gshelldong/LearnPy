import os


# 这里设置了log目录的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 不要手动拼接路径
LOG_PATH = os.path.join(BASE_DIR,'log')