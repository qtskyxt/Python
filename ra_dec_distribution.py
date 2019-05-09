#画出 HSC 和 S82 中 star 的位置分布

import numpy as np
import matplotlib.pyplot as plt


pwd1='/home/tian.qiu/data/catalog/'
pwd2=='/home/tian.qiu/data/plot/'
HSC=np.loadtxt(pwd1+'213641.csv',usecols=(0,1),delimiter=',')
HSC=np.insert(HSC,0,range(HSC.shape[0]),axis=1)
S82=np.loadtxt(pwd1+'S82coaddStars.dat',usecols=(0,1))
S82=np.insert(S82,0,range(S82.shape[0]),axis=1)


plt.figure(figsize=(8,12),dpi=300)
plt.title('dec vs ra distribution')
plt.scatter(HSC[:,1],HSC[:,2],label='HSC',alpha=0.005)
plt.scatter(S82[:,1],S82[:,2],color='red',label='S82',alpha=0.005)

plt.xlabel('ra')
plt.ylabel('dec')
plt.title('dec vs ra distribution')
plt.legend()
plt.savefig(pwd2+'ra_dec_dist.png')

