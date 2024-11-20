import os

dn = os.path.dirname(__file__)   # 获取当前文件的路径
filepath = os.path.join(dn,'myfile')

content_list = os.listdir(filepath)

# 根据用户输入查看文件内容
# while True:
#     for i,j in enumerate(content_list,1):
#         print(i,j)
#     user_in = input('请输入你想看的小说编号: ').strip()
#     if user_in.isdigit():
#         user_in = int(user_in)
#         if user_in in range(len(content_list)+1):
#             file_name = content_list[user_in-1]
#             open_file_path=os.path.join(filepath,file_name)
#             with open(open_file_path,mode='r',encoding='utf-8') as f:
#                 print(f.read())
#         else:
#             print('请输入正确的编号！')


# 创建文件夹,已经存在会报错
# os.makedirs('mkd')

# 判断目录是否存在返回布尔值
print(os.path.isdir('mkd'))

# 判断文件是否存在,不能判断文件夹，返回布尔值
print(os.path.isfile('myfile\\斗罗大陆.txt'))
print(os.path.exists('myfile\\斗罗大陆.txt'))

# 切换工作的目录
#print(os.chdir('d:\\'))

'''
>>> os.chdir('d:\\')
获取当前的路径
>>> os.getcwd()
'd:\\'
'''

# 获取文件的大小
size = os.path.getsize('myfile\\斗罗大陆.txt')
print("%.2f"%(size/1024/1024),"MB")