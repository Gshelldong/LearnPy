
"""
修改正方形的变长，求正方形的面积

"""

class Square():
    def __init__(self,boder):
        self.boder = boder

    def area(self):
        return self.boder * self.boder


a = Square(4)
print(a.area())

a.boder = 5
print(a.area())