import md1

print(__name__)   # 如果在本命名空间执行返回的就是__main__
print(md1.__name__)   # 如果是通过import导入到其它命名空间则值是原来命名空间的名字
