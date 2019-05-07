#plot of histogram distribution in terms of the magnitude

import numpy as np
import matplotlib.pyplot as plt

pwd='/home/tian.qiu/catalog/'
HSC=np.loadtxt(pwd+'cutHSC',usecols=(0,1,4),delimiter=',')

plt.figure(figsize=(8,6),dpi=300)
plt.subplot(111)
plt.hist(HSC[:,2],bins=20)

plt.title('magnitude distribution')
plt.ylabel('N')
plt.xlabel('mag')
