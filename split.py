pwd='/home/tian.qiu/catalog/'
HSC=open(pwd+'213641.csv','r')
lines=HSC.readlines()
names=lines[0].split(',')
files=[]
for i in range(len(names)):
    files.append(open(pwd+'result/'+names[i]+'.txt','w'))
for i in range(len(lines)-1):
    t=lines[i+1].split(',')
    for j in range(len(names)):
        files[j].write(t[j]+"\n")


