import time
def progress(percent):
    if percent > 1:
        percent = 1
    res = int(50 * percent) * '#'
    print( '\r[%-50s ] %d%%  巡检中请等待...' %(res,int( 100 * percent)), end='')


for i in range(1,11):
    time.sleep(0.2)
    res = i / 10

    progress(res)
