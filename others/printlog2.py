# -*- coding: utf-8 -*-
'''
printlog2.py
# Install Nvidia-docker
# command: $ sudo nvidia-docker run --rm nvidia/cuda nvidia-smi
# output: 
	1yk9vffxy2c9: Downloading   0.00MB/369.61MB          
	1yk9vffxy2c9: Downloading  55.70MB/369.61MB          
	1yk9vffxy2c9: Downloading 111.40MB/369.61MB          
	1yk9vffxy2c9: Downloading 167.10MB/369.61MB          
	1yk9vffxy2c9: Downloading 222.80MB/369.61MB          
	1yk9vffxy2c9: Downloading 278.50MB/369.61MB          
	1yk9vffxy2c9: Downloading 334.20MB/369.61MB          
	1yk9vffxy2c9: Pull complete  
'''
import time
import sys
import string
import random
import numpy as np

def id_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#id_generator()  #'b8cd3wa19t28'
timesleep = 0.1
intvl = 15.7
id_num = 5
idg = []
idg.extend([id_generator() for _ in xrange(id_num)])

seq = [round(random.uniform(300, 800),2) for _ in xrange(id_num)]

for i in xrange(id_num):          
    jumpnum = np.arange(0.0,seq[i],intvl) 
    for j in range(len(jumpnum)):
        sys.stdout.write("{0}: Downloading {1:>6.2f}MB/{2}MB          ".format(idg[i],jumpnum[j],seq[i])+'\r')
        sys.stdout.flush()
        time.sleep(timesleep)
    sys.stdout.write("{0}: Pull complete                        ".format(idg[i])+'\n'+'\r')

