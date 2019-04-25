import numpy as np
import matplotlib.pyplot as plt
import math

pwd='/home/tian.qiu/catalog/hsc.split/'
mag=open(pwd+'i_cmodel_mag.txt','r')
magdata=[float(x) for x in mag.readlines()]
magerr=open(pwd+'i_cmodel_magsigma.txt','r')
magerrdata=[float(x) for x in magerr.readlines()]

data=[[a,b] for a,b in zip(magdata,magerrdata)]

#按光度排序并分成 n 份
n=5
m1=min(magdata)
m2=max(magdata)
nmag=np.linspace(m1,m2,n+1)
print(nmag)

#sorted(data,key=lambda x:x[0])
#data2=[data[i:i+math.ceil(len(data)/5)] for i in range(0,len(data),math.ceil(len(data)/5))]

#按 error 的取值分成 m 段等比区间
m=10
e1=min(magerrdata)
e2=max(magerrdata)
nerr=np.geomspace(e1,e2,m+1)
print(e1,e2)
print(nerr)

#对每一段区间不同光度的 star 个数进行计数 n[i][j] 表示第 i 段光度中，第 j 段 err 的个数
'''
for i in range(len(data)):
    for j in range(5):

    if data[i][0] >= nmag[0] and data[i][0] < nmag[1]:

    elif data[i][0] >= nmag[1] and data[i][0] < nmag[2]:

    elif data[i][0] >= nmag[2] and data[i][0] < nmag[3]:

    elif data[i][0] >= nmag[3] and data[i][0] < nmag[4]:

    else:
'''
adata=np.array(data)
n=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        t1=adata[adata[:,0]>=nmag[i]]
        t2 = t1[t1[:, 0] <= nmag[i+1]]
        t3 = t2[t2[:, 1] >= nerr[j]]
        t4 = t3[t3[:, 1] <= nerr[j+1]]
        n[i][j]=len(t4)
print(n)
#创建窗口
plt.figure(figsize=(10,6),dpi=300)

#创建子图
plt.subplot(111)

bar_width=0.2
index=np.arange(m)
xindex=range(m+1)

plt.title('magnitude error distribution with different i_magnitude')

#坐标
plt.xlabel('mag_err')
nerrl=[[]]*(m+1)
for i in range(m+1):
	nerrl[i]=round(nerr[i],5)
plt.xticks([xindex-0.1,nerrl )
plt.ylabel('N')
plt.yscale('log')

#画图
for i in range(n):
    plt.bar(index+i*bar_width, n[i], width=bar_width, label='i_mag='+str(nmag[i])+'~'+str(nmag[i+1]))

plt.legend()
plt.savefig('2.png')




