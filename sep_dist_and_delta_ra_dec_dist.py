#plot of histogram distribution in terms of the magnitude and plot of scatter distribution of delta_ra vs delta_dec
#insert the curve_fit for the sep distribution (May.29)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

from astropy.coordinates import SkyCoord
import multiprocessing as mp


pwd1='/home/tian.qiu/data/result/5_27/'
pwd2='/home/tian.qiu/data/plot/5_30/'

ml=pd.read_csv(pwd1+'matchlist')
#h=pd.read_csv(pwd1+'matchedHSC')
#s=pd.read_csv(pwd1+'matchedS82')
m=ml[ml.matchednum!=0]

n=50

Y=m.HSCsep1
x=np.array(range(n+1))/n
y=[]
for i in range(n):
    temp=len(Y[(Y>=x[i])&(Y<x[i+1])])
    y.append(temp)
y=np.array(y)
y=y/sum(y)*n
x=np.delete(x,-1)

def func(theta,sigma):
    y=1/(sigma**2)*np.exp(-(theta)**2/(2*sigma**2))*theta
    return y

popt,pcov=curve_fit(func,x,y)

plt.figure(figsize=(8,12))
plt.subplot(211)
plt.hist(m.HSCsep1,bins=n,color='red',histtype='step',label='distribution')
plt.plot(x,func(x,popt)/n*len(m),label=r'$\frac{1}{\sigma^2}exp(-\frac{-\theta^2}{2\sigma^2})\theta]$')
plt.ylabel('N')
plt.title('separation distribution')
plt.legend()
plt.subplot(212)
plt.hist(m.HSCsep1,bins=n,color='red',histtype='step',label='distribution')
plt.plot(x,func(x,popt)/n*len(m),label=r'$\frac{1}{\sigma^2}exp[-\frac{-\theta^2}{2\sigma^2}]\theta]$, $\sigma$=%1.5f'%(popt))
plt.ylabel('N')
plt.yscale('log')
plt.axis([-0.01,1.01,1,1e5])
plt.xlabel('separation/arcsec')
plt.savefig(pwd2+'sep_dist_5_30.png')
plt.close()

#ms=m.sample(frac=0.005,axis=0)
delta_ra=(m.HSCra1.values-m.S82ra.values)*3600
delta_dec=(m.HSCdec1.values-m.S82dec.values)*3600
plt.figure()
plt.title(r'$\delta_{dec}$ vs $\delta_{ra}$ distribution')
plt.scatter(delta_ra,delta_dec,alpha=1,s=0.1)
plt.xlabel(r'$\delta_{ra}/arcsec$')
plt.ylabel(r'$\delta_{dec}/arcsec$')
plt.axis([-1,1,-1,1])
plt.savefig(pwd2+'delta_ra_dec_dist_5_30.png')
plt.close()

plt.figure()
plt.hist(delta_ra,bins=n,color='red',histtype='step',label=r'$\delta_{ra}$')
plt.hist(delta_dec,bins=n,color='blue',histtype='step',label=r'$\delta_{dec}$')
plt.title(r'$\delta_{ra}$ and $\delta_{dec}$ distribution')
plt.ylabel('N')
plt.yscale('log')
plt.xlabel('separation/arcsec')
plt.legend()
plt.savefig(pwd2+'delta_dist_5_30.png')
plt.close()

