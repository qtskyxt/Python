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
ra=[[] for i in range(360)] #to store the overlapped dec for every degree of ra.
dec=[]
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