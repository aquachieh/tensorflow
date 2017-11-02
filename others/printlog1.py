# -*- coding: utf-8 -*-
'''
# Install Nvidia-docker
# command:$ wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb
# output:
nvidia-docker_1.0.1-1_amd6  100%[==============================>]     2.16M  771KB/s  in 2.9s   
'''

import time
import sys
import random
import datetime

TXT0 = ["wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb\n",
"--2017-11-01 18:18:12--  https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb\nResolving github.com (github.com)... 192.30.253.113, 192.30.253.112\nConnecting to github.com (github.com)|192.30.253.113|:443... ","connected.\n"
"HTTP request sent, awaiting response... ","302 Found\nLocation: https://github-production-release-asset-2e65be.s3.amazonaws.com/45557469/d4efc7cc-ff73-11e6-91a2-ce84b8670fcd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20171101%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20171101T101813Z&X-Amz-Expires=300&X-Amz-Signature=fa888f4dffc7b6626820ee6a1fe350bd8d5b68b587f08280d7d1c6df2a76dbbb&X-Amz-SignedHeaders=host&actor_id=0&response-content-disposition=attachment%3B%20filename%3Dnvidia-docker_1.0.1-1_amd64.deb&response-content-type=application%2Foctet-stream [following]\n--2017-11-01 18:18:13--  https://github-production-release-asset-2e65be.s3.amazonaws.com/45557469/d4efc7cc-ff73-11e6-91a2-ce84b8670fcd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20171101%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20171101T101813Z&X-Amz-Expires=300&X-Amz-Signature=fa888f4dffc7b6626820ee6a1fe350bd8d5b68b587f08280d7d1c6df2a76dbbb&X-Amz-SignedHeaders=host&actor_id=0&response-content-disposition=attachment%3B%20filename%3Dnvidia-docker_1.0.1-1_amd64.deb&response-content-type=application%2Foctet-stream\nResolving github-production-release-asset-2e65be.s3.amazonaws.com (github-production-release-asset-2e65be.s3.amazonaws.com)... 52.216.2.8\nConnecting to github-production-release-asset-2e65be.s3.amazonaws.com (github-production-release-asset-2e65be.s3.amazonaws.com)|52.216.2.8|:443... ",
"connected.\n","HTTP request sent, awaiting response... ","200 OK\nLength: 2266050 (2.2M) [application/octet-stream]\nSaving to: ‘/tmp/nvidia-docker_1.0.1-1_amd64.deb’\n\n"]

for tt in TXT0:
    sys.stdout.write(tt)
    sys.stdout.flush()
    time.sleep(0.5)

###
row = 20
length = 30
totalA = 2.163
totalB = 771
timesleep = 0.5
totaltime = 2.9
seq = sorted([random.randint(1, 100) for _ in xrange(row)])
txt1 = "nvidia-docker_1.0.1-1_amd6 "

sys.stdout.write("{0} {3:>3d}%[{1} {2}] {4:>8d}  --,-KB/s\r".format(txt1,'='*0,' '*length,0, 0 , "--,-" ))
sys.stdout.flush()
time.sleep(timesleep)
for i in seq:
    if totalA*i*0.01<1.0 :
        sys.stdout.write("{0} {3:>3d}%[{1}>{2}] {4:>8.2f}K {5:>4d}KB/s   \r".format(txt1,'='*(int(i*length/100.0)),' '*(length-int(i*length/100.0)),int(i),
                          totalA*i*0.01*1000 , int(totalB*i*0.01) ))
        sys.stdout.flush()
        time.sleep(timesleep)
    else :
        sys.stdout.write("{0} {3:>3d}%[{1}>{2}] {4:>8.2f}M {5:>4d}KB/s   \r".format(txt1,'='*(int(i*length/100.0)),' '*(length-int(i*length/100.0)),int(i),
                          totalA*i*0.01 , int(totalB*i*0.01) ))
        sys.stdout.flush()
        time.sleep(timesleep)
sys.stdout.write("{0} {3:>3d}%[{1}>{2}] {4:>8.2f}M {5:>4d}KB/s  in {6}s   \n\n".format(txt1, '='*length, ' '*0, 100, totalA, int(totalB), totaltime ))      


dd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sys.stdout.write("{} ({} KB/s) - ‘/tmp/nvidia-docker_1.0.1-1_amd64.deb’ saved [2266050/2266050]\n".format(dd,totalB)) 
#sys.stdout.write("2017-11-01 18:18:17 (771 KB/s) - ‘/tmp/nvidia-docker_1.0.1-1_amd64.deb’ saved [2266050/2266050]\n")    #-------date

