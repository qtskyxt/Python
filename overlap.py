#find the overlap part of two catalogs

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
    if radec[ra]!=[] and ra<=radec[ra][1] and ra>=radec[ra][0]:
        t = HSCl[i]
        olHSC.write(t)

olHSC.close()

for i in range(len(S82l)):
    ra=int(S82[i][0])
    if radec[ra]!=[] and ra<=radec[ra][1] and ra>=radec[ra][0]:
        x = S82l[i]
        olS82.write(x)

olS82.close()