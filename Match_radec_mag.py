#match HSC 与 Stripe82 中的相同 star，匹配后转移到另一个文件中,use SkyCoord and slice with mag and ra

import numpy as np
from astropy.coordinates import SkyCoord  #利用 astropy内置函数加快计算


pwd1='/home/tian.qiu/data/catalog/'
pwd2='/home/tian.qiu/data/result/'

#读取 HSC 数据，1ra 2dec 3-6g,r,i,z 7-10g,r,i,z err 0增加编码 先只读取位置和 i ,i err
HSC=np.loadtxt(pwd1+'224959.csv',usecols=(0,1,4,8),delimiter=',')
HSC=np.insert(HSC,0,range(HSC.shape[0]),axis=1)

#读取 S82 数据，1ra 2dec 3rExt 4-8u,g,r,i,z 9-13u,g,r,i,z err 0 增加编码 
S82=np.loadtxt(pwd1+'S82coaddStars.dat',usecols=(0,1,6,11))
S82=np.insert(S82,0,range(S82.shape[0]),axis=1)

#创建切片的数组，切片总数据为 360 份，根据 ra 每度为一份，加快运行,再根据亮度分成 13-25每 2 度一份，6 份
HSCs=[[[] for i in range(6)] for j in range(360)]
S82s=[[[] for i in range(6)] for j in range(360)]
for i in range(HSC.shape[0]):
	HSCs[int(HSC[i][1])][int((HSC[i][3]-13)/2)].append(HSC[i])
for i in range(S82.shape[0]):
	S82s[int(S82[i][1])][int((S82[i][3]-13)/2)].append(S82[i])

def sep_s2m(Ara,Adec,Bras,Bdecs):
	s=SkyCoord(Ara,Adec,unit='deg')
	m=SkyCoord(Bras,Bdecs,unit='deg')
	sep=s.separation(m)
	return sep.arcsec

'''
#定义函数，判断两者是否在 1 角秒的范围内，返回 T or F
def dis(i,j,k,m):
	a=SkyCoord(HSCs[k][m][i][1],HSCs[k][m][i][2],unit='deg')
	b=SkyCoord(S82s[k][m][j][1],S82s[k][m][j][2],unit='deg')
	c=a.separation(b)
	if c.arcsec <=1:
		return True
	else:
		return False

    d2 = (HSCs[k][i][1] - S82s[k][j][1]) ** 2 + (HSCs[k][i][2] - S82s[k][j][2]) ** 2
    # 距离小于 1 角秒，1/3600
    if d2 <= (1/3600)**2:
        return True
    else:
        return False
'''

#创建记录文件，记录匹配的总数和编号
match=open(pwd2+'match1s_aspy_mag.txt','w')

#根据HSC每一行的目标寻找匹配的Stripe82中的目标
for k in range(360):
	for m in range(6):
		if HSCs[k][m] != []:
			HSCs[k][m] = np.vstack(HSCs[k][m])
		else:
			continue
		if S82s[k][m] != []:
			S82s[k][m] = np.vstack(S82s[k][m])
		else:
			continue
		for i in range(len(HSCs[k][m])):
			match.write(str(HSCs[k][m][i][0])+' ')
			n=0
			sep=sep_s2m(HSCs[k][m][i][1],HSCs[k][m][i][2],S82s[k][m][:,1],S82s[k][m][:,2])
			for j in range(len(sep)):
				if sep[j]<=1:
					n=n+1
					match.write(str(S82s[k][m][j][0])+' ')
			match.write(str(n)+'\n')
match.close()





