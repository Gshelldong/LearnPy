
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
            pass

    def set_buffer_size(self):
        pass

    def get_buffer_size(self):
        pass

dl = Downloader('movie.rmvb','www.baidu.com',1024*4)
