#plot of histogram distribution in terms of the magnitude

import matplotlib.pyplot as plt
import pandas as pd
pwd1='/home/tian.qiu/data/result/6_6/'
pwd2='/home/tian.qiu/data/catalog/6_6/'
pwd3='/home/tian.qiu/data/plot/6_8/'
mHSC=pd.read_csv(pwd1+'matchedHSC')
mS82=pd.read_csv(pwd1+'matchedS82')
umHSC=pd.read_csv(pwd1+'unmatchedHSC')
umS82=pd.read_csv(pwd1+'unmatchedS82')
HSC=pd.read_csv(pwd2+'HSCol.csv')
S82=pd.read_csv(pwd2+'S82ol.csv')
plt.figure(figsize=(8,6),dpi=300)
plt.subplot(111)
bins1=plt.hist(mHSC.i_cmodel_mag,bins=50,color='red',label='matchedHSC',histtype='step')[1]
plt.hist(mS82.psfMag_i,bins=bins1,color='blue',label='matchedS82',histtype='step')
plt.hist(umS82.psfMag_i,bins=bins1,color='orange',label='unmatchedS82',histtype='step')
plt.hist(umHSC.i_cmodel_mag,bins=bins1,color='yellow',label='unmatchedHSC',histtype='step')
plt.hist(S82.psfMag_i,bins=bins1,color='black',label='allS82',histtype='step')
plt.hist(HSC.i_cmodel_mag,bins=bins1,color='pink',label='allHSC',histtype='step')
plt.title('magnitude distribution')
plt.ylabel('N')
plt.axis([16,25,0,0.5e5])
plt.xlabel('mag')
plt.legend()
plt.savefig(pwd3+'mag_dist_ol.png')
