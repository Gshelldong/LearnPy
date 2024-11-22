
from lib import common

user_status = {
    "is_login": None
}

def register():
    print("register")

def user_login():
    username = input("请输入用户名>>>: ").strip()
    password = input("请输入密码>>>: ").strip()
    if username =='tom' and password =='123456':
        user_status['is_login'] = True
    else:
        print("用户名密码错误请重新登录")

@common.pass_check
def shopping():
    print("shopping")

def pay():
    print("pay")

choice_menue = {
    '1': register,
    '2': user_login,
    '3':shopping,
    '4': pay
}

def run():
    while True:
        print("""
        1 : 注册
        2 : 用户登陆
        3 : 购物
        4 : 支付
        """)
        choice = input('请输入你想使用的功能: ').strip()
        if choice not in choice_menue:continue
        choice_menue[choice]()

