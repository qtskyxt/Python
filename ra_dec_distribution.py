#画出 HSC 和 S82 中 star 的位置分布

import numpy as np
import matplotlib.pyplot as plt


pwd='/home/tian.qiu/data/catalog/'
HSC=np.loadtxt(pwd+'213641.csv',usecols=(0,1),delimiter=',')
HSC=np.insert(HSC,0,range(HSC.shape[0]),axis=1)
S82=np.loadtxt(pwd+'S82coaddStars.dat',usecols=(0,1))
S82=np.insert(S82,0,range(S82.shape[0]),axis=1)


plt.figure(figsize=(8,12),dpi=300)
plt.subplot(211)
plt.scatter(HSC[:,1],HSC[:,2])
plt.subplot(212)
plt.scatter(S82[:,1],S82[:,2])
plt.xlabel('ra')
plt.ylabel('dec')
plt.title('dec vs ra distribution')
plt.savefig(pwd+'ra_dec_dist.png')

