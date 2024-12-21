
import importlib
import settings

# 实现框架部分的功能
def run(plugin):
    while True:
        cmd = input('请输入要执行的命令: ')
        if cmd == 'exit':
            break
        # 因为无法确定框架使用者是否传入正确的对象所以需要使用反射来检测
        # 判断对象是否具备处理这个指令的方法
        if hasattr(plugin,cmd):
            func = getattr(plugin, cmd)
            func()
        else:
            print('还没有实现此功能.')
    print('exit.....')

setting_args = settings.CLASS_PATH
mode_path, mode_name = setting_args.rsplit('.',1)

mk = importlib.import_module(mode_path)

# 这里获取到plugins中的class类
cls = getattr(mk, mode_name)

# 实例化一个对象
obs = cls()

# 放在框架中跑
run(obs)

"""
这种方式重写之后我们只需要在配置文件中控制CLASS_PATH是要使用
LinuxCmd还是WindowsCmd就可以控制想要得到的功能。
很好的解耦合。

CLASS_PATH = "libs.plugins.LinuxCmd"
"""


