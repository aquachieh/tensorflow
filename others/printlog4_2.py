# -*- coding: utf-8 -*-
'''
# Install Nvidia-docker
# command: $ sudo nvidia-docker run --rm nvidia/cuda nvidia-smi
# output: 
  TensorFlow dependencies: Pull complete                                                       
   TensorFlow GPU version: Pull complete                                                       
   Set up notebook config: Pull complete                                                       
    Copy sample notebooks: Pull complete                                                       
  Fix some Jupyter issues: Pull complete                                                       

Digest: sha256:685ae5cc01ecb126569fcf9c8ee6168dea003fa836c46e2f5b7f9f0fbabf3fa3
Status: Downloaded newer image for tensorflow/tensorflow:latest-devel-gpu

'''
       
### 1106_1
import sys, time
import string
import random
import copy
from random import uniform

def id_generator(size=12, chars=string.ascii_lowercase + string.digits): #id_generator()  #'b8cd3wa19t28'
    return ''.join(random.choice(chars) for _ in range(size))

def randnum():
    return uniform(0, 2)  #float

UP_ONE_LINE = "\033[F"
time_s = 0.22
intvl1 = 3.2
intvl2 = 7.7
id_num = 5
length = 30

#ids = ["TF dependencies","TensorFlow GPU version","Set up notebook config","Copy sample notebooks","Add a wrapper script to fix Jupyter issues"]
ids = ["TensorFlow dependencies","TensorFlow GPU version","Set up notebook config","Copy sample notebooks","Fix some Jupyter issues"]
#ids = []
#ids.extend([id_generator() for _ in xrange(id_num)])
oriids = copy.deepcopy(ids)
orijob = [326.24,256.84,65.32,48.15,86.21]
#orijob = [round(random.uniform(30, 500),2) for _ in xrange(id_num)]

gudin = dict(zip(ids, orijob)) 
dic = dict(zip(ids, orijob))  # {'a': 6, 'c': 4, 'b': 5, 'k': 3, 'j': 4, 'p': 8}
dic2 = dict(zip(ids, orijob))

now_id = []
now_id.append(ids.pop(0));now_id.append(ids.pop(0));now_id.append(ids.pop(0))  #nowid = ['a', 'j', 'k']
done_id = []

show_row = id_num

def clean_the_screen(row):
    for i in xrange(show_row): # clean the screen
        sys.stdout.write(" "*46 +'\n')

clean_the_screen(show_row)

while(ids!=[] or now_id!=[]):
    while(len(now_id)<3 and ids!=[]):
        now_id.append(ids.pop(0))
    #print "--now_id:",now_id
    sys.stdout.write(UP_ONE_LINE * show_row)
    clean_the_screen(show_row)
    sys.stdout.write(UP_ONE_LINE * show_row)
    for j in oriids :   #j is key
        if j in now_id :  ##xxx
            dic[j] = dic[j]-intvl1-randnum()
            if dic[j] < 0:
                dic2[j] = dic2[j]-intvl2-randnum()
                if dic2[j] < 0:
                    done_id.append(j)
                    now_id.remove(j)
                    sys.stdout.write(" "*95+'\r')
                    sys.stdout.write("{0:>25}: Pull complete".format(j)+'\n')
                else:
                    #sys.stdout.write("{0}: Extracting {1:>6.2f}MB/{2}MB          ".format(j,gudin[j]-dic2[j],gudin[j])+'\n')
                    sys.stdout.write("{0:>25}: Extracting  {3:>3d}%[{1}>{2}] {4:>6.2f}MB/{5}MB".format(j,'='*(int((gudin[j]-dic2[j])/gudin[j]*length)),' '*(length-int((gudin[j]-dic2[j])/gudin[j]*length)),int((gudin[j]-dic2[j])/gudin[j]*100.0),gudin[j]-dic2[j] ,gudin[j])+'\n')
            else :  
                #sys.stdout.write("{0}: Downloading {1:>6.2f}MB/{2}MB          ".format(j,gudin[j]-dic[j],gudin[j])+'\n')
                sys.stdout.write("{0:>25}: Downloading {3:>3d}%[{1}>{2}] {4:>6.2f}MB/{5}MB".format(j,'='*(int((gudin[j]-dic[j])/gudin[j]*length)),' '*(length-int((gudin[j]-dic[j])/gudin[j]*length)),int((gudin[j]-dic[j])/gudin[j]*100.0),gudin[j]-dic[j] ,gudin[j])+'\n')
        elif j in done_id:
            sys.stdout.write(" "*95+'\r')
            sys.stdout.write("{0:>25}: Pull complete".format(j)+'\n')  
        else: 
            sys.stdout.write("{0:>25}: Waiting".format(j)+'\n')
    sys.stdout.flush()
    time.sleep(time_s)

TXT0 = "\nDigest: sha256:685ae5cc01ecb126569fcf9c8ee6168dea003fa836c46e2f5b7f9f0fbabf3fa3\nStatus: Downloaded newer image for tensorflow/tensorflow:latest-devel-gpu\n"

sys.stdout.write(TXT0)
sys.stdout.flush()
#time.sleep(0.5)

