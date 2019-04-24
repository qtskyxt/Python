pwd='/home/tian.qiu/catalog/'
HSC=open(pwd+'213641.csv','r')
lines=HSC.readlines()
ra=[]
dec=[]
for i in range(len(lines)):
    t=lines[i].split(',')
    ra.append(t[0])
    dec.append(t[1])
RA=open(pwd+'result/ra.txt','w')
DEC=open(pwd+'result/dec.txt','w')
for i in range(len(lines)-1):
    RA.write(ra[i+1]+"\n")
    DEC.write(dec[i+1]+"\n")

