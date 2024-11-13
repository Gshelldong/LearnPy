# 自定义一个装饰器实现输入对了用户名久执行函数。
def login_auth(func):
    def runfc(*args,**kwargs):
        username = input('please input username: ').strip()
        passwd = input('please input password: ').strip()
        if username == 'tom' and passwd == '1234':
            res = func(*args,**kwargs)
            return res
        else:
            print('认证失败!')
    return runfc


@login_auth
def index():
    print('登陆成功!')

@login_auth
def home():
    print('环境主页!')

# index()

home()




