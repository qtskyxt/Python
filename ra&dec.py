pwd='/home/tian.qiu/catalog/'
HSC=open(pwd+'213641.csv','r')
lines=HSC.readlines()
ra=[]
dec=[]
for i in range(len(HSC)):
    t=lines.split()
    ra.append(t[0])
    dec.append(t[1])
RA=open(pwd+'result/ra.txt','w')
DEC=open(pwd+'result/dec.txt','w')
for i in range(len(HSC)):
    RA.write(ra[i]+"\n")
    DEC.write(dec[i]+"\n")

