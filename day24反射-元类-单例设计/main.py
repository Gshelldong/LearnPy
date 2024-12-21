
import socket
import ssl
from datetime import datetime,timedelta

"""
subject:((('countryName', 'CN'),), (('stateOrProvinceName', 'beijing'),), (('localityName', 'beijing'),), (('organizationName', 'Beijing Baidu Netcom Science Technology Co., Ltd'),), (('commonName', 'baidu.com'),))
issuer:((('countryName', 'BE'),), (('organizationName', 'GlobalSign nv-sa'),), (('commonName', 'GlobalSign RSA OV SSL CA 2018'),))
version:3
serialNumber:4E4003A65EB681F87F4BD8EB
notBefore:Jul  8 01:41:02 2024 GMT
notAfter:Aug  9 01:41:01 2025 GMT
subjectAltName:(('DNS', 'baidu.com'), ('DNS', 'baifubao.com'), ('DNS', 'www.baidu.cn'), ('DNS', 'www.baidu.com.cn'), ('DNS', 'mct.y.nuomi.com'), ('DNS', 'apollo.auto'), ('DNS', 'dwz.cn'), ('DNS', '*.baidu.com'), ('DNS', '*.baifubao.com'), ('DNS', '*.baidustatic.com'), ('DNS', '*.bdstatic.com'), ('DNS', '*.bdimg.com'), ('DNS', '*.hao123.com'), ('DNS', '*.nuomi.com'), ('DNS', '*.chuanke.com'), ('DNS', '*.trustgo.com'), ('DNS', '*.bce.baidu.com'), ('DNS', '*.eyun.baidu.com'), ('DNS', '*.map.baidu.com'), ('DNS', '*.mbd.baidu.com'), ('DNS', '*.fanyi.baidu.com'), ('DNS', '*.baidubce.com'), ('DNS', '*.mipcdn.com'), ('DNS', '*.news.baidu.com'), ('DNS', '*.baidupcs.com'), ('DNS', '*.aipage.com'), ('DNS', '*.aipage.cn'), ('DNS', '*.bcehost.com'), ('DNS', '*.safe.baidu.com'), ('DNS', '*.im.baidu.com'), ('DNS', '*.baiducontent.com'), ('DNS', '*.dlnel.com'), ('DNS', '*.dlnel.org'), ('DNS', '*.dueros.baidu.com'), ('DNS', '*.su.baidu.com'), ('DNS', '*.91.com'), ('DNS', '*.hao123.baidu.com'), ('DNS', '*.apollo.auto'), ('DNS', '*.xueshu.baidu.com'), ('DNS', '*.bj.baidubce.com'), ('DNS', '*.gz.baidubce.com'), ('DNS', '*.smartapps.cn'), ('DNS', '*.bdtjrcv.com'), ('DNS', '*.hao222.com'), ('DNS', '*.haokan.com'), ('DNS', '*.pae.baidu.com'), ('DNS', '*.vd.bdstatic.com'), ('DNS', '*.cloud.baidu.com'), ('DNS', 'click.hm.baidu.com'), ('DNS', 'log.hm.baidu.com'), ('DNS', 'cm.pos.baidu.com'), ('DNS', 'wn.pos.baidu.com'), ('DNS', 'update.pan.baidu.com'))
OCSP:('http://ocsp.globalsign.com/gsrsaovsslca2018',)
caIssuers:('http://secure.globalsign.com/cacert/gsrsaovsslca2018.crt',)
crlDistributionPoints:('http://crl.globalsign.com/gsrsaovsslca2018.crl',)
((('countryName', 'CN'),), (('stateOrProvinceName', 'beijing'),), (('localityName', 'beijing'),), (('organizationName', 'Beijing Baidu Netcom Science Technology Co., Ltd'),), (('commonName', 'baidu.com'),))
Aug  9 01:41:01 2025 GMT
"""

# 从证书中获取到颁发组织的名称

def get_commonname(cert_subject: tuple) -> str:
    """
    :param cert_subject: 证书的subject.
    :return: 证书颁发的目的组织,就是主域名.
    """
    subject_info = {}
    for common in cert_subject:
        for content in common:
            subject_info.update(dict([content]))
    commonname = subject_info.get('commonName')
    return commonname


domain='www222222222.baidu.com'
# 设置socket的超时时间为5秒
socket.setdefaulttimeout(3)
# 创建默认的SSL上下文
context = ssl.create_default_context()
# 创建一个SSL套接字
skt = context.wrap_socket(socket.socket(), server_hostname=domain)
skt.connect(('127.0.0.1', 443))
cert_res = skt.getpeercert()
skt.close()

# for k,v in cert_res.items():
#     print(f'{k}:{v}')


subject = cert_res['subject']
commonname = get_commonname(subject)
print(commonname)

notafter = cert_res['notAfter']

# 定义日期格式，注意两个空格和GMT部分
date_format = "%b  %d %H:%M:%S %Y GMT"

# 使用strptime()方法解析日期字符串
notafter_day = datetime.strptime(notafter, date_format)

# 证书过期时间检查
check_day = timedelta(days=15)

now_day = datetime.today()

remaining_time = notafter_day - now_day

if remaining_time < check_day:
    print('证书即将过期,请检查!')
else:
    print('证书状态正常!')
    print(f'证书剩余时间:{remaining_time}')

# a = ((('commonName', '68guakao.com'),),)
# a = ((('countryName', 'CN'),), (('stateOrProvinceName', 'beijing'),), (('localityName', 'beijing'),), (('organizationName', 'Beijing Baidu Netcom Science Technology Co., Ltd'),), (('commonName', 'baidu.com'),))








