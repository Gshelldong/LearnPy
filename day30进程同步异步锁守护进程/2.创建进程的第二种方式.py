from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running'%self.name)
        time.sleep(3)
        print('%s is end'%self.name)


if __name__ == '__main__':
    p = MyProcess("gong")
    p.start()
    print('主')