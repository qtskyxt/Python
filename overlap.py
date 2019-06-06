#find the overlap part of two catalogs

#modified with pandas. June.6th 2019

import pandas as pd

pwd='/home/tian.qiu/data/catalog/6_6/'
s=pd.read_csv(pwd+'S82_6_6.csv')
h=pd.read_csv(pwd+'HSC_6_6.csv')

sh=pd.DataFrame(columns=h.columns)
ss=pd.DataFrame(columns=s.columns)

for i in range(360):
    th=h[(h.ra>i)&(h.ra<i+1)]
    ts=s[(s.ra>i)&(s.ra<i+1)]
    if th.empty or ts.empty:
        continue
    maxdec=min(max(th.dec),max(ts.dec))
    mindec=max(min(th.dec),min(ts.dec))
    sh=sh.append(th[(th.dec>=mindec)&(th.dec<=maxdec)])
    ss=ss.append(ts[(ts.dec>=mindec)&(ts.dec<=maxdec)])

sh.to_csv(pwd+'S82ol.csv',index=False)
ss.to_csv(pwd+'HSCol.csv',index=False)

'''
import numpy as np

pwd1='/home/tian.qiu/data/catalog/'
HSC=np.loadtxt(pwd1+'224959.csv',usecols=(0,1),delimiter=',')
HSCl=open(pwd1+'224959.csv','r')
t=HSCl.readline()
HSCl=HSCl.readlines()
olHSC=open(pwd1+'olHSC','w')#overlapped HSC catalog
olHSC.write(t)

S82=np.loadtxt(pwd1+'S82coaddStars.dat',usecols=(0,1))
S82l=open(pwd1+'S82coaddStars.dat','r')
t=S82l.readline()
S82l=S82l.readlines()
olS82=open(pwd1+'olS82','w')#overlapped S82 catalog
olS82.write(t)


#try to find out overlapped ra range and dec range with each deg of ra.

#slice the data into 360 degree
HSCs=[[] for i in range(360)]
S82s=[[] for i in range(360)]
for i in range(HSC.shape[0]):
    HSCs[int(HSC[i][0])].append(HSC[i])
for i in range(S82.shape[0]):
    S82s[int(S82[i][0])].append(S82[i])
for i in range(360):
    if HSCs[i]!=[]:
        HSCs[i]=np.vstack(HSCs[i])
    if S82s[i]!=[]:
        S82s[i]=np.vstack(S82s[i])

#find out the overlapped dec range for each ra degree
radec=[[] for i in range(360)]#to store the range
for i in range(360):
    if HSCs[i]!=[] and S82s[i]!=[]:
        decmax=min(max(HSCs[i][:,1]),max(S82s[i][:,1]))
        decmin=max(min(HSCs[i][:,1]),min(S82s[i][:,1]))
        radec[i].append(decmin)
        radec[i].append(decmax)

#判断HSC中的数据是否在上述的范围内，在则存在新catalog 中
for i in range(len(HSCl)):
    ra=int(HSC[i][0])
    dec=HSC[i][1]
    if radec[ra]!=[] and dec<=radec[ra][1] and dec>=radec[ra][0]:
        x = HSCl[i]
        olHSC.write(x)

olHSC.close()

for i in range(len(S82l)):
    ra=int(S82[i][0])
    dec=S82[i][1]
    if radec[ra]!=[] and dec<=radec[ra][1] and dec>=radec[ra][0]:
        x = S82l[i]
        olS82.write(x)

olS82.close()
'''
