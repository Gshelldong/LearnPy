
import subprocess

cmd = input('>>>: ').strip()
console = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(console.stdout.read().decode('gbk'))
print(console.stderr.read().decode('gbk'))