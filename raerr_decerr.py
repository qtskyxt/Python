#scatter plot of ra_err vs dec_err

#not finitshed

import matplotlib.pyplot as plt
import pandas as pd
pwd1='/home/tian.qiu/data/catalog/'
pwd2='/home/tian.qiu/data/plot/'
HSC=pd.read_csv(pwd1+'olHSC')
S82=pd.read_csv(pwd1+'olS82',sep='\s+')

hs=HSC.sample(frac=0.01,axis=0)
ss=S82.sample(frac=0.01,axis=0)

plt.figure(figsize=(8,6),dpi=300)
plt.subplot(111)
plt.scatter()

plt.xlabel('ra')
plt.ylabel('dec')
plt.legend()

plt.savefig(pwd2+'ra_dec_errdist_5.22.png')