import numpy as np
import matplotlib.pyplot as plt
import math

pwd='/home/tian.qiu/catalog/hsc.split/'
mag=open(pwd+'i_cmodel_mag.txt','r')
magdata=[float(x) for x in mag.readlines()]
magerr=open(pwd+'i_cmodel_magsigma.txt','r')
magerrdata=[float(x) for x in magerr.readlines()]

data=[[a,b] for a,b in zip(magdata,magerrdata)]

#按光度排序并分成 5 份
m1=min(magdata)
m2=max(magdata)
m=(m2-m1)/5
nmag=[m1,m1+m,m1+2*m,m1+3*m,m1+4*m,m2]
print(nmag)

#sorted(data,key=lambda x:x[0])
#data2=[data[i:i+math.ceil(len(data)/5)] for i in range(0,len(data),math.ceil(len(data)/5))]

#按 error 的取值分成 6 段区间
e1=min(magerrdata)
e2=max(magerrdata)
e=pow((e2/e1),1/6)
nerr=[e1,e1*e,e1*e*e,e1*e*e*e,e2/e/e,e2/e,e2]
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
n=[[0]*6 for _ in range(5)]
for i in range(5):
    for j in range(6):
        t1=adata[adata[:,0]>=nmag[i]]
        t2 = t1[t1[:, 0] <= nmag[i+1]]
        t3 = t2[t2[:, 1] >= nerr[j]]
        t4 = t3[t3[:, 1] <= nerr[j+1]]
        n[i][j]=len(t4)
print(n)
#创建窗口
plt.figure(figsize=(8,6),dpi=300)

#创建子图
plt.subplot(111)

bar_width=0.2
index=np.arange(6)

plt.title('magnitude error distribution with different i_magnitude')

#坐标
plt.xlabel('mag_err')
nerrl=[[]]*7
for i in range(7):
	nerrl[i]=round(nerr[i],7)
plt.xticks([-0.1,0.9,1.9,2.9,3.9,4.9,5.9],nerrl )
plt.ylabel('N')
plt.yscale('log')

#画图
for i in range(5):
    plt.bar(index+i*bar_width, n[i], width=bar_width, label='i_mag='+str(nmag[i])+'~'+str(nmag[i+1]))

plt.legend()
plt.savefig('1.png')




