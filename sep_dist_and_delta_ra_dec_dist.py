#plot of histogram distribution in terms of the magnitude and plot of scatter distribution of delta_ra vs delta_dec

import matplotlib.pyplot as plt
import pandas as pd
from astropy.coordinates import SkyCoord
import multiprocessing as mp


pwd1='/home/tian.qiu/data/result/'
pwd2='/home/tian.qiu/data/plot/'

ml=pd.read_csv(pwd1+'matchlist')
#h=pd.read_csv(pwd1+'matchedHSC')
#s=pd.read_csv(pwd1+'matchedS82')
m=ml[ml.matchednum!=0]

plt.figure()
plt.hist(m.S82sep1,bins=40,color='red',histtype='step')
plt.title('separation distribution')
plt.ylabel('N')
plt.yscale('log')
plt.xlabel('separation/arcsec')
plt.savefig(pwd2+'sep_dist_5_23.png')
plt.close()

ms=m.sample(frac=0.005,axis=0)
delta_ra=(ms.HSCra.values-ms.S82ra1.values)*3600
delta_dec=(ms.HSCra.values-ms.S82ra1.values)*3600
plt.figure()
plt.title('delta_dec vs delta_ra distribution')
plt.scatter(delta_ra,delta_dec,alpha=0.3,s=0.1)
plt.xlabel('ra/arcsec')
plt.ylabel('dec/arcsec')
plt.axis([-1,1,-1,1])
plt.savefig(pwd2+'delta_ra_dec_dist_5_23.png')
'''
radec=pd.DataFrame(columns=['HSCindex','ra1','dec1','S82index','ra2','dec2'])
def output(i):
	hi=m.iloc[i].HSCindex
	si=m.iloc[i].matchedS82index1
	ra1=h[h.HSCindex==hi].iloc[0].ra
	dec1=h[h.HSCindex==hi].iloc[0].dec
	ra2=s[s.S82index==si].iloc[0].ra
	dec2=s[s.S82index==si].iloc[0].dec
	return hi,si,ra1,dec1,ra2,dec2

pool=mp.Pool(20)
data=pool.map(output,range(len(m)))

hc=SkyCoord(radec.ra1,radec.dec1,unit='deg')
sc=SkyCoord(radec.ra2,radec.dec2,unit='deg')
sep=[]
for i in range(len(hc)):
	sep.append((hc[i].separation(sc[i])).arcsec)
'''

