"""
以下代码实现几个需求以总结装饰器的使用：
1、给一个函数添加统计时间的功能和登陆认证功能。
2、登陆认证功能只执行一次，认证一次之后再次执行该函数就不需要再次认证。
3、装饰器中添加认证的类型比如mysql\file\ldap,通过在装饰的时候传入认证类型。
"""

import time

# 创建一个统计函数执行时间的装饰器
def count_time(func):
    def get_time(*args,**kwargs):
        head_time=time.time()
        func(*args,**kwargs)
        after_time = time.time()
        print(after_time - head_time)
    return get_time

# 定义一个登陆的装饰器
def login_auth_and_type(auth_type):  # 这里在外面再封装一层通过装饰器把认证的类型传进去。
    def login_auth(func):
        def auth(*args,**kwargs):
            if login_status['is_login']:  # 通过在这里判断登陆状态判断是否直接执行被装饰的函数
                res = func(*args,**kwargs)
                return res
            else:
                if auth_type == 'file':
                    username = input('请输入用户名: ').strip()
                    password = input('请输入密码: ').strip()
                    if username == 'tom' and password == '123456':
                        login_status['is_login']=True   # 登陆成功之后设置的状态标志。
                        res = func(*args,**kwargs)
                        return res
                elif auth_type == 'mysql':
                    print('from mysql')
                elif auth_type == 'ldap':
                    print('ldap认证')
                else:
                    print('登陆失败')
        return auth
    return login_auth

login_status={'is_login': None}

@login_auth_and_type('ldap')
@count_time
def index() -> str:
    time.sleep(3)
    print("这是index函数")
    return 'index'

index()
# index()