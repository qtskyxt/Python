#画出 HSC 和 S82 中 star 的位置分布

import pandas as pd
import matplotlib.pyplot as plt

pwd1='/home/tian.qiu/data/catalog/'
pwd2='/home/tian.qiu/data/plot/'
HSC=pd.read_csv(pwd1+'olHSC')
S82=pd.read_csv(pwd1+'olS82',sep='\s+')

hs=HSC.sample(frac=0.005,axis=0)
ss=S82.sample(frac=0.005,axis=0)


plt.figure(figsize=(8,6),dpi=300)
plt.title('dec vs ra distribution')
plt.scatter(hs.ra,hs.dec,label='HSC',alpha=0.3,s=0.1)
plt.scatter(ss.ra,ss.dec,color='red',label='S82',alpha=0.3,s=0.1)

plt.xlabel('ra')
plt.ylabel('dec')
plt.legend()
plt.savefig(pwd2+'ra_dec_dist_5_22.png')

