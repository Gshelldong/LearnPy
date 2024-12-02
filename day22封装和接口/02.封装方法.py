"""
把一些不固定功能的方法给封装起来在类里面直接调用，
比如电脑开机的过程。
"""

class PC:
    def __init__(self,price,kind,color):
        self.price = price
        self.kind = kind
        self.color = color

    def open(self):
        print("接通电源")
        self.__check_device()
        print("载入内核")
        print("初始化内核")
        self.__start_services()
        print("启动GUI")
        self.__login()


    def __check_device(self):  # 检测硬件的方法是固定的所以可以单独封装成内部的私有方法，在内部调用
        print("硬件检测1")
        print("硬件检测2")
        print("硬件检测3")
        print("硬件检测4")

    def __start_services(self):
        print("启动服务1")
        print("启动服务2")
        print("启动服务3")
        print("启动服务4")

    def  __login(self):
        print("login....")
        print("login....")
        print("login....")

pc1 = PC(20000,"香蕉","黄色")
# pc1.open()

pc1.login()
