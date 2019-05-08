#plot of histogram distribution in terms of the magnitude

import numpy as np
import matplotlib.pyplot as plt

pwd='/home/tian.qiu/catalog/'
HSC=np.loadtxt(pwd+'cutHSC',usecols=(0,1,4),delimiter=',')
S82=np.loadtxt(pwd+'S82coaddStars.dat',usecols=(0,1,6))

plt.figure(figsize=(8,6),dpi=300)
plt.subplot(111)
bins1=plt.hist(S82[:,2],bins=20,color='red',label='S82',histtype='step')[1]
plt.hist(HSC[:,2],bins=bins1,color='blue',label='HSC',histtype='step')
plt.title('magnitude distribution')
plt.ylabel('N')
plt.xlabel('mag')
plt.legend()
plt.savefig(pwd+'mag_dist.png')
