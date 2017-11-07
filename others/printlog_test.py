# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:04:52 2017
@author: so
各種 print log 的 test

"""

#!/usr/bin/python3
import time
import itertools
    
for i in range(5):
    print str(i)+'\r',
    time.sleep(1)

'''
想要print始终显示在同一行，本身是在最后加上逗号即可，即：
print "xxx",
然后又想要实现，新打印的一行，冲掉之前旧的一行，达到显示出下载文件大小一点点增加，但是却始终保持同行，那么就再打印的内容最后添加上\r即可：
print "xxx\r",
'''

#%%
TXT_PATH = "/media/.../DATA/printlog/log3.txt"
f = open(TXT_PATH , "r")
while True:
    line1 = f.readline()
    line2 = f.readline()
    if not line2: break  # EOF
    print line1
    print line2

#%%
###


import sys, time
UP_ONE_LINE = "\033[F"

sys.stdout.write(" "*20 +'\n')
sys.stdout.write(" "*20 +'\n')

show_row = 2

for i in range(5):
    # clean the screen
    sys.stdout.write(UP_ONE_LINE * show_row)
    sys.stdout.write(" "*20 +'\n')
    sys.stdout.write(" "*20 +'\n')
    sys.stdout.write(UP_ONE_LINE * show_row)

    sys.stdout.write(str(i) * (10 - i) +'\n')
    sys.stdout.write(str(i) * (5 - i) +'\n')
    sys.stdout.flush()
    time.sleep(1)

   
#%%
'''
read and print
nvidia-docker_1.0.1-1_amd6 20% [====>                ]   2.16M   659KB/s    in 3.4s
'''
import time
import sys

TXT_PATH = "/media/.../DATA/printlog/log2.txt"
text_file = open(TXT_PATH , "r")
for line in text_file:
    line = line.split("\n")[0]
    line_sp = line.split(" ")[1]
    if (line_sp == "Pull" or line_sp == "100%"):
        sys.stdout.write(line+'\n'+'\r')
        sys.stdout.flush()
        time.sleep(0.5)
    else:
        sys.stdout.write(line+'\r')
        sys.stdout.flush()
        time.sleep(0.5)
print "###  done ###"
text_file.close()


#%%
###
'''
print
'''
import time
import sys
import string
import random
import numpy as np

def id_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#id_generator()  #'b8cd3wa19t28'
    
intvl1 = 25.7
intvl2 = 80.7
id_num = 7
idg = []
idg.extend([id_generator() for _ in xrange(id_num)])

seq = [round(random.uniform(300, 800),2) for _ in xrange(id_num)]

for i in xrange(id_num):          
    jumpnum = np.arange(0.0,seq[i],intvl1)
    jumpnum2 = np.arange(0.0,seq[i],intvl2) 
    for j in range(len(jumpnum)):
        print("{0}: Downloading {1:>6.2f}MB/{2}MB          ".format(idg[i],jumpnum[j],seq[i]))
    print("{0}: Download complete                        ".format(idg[i])+'\n'+'\r')
    for k in range(len(jumpnum2)):
        print("{0}: Extracting {1:>6.2f}MB/{2}MB          ".format(idg[i],jumpnum2[k],seq[i]))
    print("{0}: Pull complete                        ".format(idg[i])+'\n'+'\r')



#%%    

xxx: Waiting
xxx: Pulling fs layer
xxx: Downloading  8.732 MB/20.71 MB
xxx: Download complete
xxx: Extracting  8.732 MB/20.71 MB
xxx: Pull complete

xxx: Pulling fs layer  --->  Download complete (---> Extracting )---> Pull complete
xxx: Waiting  --->Downloading --->  Download complete ---> Extracting  ---> Pull complete
xxx: Waiting
xxx: Waiting


#%%  
'''
xxx: Waiting  ---> Downloading ---> Download complete
'''
### 1106_1
ids = ['a','j','k','b','c','p','d']
orijob = [6,2,3,5,4,8,4]
dic = dict(zip(ids, orijob))  # {'a': 6, 'c': 4, 'b': 5, 'k': 3, 'j': 4, 'p': 8}

now_id = []
now_id.append(ids.pop(0));now_id.append(ids.pop(0));now_id.append(ids.pop(0))
#nowid = ['a', 'j', 'k']

done_id = []

while(ids!=[] or now_id!=[]):
    while(len(now_id)<3 and ids!=[]):
        now_id.append(ids.pop(0))
    print "--now_id:",now_id
        #
    for j in dic :   #j is key
        if j in now_id :  ##xxx
            dic[j] = dic[j] -1
            if dic[j] <= 0:
                done_id.append(j)
                now_id.remove(j)
                print j,dic[j],"Download complete"
            else :  # orijob[j]>0
                print j,dic[j],"Downloading"
        elif j in done_id:
            print j,dic[j],"Download complete"            
        else: 
            print j,dic[j],"Waiting"
            
            

#%%
'''
xxx: Waiting  --->Downloading ---> Extracting  ---> Pull complete
'''
### 1106_2
import sys
import string
import random
import copy
from random import uniform

def id_generator(size=12, chars=string.ascii_lowercase + string.digits):
    '''
    id_generator()  #'b8cd3wa19t28'
    '''
    return ''.join(random.choice(chars) for _ in range(size))

def randnum():
    return uniform(0, 3)  #float

intvl1 = 25.0
intvl2 = 80.0
id_num = 7
ids = []
ids.extend([id_generator() for _ in xrange(id_num)])
oriids = copy.deepcopy(ids)
orijob = [round(random.uniform(300, 800),2) for _ in xrange(id_num)]

#intvl1 = 0.3
#intvl2 = 1.7
#ids = ['a','j','k','b','c','p','d']
#orijob = [6,2,7,5,4,3,4]
gudin = dict(zip(ids, orijob)) 
dic = dict(zip(ids, orijob))  # {'a': 6, 'c': 4, 'b': 5, 'k': 3, 'j': 4, 'p': 8}
dic2 = dict(zip(ids, orijob))

now_id = []
now_id.append(ids.pop(0));now_id.append(ids.pop(0));now_id.append(ids.pop(0))  #nowid = ['a', 'j', 'k']
done_id = []
    
while(ids!=[] or now_id!=[]):
    while(len(now_id)<3 and ids!=[]):
        now_id.append(ids.pop(0))
    print "--now_id:",now_id
    for j in oriids :   #j is key
        if j in now_id :  ##xxx
            dic[j] = dic[j]-intvl1-randnum()
            if dic[j] < 0:
                dic2[j] = dic2[j]-intvl2-randnum()
                if dic2[j] < 0:
                    done_id.append(j)
                    now_id.remove(j)
                    print ("{0}: Pull complete".format(j))
                    #print j,dic2[j],"Pull complete"
                else:
                    print("{0}: Extracting {1:>6.2f}MB/{2}MB          ".format(j,gudin[j]-dic2[j],gudin[j]))
                    #print("{0}: Extracting {1:>6.2f}MB/{2}MB          ".format(j,dic2[j],gudin[j]))
            else :  
                print("{0}: Downloading {1:>6.2f}MB/{2}MB          ".format(j,gudin[j]-dic[j],gudin[j]))
                #print("{0}: Downloading {1:>6.2f}MB/{2}MB          ".format(j,dic[j],gudin[j]))
        elif j in done_id:
            print ("{0}: Pull complete".format(j))  
            #print j,dic[j],"Pull complete"
        else: 
            print ("{0}: Waiting".format(j))
            #print j,dic[j],"Waiting"

    
