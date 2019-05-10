#find the overlap part of two catalogs

import numpy as np

pwd1='/home/tian.qiu/data/catalog/'
HSC=np.loadtxt(pwd1+'224959.csv',usecols=(0,1),delimiter=',')
HSCl=open(pwd1+'224959.csv','r')
t=HSCl.readline()
olHSC=open(pwd1+'olHSC','w')#overlapped HSC catalog
olHSC.write(t)

S82=np.loadtxt(pwd1+'S82coaddStars.dat',usecols=(0,1))
S82l=open(pwd1+'S82coaddStars.dat','r')
t=S82l.readline()
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

HSCs=np.array(HSCs)
S82s=np.array(S82s)

#find out the overlapped dec range for each ra degree
radec=[[] for i in range(360)]#to store the range
for i in range(360):
	a=max(HSCs[i][:,1])
	b=max(S82s[i][:,1])
	decmax=min(a,b)
	a=min(HSCs[i][:,1])
	b=min(S82s[i][:,1])
	decmin=max(a,b)
	radec[i].append(decmin)
	radec[i].append(decmax)


#判断HSC中的数据是否在上述的范围内，在则存在新catalog 中
for i in range(len(HSCl)):
    t=HSCl.readline()
    ra=int(t[0])
    if ra<=radec[ra][1] and ra>=radec[ra][0]:
        olHSC.write(t)

olHSC.close()

for i in range(len(S82l)):
    t=S82l.readline()
    ra=int(t[0])
    if ra<=radec[ra][1] and ra>=radec[ra][0]:
        olS82.write(t)

olS82.close()