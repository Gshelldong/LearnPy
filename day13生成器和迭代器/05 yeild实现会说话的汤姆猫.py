def tom_cat():
    print("这是一直汤姆猫!")
    while True:
        speak = yield
        print("汤姆猫说了%s"%speak)

tom = tom_cat()   # tom就是一个生成器
tom.__next__()    # 取生成器的第一个值 -> 这是一直汤姆猫!
tom.send('hello!!!')  # 用send发送内容给yield,yeild接收到了之后赋值给speak.
                      # 这个时候yield已经执行过了，跳到下一步print.
tom.send('你好！！')