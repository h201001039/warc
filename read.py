import os
import shelve
import hashlib
def dir_check(path):
    if not os.path.exists(path):
        os.makedirs(path)
pos=0
prev=0
temp=0
time=0
time1=0
f2=shelve.open("map")

with open('/home/harsh/cc-mrjob/common-crawl/crawl-data/CC-MAIN-2014-35/segments/1408500800168.29/warc/CC-MAIN-20140820021320-00000-ip-10-180-136-8.ec2.internal.warc') as f:
    #for content in f:
    while(1):
        content=f.readline()
        prev=pos
        pos=f.tell()
        x=content.split()
        if not content:
            break
        if not x:
            continue
        if temp==1:
            if x[0]=="WARC/1.0":
                #print content
                temp=0
                key=m.hexdigest()+":end"
                f2[key]=prev
                #print key,f2[key]
                f1.close()

            else:
                f1.write(content)
        if x[0]=="WARC-Target-URI:":
            #temp=1
            time1+=1
            #print content
            if time1==3:
                time1=0
            if time1 !=2:
                continue
            else:
                temp=1
                m = hashlib.md5()
                m.update(x[1])
                key=m.hexdigest()+":start"
                dir_check(key[0])
                dir_check(key[0]+'/'+key[1])
                dir_check(key[0]+'/'+key[1]+'/'+key[2])
                path=key[0]+'/'+key[1]+'/'+key[2]
                f1=open(os.path.join(path,m.hexdigest()),'a')
                #f1=open(m.hexdigest(),'a')
                f2[key]=pos
                #print key,f2[key]
        #if f.tell() >10000:
            #break

