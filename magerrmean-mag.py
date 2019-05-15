#横轴为 mag 纵轴为 mag error mean，观测分布

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pwd1='/home/tian.qiu/data/catalog/'
pwd2='/home/tian.qiu/data/plot'
data=pd.read_csv('name')
mag=data.i_cmodel_mag.values
error=data.i_cmodel_magsigma.values
'''
mag=open(pwd+'i_cmodel_mag.txt','r')
magdata=[float(x) for x in mag.readlines()]
magerr=open(pwd+'i_cmodel_magsigma.txt','r')
magerrdata=[float(x) for x in magerr.readlines()]
data=[[a,b] for a,b in zip(magdata,magerrdata)]
'''
#按光度排序并分成 n 份
n=30
m1=min(mag)
m2=max(mag)
nmag=np.linspace(m1,m2,n+1)
print(nmag)

#计算每个光度区间的 error 的平均值 merr
merr=[0]*n
for i in range(n):
#	t1=adata[adata[:,0]>=nmag[i]]
#	t2=t1[t1[:,0]<=nmag[i+1]]
	merr[i]=np.mean(data[(data.i_cmodel_mag>=nmag[i])&(data.i_cmodel_mag<nmag[i+1])].i_cmodel_magsigma)
print(merr)

#创建窗口
plt.figure(figsize=(8,6),dpi=300)

#创建子图
plt.subplot(111)

bar_width=1
index=np.arange(n)
xindex=np.arange(n+1)
xindex=xindex[0::3]

plt.title('magnitude error mean distribution with different i_magnitude')

#坐标
plt.xlabel('magnitude')
for i in range(n+1):
	nmag[i]=round(nmag[i],3)
nmagl=nmag[0::3]
plt.xticks(xindex-0.5,nmagl)
plt.ylabel('mag error mean')
#plt.yscale('log')


#画图
plt.bar(index, merr, width=bar_width,edgecolor='black')
plt.savefig('4.png')
