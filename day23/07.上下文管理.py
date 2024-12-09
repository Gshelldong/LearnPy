
"""
在python中变量会被解释器直接释放掉，但是解释器之外的比如文件的操作
解释器就无法去操作，这个时候就需要进行对文件管理
"""

class MyOpen:
    def __init__(self,path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path)
        print('enter....')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit....')
        print(exc_tb,exc_val,exc_type)
        self.file.close()
        return True

with MyOpen('a.txt') as f:
    # print(f.file.read())
    print(f.read())

# 因为已经被关闭了，所以无法再读取
f.file.read()