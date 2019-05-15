#plot of histogram distribution in terms of the magnitude

import matplotlib.pyplot as plt
import pandas as pd
pwd1='/home/tian.qiu/data/catalog/'
pwd2='/home/tian.qiu/data/plot/'
HSC=pd.read_csv(pwd1+'olHSC')
S82=pd.read_csv(pwd1+'olS82',sep='\s+')

plt.figure(figsize=(8,6),dpi=300)
plt.subplot(111)
bins1=plt.hist(S82.iM,bins=20,color='red',label='S82',histtype='step')[1]
plt.hist(HSC.i_cmodel_mag,bins=bins1,color='blue',label='HSC',histtype='step')
plt.title('magnitude distribution')
plt.ylabel('N')
plt.xlabel('mag')
plt.legend()
plt.savefig(pwd+'mag_dist_ol.png')
