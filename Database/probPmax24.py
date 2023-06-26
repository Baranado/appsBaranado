import math
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
datos=[18.0,22.2,27.0,28.3,10.0,38.0,66.4,62.5,24.0,24.0,37.0,20.4,28.4,54.0,40.0,21.0,40.0,38.0,50.0,45.0,27.0,34.0,52.0,27.0,37.0,33.0,29.0,30.5,17.5,38.0,37.5,31.5,33.0,31.0,30.0,15.7,26.5,24.7,19.0,15.0,19.0,18.5,20.1,28.4,38.5,25.9,29.0,20.5,22.5,20.0,21.4,36.8,24.6,19.5,27.5,20.0,26.2,24.2,44.0,58.0,49.0,49.5,25.2,54.8,48.0,48.0,28.4,24.2,20.5,21.0,22.0,20.5,43.4,14.2,22.2]
n=len(datos)
meano=sum(datos)/n
print(f"mean:{meano}")
mu=stats.tmean(datos)
print(f"mean:{mu}")
stdevo=(sum([(item-mu)**2 for item in datos])/(n-1))**.5
print(f"stdev:{stdevo}")
sigma=stats.tstd(datos)
print(f"stdev:{sigma}")
var=sigma**2
fig,ax=plt.subplots()
#mean,var,skew,kurt=stats.norm.stats(moments='mvsk')
#print(f"mean:{mean}\nvar:{var}\nskew:{skew}\nkurt:{kurt}\nstdev:{stdev}")
x=np.linspace(min(datos),max(datos),100)
ax.plot(x,stats.norm.pdf(x,loc=mu,scale=sigma),'r-',lw=3,label='norm')
ax.plot(x,stats.lognorm.pdf(x,s=sigma,loc=mu,scale=sigma),'r--',lw=3,label='lognorm')
#rv=stats.norm()
#ax.plot(x,rv.pdf(x),'k-',lw=2,label='frozen pdf')
#y1=stats.norm.ppf(x,loc=mean,scale=stdev)
#np.allclose([0.001,0.5,0.999],stats.norm.cdf(vals))
#r=stats.norm.rvs(size=100)
ax.hist(datos,density=True,bins='auto',histtype='bar',alpha=0.6,rwidth=.85)
#ax.set_xlim([x[0],x[-1]])
#ax.legend(loc='best',frameon=False)
plt.savefig("figure.jpeg")
#counts, bins = np.histogram(x)
#plt.stairs(counts, bins)
#plt.savefig("figure.jpeg")
