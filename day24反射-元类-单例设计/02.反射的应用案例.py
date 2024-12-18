
"""
反射被称为框架的基石,为什么
因为框架的设计者,不可能提前知道你的对象到底是怎么设计的
所以你提供给框架的对象 必须通过判断验证之后才能正常使用
判断验证就是反射要做的事情,
当然通过__dict__也是可以实现的, 其实这些方法也就是对__dict__的操作进行了封装


需求:要实现一个用于处理用户的终端指令的小框架
框架就是已经实现了最基础的构架,就是所有项目都一样的部分
"""

from day24.libs import plugins


def run(plugin):
    while True:
        cmd = input('请输入要执行的命令: ')
        if cmd == 'exit':
            break
        if hasattr(plugin,cmd):
            func = getattr(plugin, cmd)
            func()
        else:
            print('还没有实现此功能.')

    print('exit.....')

"""
这种方式通过核心的判断
hasattr
getattr
方式判断了从plugins中不同类中方法的实现。
run() 命令提供了最基础的实现方法，具体的方法由plugins提供。

这种方式 写死了必须使用某个类,这是不合理的,因为无法提前知道对方的类在什么地方以及类叫什么
所以我们应该为框架的使用者提供一个配置文件,要求对方将类的信息写入配置文件，然后框架run()自己去加载需要的模块
"""

linux = plugins.LinuxCmd()
# windows = plugins.WinCmd()
run(linux)


