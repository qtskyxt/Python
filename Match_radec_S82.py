#match HSC 与 Stripe82 中的相同 star，匹配后转移到另一个文件中,use SkyCoord and slice with mag and ra

import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord  #利用 astropy内置函数加快计算
import multiprocessing as mp


pwd1='/home/tian.qiu/data/catalog/'
pwd2='/home/tian.qiu/data/result/'

#读取 HSC 数据，1ra 2dec 3-6g,r,i,z 7-10g,r,i,z err 0增加编码 先只读取位置和 i ,i err
#HSC=np.loadtxt(pwd1+'224959.csv',usecols=(0,1,4,8),delimiter=',')
#HSC=np.insert(HSC,0,range(HSC.shape[0]),axis=1)
HSC=pd.read_csv(pwd1+'olHSC')

#读取 S82 数据，1ra 2dec 3rExt 4-8u,g,r,i,z 9-13u,g,r,i,z err 0 增加编码
#S82=np.loadtxt(pwd1+'S82coaddStars.dat',usecols=(0,1,6,11))
#S82=np.insert(S82,0,range(S82.shape[0]),axis=1)
S82=pd.read_csv(pwd1+'olS82',sep='\s+')

#创建切片的数组，切片总数据为 360 份，根据 ra 每度为一份，加快运行,再根据亮度分成 13-25每 2 度一份，6 份
'''
HSCs=[[[] for i in range(6)] for j in range(360)]
S82s=[[[] for i in range(6)] for j in range(360)]
for i in range(HSC.shape[0]):
	HSCs[int(HSC[i][1])][int((HSC[i][3]-13)/2)].append(HSC[i])
for i in range(S82.shape[0]):
	S82s[int(S82[i][1])][int((S82[i][3]-13)/2)].append(S82[i])
'''
HSCs=[[] for i in range(360)]
S82s=[[] for i in range(360)]
for i in range(360):
	HSCs[i]=HSC[(HSC.ra>=i)&(HSC.ra<i+1)]
	S82s[i]=S82[(S82.ra>=i)&(S82.ra<i+1)]
'''
def sep_s2m(Ara,Adec,Bras,Bdecs):
	s=SkyCoord(Ara,Adec,unit='deg')
	m=SkyCoord(Bras,Bdecs,unit='deg')
	sep=s.separation(m)
	return sep.arcsec
'''
def sep_s2m(A,Bs):
	s=SkyCoord(A[0],A[1],unit='deg')
	m=SkyCoord(Bs[:,0],Bs[:,1],unit='deg')
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

#创建记录文件，记录匹配的总数和编号，at the meanwhile, output the unmatched list and the matched list both in HSC and S82
#match=open(pwd2+'match1s_aspy_mag.txt','w')
matchedHSC=[pd.DataFrame(columns=HSC.columns) for i in range(360)]
matchedS82=[pd.DataFrame(columns=S82.columns) for i in range(360)]
unmatchedHSC=[pd.DataFrame(columns=HSC.columns) for i in range(360)]
unmatchedS82=[pd.DataFrame(columns=S82.columns) for i in range(360)]
matchlist=[pd.DataFrame(columns=['HSCindex','HSCimag','matchednum']) for i in range(360)]
TF=[[] for i in range(360)]

def calculate(i):
	t=[]
	print(i,'b',flush=True)
	As = S82s[i].values
	Bs = HSCs[i].values
	for j in range(len(S82s[i])):
		sep = sep_s2m(As[j], Bs)
		m = sep<=1
		t.append([])
		for k in range(len(m)):
			if m[k]:
				t[j].append(k)
	print(i,'e',flush=True)
	return t



def putout(i):
	print(i,'wb',flush=True)
	matchedHSC = pd.DataFrame(columns=HSC.columns)
	matchedS82 = pd.DataFrame(columns=S82.columns)
	unmatchedS82 = pd.DataFrame(columns=S82.columns)
	matchlist = pd.DataFrame(columns=['S82index', 'S82imag', 'S82ra','S82dec','matchednum'])
	for j in range(len(TF[i])):
		n = 0
		sra=S82s[i].iloc[j].ra
		sdec=S82s[i].iloc[j].dec
		matchlist = matchlist.append({'S82index': int(S82s[i].iloc[j].name), 'S82imag': S82s[i].iloc[j].iM,'S82ra': sra,'S82dec' :sdec}, ignore_index=True)
		for k in range(len(TF[i][j])):
			if TF[i][j]!=[]:
				n = n + 1
				matchedHSC = matchedHSC.append(HSCs[i].iloc[TF[i][j][k]])
				matchlist.loc[j, 'matchedHSCindex' + str(n)] = int(HSCs[i].iloc[TF[i][j][k]].name)
				matchlist.loc[j, 'HSCimag' + str(n)] = HSCs[i].iloc[TF[i][j][k]].i_cmodel_mag
				hra=HSCs[i].iloc[TF[i][j][k]].ra
				hdec=HSCs[i].iloc[TF[i][j][k]].dec
				matchlist.loc[j, 'HSCra' + str(n)] = hra
				matchlist.loc[j, 'HSCdec' + str(n)] = hdec
				matchlist.loc[j, 'HSCsep' + str(n)] = SkyCoord(sra,sdec,unit='deg').separation(SkyCoord(hra,hdec,unit='deg')).arcsec
		if n != 0:
			matchedS82 = matchedS82.append(S82s[i].iloc[j])
		else:
			unmatchedS82 = unmatchedS82.append(S82s[i].iloc[j])
		matchlist.loc[j, 'matchednum'] = n
	print(i,'we',flush=True)
	return matchedHSC,matchedS82,unmatchedS82,matchlist
''' too slow to output with pandas during the calculation 
			n=0
			matchlist=matchlist.append({'HSCindex':int(HSCs[i].iloc[j].name),'HSCimag':HSCs[i].iloc[j].i_cmodel_mag},ignore_index=True)
#			sep=sep_s2m(HSCs[i].iloc[j].ra,HSCs[i].iloc[j].dec,S82s[i].ra,S82s[i].dec)
			sep=sep_s2m(As[j],Bs)
			for k in range(len(sep)):
				if sep[k]<=1:
					n=n+1
					matchedS82=matchedS82.append(S82s[i].iloc[k])
					matchlist.loc[j,'matchedS82index'+str(n)]=int(S82s[i].iloc[k].name)
					matchlist.loc[j,'S82imag'+str(n)]=S82s[i].iloc[k].iM
			if n!=0:
				matchedHSC = matchedHSC.append(HSCs[i].iloc[j])
			else:
				unmatchedHSC=unmatchedHSC.append(HSCs[i].iloc[j])
			matchlist.loc[j, 'matchednum'] = n
			print(i,j,n)
'''
s=[]
for i in range(360):
	if S82s[i].empty:
		continue
	else:
		s.append(i)


pool1=mp.Pool(20)
data=pool1.map(calculate,s)
pool1.close()
for i in s:
	TF[i]=data[s.index(i)]
print('calculation finished',flush=True)

pool2=mp.Pool(20)
data=pool2.map(putout,s)
pool2.close()
for i in s:
	matchedHSC[i]=data[s.index(i)][0]
	matchedS82[i]=data[s.index(i)][1]
	unmatchedS82[i]=data[s.index(i)][2]
	matchlist[i]=data[s.index(i)][3]
print('output finished',flush=True)

m=pd.concat([matchlist[i] for i in s],sort=False)
mh=pd.concat([matchedHSC[i] for i in s],sort=False)
ums=pd.concat([unmatchedS82[i] for i in s],sort=False)
ms=pd.concat([matchedS82[i] for i in s],sort=False)
mh=mh.drop_duplicates()
umh=(HSC.append(mh)).drop_duplicates(keep=False)

mh.to_csv(pwd2+'matchedHSC',index_label='HSCindex')
ms.to_csv(pwd2+'matchedS82',index_label='S82index')
umh.to_csv(pwd2+'unmatchedHSC',index_label='HSCindex')
ums.to_csv(pwd2+'unmatchedS82',index_label='S82index')
m.to_csv(pwd2+'matchlist',index=False)




#根据HSC每一行的目标寻找匹配的Stripe82中的目标
'''
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
'''




