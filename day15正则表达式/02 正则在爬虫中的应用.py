import re
import requests

# url = 'https://www.maoyan.com/board/4?offset=0'
#
# res = requests.get(url=url)
# res_content = res.text

with open(r'index.html',mode='r',encoding='utf-8') as f:
    html = f.read()
f.close()

partten=r'https:\/\/[^\s]+\.jpg'
image_urls = re.findall(partten,html)
for i in image_urls:
    print(i)




# content = '<img data-src="https://p0.pipi.cn/mmdb/54ecde3311ef2abe12f0ee281b37b5fc0bc2b.jpg?imageView2/1/w/160/h/220" alt="肖申克的救赎" class="board-img" />'
#
# print()