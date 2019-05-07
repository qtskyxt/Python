#match HSC 与 Stripe82 中的相同 star，匹配后转移到另一个文件中

import numpy as np
from astropy.coordinates import SkyCoord  #利用 astropy内置函数加快计算


pwd='/home/tian.qiu/catalog/'

#读取 HSC 数据，1ra 2dec 3-6g,r,i,z 7-10g,r,i,z err 0增加编码 先只读取位置和 r,i re,ie
HSC=np.loadtxt(pwd+'213641.csv',usecols=(0,1,4,8),delimiter=',')
HSC=np.insert(HSC,0,range(HSC.shape[0]),axis=1)

#读取 S82 数据，1ra 2dec 3rExt 4-8u,g,r,i,z 9-13u,g,r,i,z err 0 增加编码 
S82=np.loadtxt(pwd+'S82coaddStars.dat',usecols=(0,1,6,11))
S82=np.insert(S82,0,range(S82.shape[0]),axis=1)

#创建切片的数组，切片总数据为 360 份，根据 ra 每度为一份，加快运行
HSCs=[[] for i in range(360)]
S82s=[[] for i in range(360)]
for i in range(HSC.shape[0]):
    HSCs[int(HSC[i][1])].append(HSC[i])
for i in range(S82.shape[0]):
    S82s[int(S82[i][1])].append(S82[i])

#定义函数，判断两者是否在 1 角秒的范围内，返回 T or F
def dis(i,j,k):
	a=SkyCoord(HSCs[k][i][1],HSCs[k][i][2],unit='deg')
	b=SkyCoord(S82s[k][j][1],S82s[k][j][2],unit='deg')
	c=a.separation(b)
	if c.arcsec <=1:
		return True
	else:
		return False

'''
    d2 = (HSCs[k][i][1] - S82s[k][j][1]) ** 2 + (HSCs[k][i][2] - S82s[k][j][2]) ** 2
    # 距离小于 1 角秒，1/3600
    if d2 <= (1/3600)**2:
        return True
    else:
        return False
'''

#创建记录文件，记录匹配的总数和编号
match=open(pwd+'match1s_aspy.txt','w')

#根据HSC每一行的目标寻找匹配的Stripe82中的目标
for k in range(360):
	for i in range(len(HSCs[k])):
		match.write(str(int(HSCs[k][i][0]))+' ')
		n=0
		for j in range(len(S82s[k])):
			if dis(i,j,k):
				n=n+1
				match.write(str(int(S82s[k][j][0]))+' ')
		match.write(str(n)+'\n')
match.close()





