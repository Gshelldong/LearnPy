
"""
接口
接口就是定义一个类，继承的类要按照类的方法去写或者对功能的扩展，
大家都按照类中统一的方法进行写和扩展就能够，提高代码的可用和扩展性

比如大家都遵循usb的规范，那么只要是符合这个规范的设备都可以正常使用
"""

class Mouse:
    def open(self):
        print("鼠标开机.....")

    def close(self):
        print("鼠标关机了...")

    def read(self):
        print("获取了光标位置....")

    def write(self):
        print("鼠标不支持写入....")



def pc(usb_device):
    usb_device.open()
    usb_device.read()
    usb_device.write()
    usb_device.close()

m = Mouse()
# 将鼠标传给电脑
pc(m)

class KeyBoard:
    def open(self):
        print("键盘开机.....")

    def close(self):
        print("键盘关机了...")

    def read(self):
        print("获取了按键字符....")

    def write(self):
        print("可以写入灯光颜色....")

# 来了一个键盘对象
k = KeyBoard()
pc(k)


class UDisk:

    def open(self):
        print("U盘启动了...")

    def close(self):
        print("U盘关闭了...")

    def read(self):
        print("读出数据")

    def write(self):
        print("写入数据")

u = UDisk()

pc(u)