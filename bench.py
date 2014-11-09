import shelve
import random
import time
start_time = time.time()
for i in range(0,1):
    f=shelve.open("map")
    x=random.choice(f.keys())
    #print x.split(':')[1]
    if x.split(':')[1] == "start" :
        y=x.split(':')[0]+":end"
    else:
         y=x.split(':')[0]+":start"
    print f[x],f[y]
    if f[y]-f[x] > 0:
        d=f[y]-f[x]
        d1=f[x]
    else:
        d=f[x]-f[y]
        d1=f[y]
    f1= open('/home/harsh/cc-mrjob/common-crawl/crawl-data/CC-MAIN-2014-35/segments/1408500800168.29/warc/CC-MAIN-20140820021320-00000-ip-10-180-136-8.ec2.internal.warc','rb')
    f1.seek(d1)
    print f1.read(d)
    f1.close()

