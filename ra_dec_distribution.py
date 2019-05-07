#画出未匹配的 HSC 中 star 的位置分布

import numpy as np
import matplotlib.pyplot as plt


pwd='/home/tian.qiu/catalog/'
HSC=np.loadtxt(pwd+'213641.csv',usecols=(0,1),delimiter=',')
HSC=np.insert(HSC,0,range(HSC.shape[0]),axis=1)

match=np.loadtxt(pwd+'match1s.txt',usecols=(0,1))
unmatch=[]
for i in range(len(match)):
    if match[i][1]==0:
        unmatch.append([HSC[int(match[i][0])][1],HSC[int(match[i][0])][2]])

unmatch=np.array(unmatch)

plt.figure(figsize=(8,6),dpi=300)
plt.scatter(unmatch[:,0],unmatch[:,1])
plt.xlabel('ra')
plt.ylabel('dec')
plt.title('dec vs ra distribution')
plt.savefig(pwd+'ra_dec_dist.png')

