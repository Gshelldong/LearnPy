
"""
这是一个下载程序能够提供缓存大小
缓存大小不能查超过内存限制
"""


class Downloader():
    def __init__(self,name,url,buffer_size):
        self.name =name
        self.url = url
        self.__buffer_size = buffer_size


    def start_download(self):
        if self.__buffer_size < 1024 * 8:
            print('启动下载')
        else:
            print('内存炸了')

    def set_buffer_size(self,size):
        if type(size) != int:
            print('输入必须是整型')
        else:
            print('缓存修改成功!')
            self.__buffer_size = size

    def get_buffer_size(self):
        print(self.__buffer_size)


# 通过写方法的方式来修内部的变量
dl = Downloader('movie.rmvb','www.baidu.com',1024*4)
dl.set_buffer_size(1024*9)
dl.start_download()
dl.get_buffer_size()

