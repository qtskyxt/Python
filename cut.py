#cut off the nonoverlapped catalog

import numpy as np


pwd='/home/tian.qiu/catalog/'
HSC=open(pwd+'213641.csv','r')
S82=np.loadtxt(pwd+'S82coaddStars.dat')

a=int(S82[0][0])
n=1
for i in range(len(S82)):
    if a<=S82[i][0] and a+n>=S82[i][0]:
        continue
    else:
        n=n+1
        if a <= S82[i][0] and a + n >= S82[i][0]:
            continue
        else:
            print(a,a+n)
            a=int(S82[i][0])
            n=1



