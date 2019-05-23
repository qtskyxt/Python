#plot of histogram distribution in terms of the magnitude and plot of scatter distribution of delta_ra vs delta_dec

import matplotlib.pyplot as plt
import pandas as pd
from astropy.coordinates import SkyCoord
import multiprocessing as mp


pwd1='/home/tian.qiu/data/result/'
pwd2='/home/tian.qiu/data/plot/'

ml=pd.read_csv(pwd1+'matchlist')
h=pd.read_csv(pwd1+'matchedHSC')
s=pd.read_csv(pwd1+'matchedS82')
m=ml[ml.matchednum!=0]

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

hc=SkyCoord(radec[:,1],radec[:,2],unit='deg')
sc=SkyCoord(radec[:,4],radec[:,5],unit='deg')
sep=[]
for i in range(len(hc)):
	sep.append((hc[i].separation(sc[i])).arcsec)