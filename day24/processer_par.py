import time


def progress(percent):
    if percent > 1:
        percent = 1
    res = int(50 * percent) * '#'
    print( '\r[%-50s ] %d%%' %(res,int( 100 * percent)), end='')


download_size = 0
total_size=204800

while download_size < total_size:
    download_size += 10000
    percent = download_size / total_size
    time.sleep(0.2)
    progress(percent)