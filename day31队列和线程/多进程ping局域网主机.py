import subprocess
from multiprocessing import Pool


# 生成 192.168.1.0/24 网段的主机列表
def generate_ip_list():
    base_ip = "192.168.232."
    return [f"{base_ip}{i}" for i in range(1, 255)]  # 忽略 .0 和 .255


# 探测主机是否在线
def ping_host(ip):
    try:
        # 使用 ping 命令探测主机是否在线
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "1000", ip],  # Windows 系统
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode == 0:
            return f"{ip} is online"
        else:
            return f"{ip} is offline"
    except Exception as e:
        return f"{ip} error: {e}"


if __name__ == "__main__":
    # 生成主机列表
    ip_list = generate_ip_list()

    # 定义进程池的大小
    pool_size = 10

    # 使用多进程探测
    with Pool(processes=pool_size) as pool:
        results = pool.map(ping_host, ip_list)

    # 打印结果
    for result in results:
        print(result)
