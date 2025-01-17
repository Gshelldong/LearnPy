
import subprocess

cmd = input('>>>: ').strip()
console = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(console.stdout.read().decode('gbk'))  # 标准输出，只会读取一次，后面不会再读取
print(console.stderr.read().decode('gbk'))  # 标准错误输出