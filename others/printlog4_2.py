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

def randnum():
    return uniform(0, 2)  #float

UP_ONE_LINE = "\033[F"
time_s = 0.32
intvl1 = 3.2
intvl2 = 7.7
id_num = 6
length = 12

ids = ["Install ubuntu16.04","Install nvidia/cuda:8.0-cudnn6","Install TensorFlow dependencies","Install TensorFlow GPU version","Set up notebook config","Copy sample notebooks"]

oriids = copy.deepcopy(ids)
orijob = [373.24,286.84,65.32,50.33,48.15,86.21]

gudin = dict(zip(ids, orijob)) 
dic = dict(zip(ids, orijob))  
dic2 = dict(zip(ids, orijob))

now_id = []
now_id.append(ids.pop(0));now_id.append(ids.pop(0));now_id.append(ids.pop(0))  
done_id = []

show_row = id_num

def clean_the_screen(row):
    for i in xrange(row): # clean the screen
        sys.stdout.write(" "*80 +'\n')

clean_the_screen(show_row)

while(ids!=[] or now_id!=[]):
    while(len(now_id)<3 and ids!=[]):
        now_id.append(ids.pop(0))
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
                    sys.stdout.write(" "*80+'\r')
                    sys.stdout.write("{0:<31}: Pull complete".format(j)+'\n')
                else:
                    sys.stdout.write("{0:<31}: Extracting [{1}>{2}] {4:>6.2f}MB/{5}MB".format(j,'='*(int((gudin[j]-dic2[j])/gudin[j]*length)),' '*(length-int((gudin[j]-dic2[j])/gudin[j]*length)),int((gudin[j]-dic2[j])/gudin[j]*100.0),gudin[j]-dic2[j] ,gudin[j])+'\n')
            else :  
                sys.stdout.write("{0:<31}: Downloading [{1}>{2}] {4:>6.2f}MB/{5}MB".format(j,'='*(int((gudin[j]-dic[j])/gudin[j]*length)),' '*(length-int((gudin[j]-dic[j])/gudin[j]*length)),int((gudin[j]-dic[j])/gudin[j]*100.0),gudin[j]-dic[j] ,gudin[j])+'\n')
        elif j in done_id:
            sys.stdout.write(" "*80+'\r')
            sys.stdout.write("{0:<31}: Pull complete".format(j)+'\n')  
        else: 
            sys.stdout.write("{0:<31}: Waiting".format(j)+'\n')
    sys.stdout.flush()
    time.sleep(time_s)

TXT0 = "\nDigest: sha256:685ae5cc01ecb126569fcf9c8ee6168dea003fa836c46e2f5b7f9f0fbabf3fa3\nStatus: Downloaded newer image for tensorflow/tensorflow:latest-devel-gpu\n"

sys.stdout.write(TXT0)
sys.stdout.flush()


