
import sys

# 打印全部的参数包括本身和传入的
if len(sys.argv) !=3:
    print(sys.argv)
    print("请输入脚本的启动参数用户名和密码!")
else:
    username = sys.argv[1]
    password = sys.argv[2]
    if username == 'admin' and password == '123456':
        print('欢迎使用!')
    else:
        print('请输入正确的用户名和密码!')