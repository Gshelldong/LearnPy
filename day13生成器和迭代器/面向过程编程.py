def user_regis():
    username = input('请输入用户名: ').strip()
    password = input('请输入密码: ').strip()
    second_password = input('请再次输入密码: ').strip()
    if password == second_password:
        save_user_info(username,password)
        print("注册成功!")
    else:
        print("注册失败!")

def save_user_info(username,password):
    user_info = "%s|%s\n"%(username,password)
    save_disk(user_info)

def save_disk(user_info):
    with open(r'password.txt',mode='a',encoding='utf-8') as f:
        f.write(user_info)

def regis():
    user_regis()

if __name__ == '__main__':
    regis()
