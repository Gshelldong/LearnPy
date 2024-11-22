from core import src

def pass_check(func):
    def func_in(*args,**kwargs):
        if src.user_status.get('is_login'):
            res = func(*args,**kwargs)
            return res
        else:
            print("请滚去登陆!")
    return func_in