#find the overlap part of two catalogs

import numpy as np

pwd1='/home/tian.qiu/data/catalog/'
HSC=open(pwd1+'224959.csv','r')
HSCl=HSC
HSC.readline()
t=HSCl.readline()
olHSC=open(pwd1+'olHSC','w')#overlapped HSC catalog
olHSC.write(t)

S82=open(pwd1+'S82coaddStars.dat','r')
S82l=S82
S82.readline()
t=S82l.readline()
olS82=open(pwd1+'olS82','w')#overlapped S82 catalog
olS82.write(t)


#try to find out overlapped ra range and dec range with each deg of ra.

#slice the data into 360 degree
HSCs=[[] for i in range(360)]
S82s=[[] for i in range(360)]
for i in range(len(HSC)):
    HSCs[int(HSC[i][0])].append(HSC[i])
for i in range(len(S82):
    S82s[int(S82[i][0])].append(S82[i])

HSCs=np.array(HSCs)
S82s=np.array(S82s)

#find out the overlapped dec range for each ra degree
radec=[[] for i in range(360)]#to store the range
for i in range(360):
    decmax=min(max(HSCs[:,1]),max(S82s[:,1]))
    decmin=max(min(HSCs[:,1]),min(S82s[:,1]))
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