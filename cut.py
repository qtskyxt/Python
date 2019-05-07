#cut off the nonoverlapped catalog

import numpy as np


pwd='/home/tian.qiu/catalog/'
HSC=np.loadtxt(pwd+'213641.csv',usecols=(0),delimiter=',')
HSCl=open(pwd+'213641.csv','r')
t=HSCl.readline()
S82=np.loadtxt(pwd+'S82coaddStars.dat',usecols=(0))
cut=open(pwd+'cutHSC','w')#用来储存 cut 后的 catalog
cut.write(t)

#寻找 S82 中 ra 的范围
a=int(S82[0])
b=[[] for i in range(2)]
n=1
for i in range(len(S82)):
    if a<=S82[i] and a+n>=S82[i]:
        continue
    else:
        n=n+1
        if a <= S82[i] and a + n >= S82[i]:
            continue
        else:
            print(a,a+n-1)
            b[0].append(a)
            b[1].append(a+n-1)
            a=int(S82[i])
            n=1
print(a,a+n)
b[0].append(a)
b[1].append(a+n)

#判断HSC中的数据是否在上述的范围内，在则存在新catalog 中
for i in range(len(HSC)):
    t=HSCl.readline()
    for j in range(len(b[0])):
        if HSC[i]>=b[0][j] and HSC[i]<=b[1][j]:
            cut.write(t)
            break
cut.close()


