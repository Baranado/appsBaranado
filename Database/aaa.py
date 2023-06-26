import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=[18.0,22.2,27.0,28.3,10.0,38.0,66.4,62.5,24.0,24.0,37.0,20.4,28.4,54.0,40.0,21.0,40.0,38.0,50.0,45.0,27.0,34.0,52.0,27.0,37.0,33.0,29.0,30.5,17.5,38.0,37.5,31.5,33.0,31.0,30.0,15.7,26.5,24.7,19.0,15.0,19.0,18.5,20.1,28.4,38.5,25.9,29.0,20.5,22.5,20.0,21.4,36.8,24.6,19.5,27.5,20.0,26.2,24.2,44.0,58.0,49.0,49.5,25.2,54.8,48.0,48.0,28.4,24.2,20.5,21.0,22.0,20.5,43.4,14.2,22.2]
n=len(x)
mu=sum(x)/n
print("mu",mu)
sigma=math.sqrt(sum([(item-mu)**2 for item in x])/(n-1))
print("sigma",sigma)
def normpdf(x,mu,sigma):
    return math.exp(-0.5*((x-mu)/sigma)**2)/sigma/math.sqrt(2*math.pi)
def lognormpdf(x,m,s):
    m2=m**2
    s2=s**2
    mu=math.log(m2/math.sqrt(m2+s2))
    sigma=math.sqrt(math.log(s2/m2+1))
    return math.exp(-0.5*((math.log(x)-mu)/sigma)**2)/sigma/x/math.sqrt(2*math.pi)
xrange=[]
y1=[]
y2=[]
for i in range(1,100):
    xrange.append(i)
    y1.append(normpdf(i,mu,sigma))
    y2.append(lognormpdf(i,mu,sigma))

xmin=min(x)
xmax=max(x)
rang=xmax-xmin
k=math.ceil(1+math.log(n,2))
binsx=np.linspace(xmin,xmax,k)
#print(binsx)
df=pd.qcut(x,q=k)
print(df.value_counts())
#print(df.mind)
print("xmin:",xmin)
print("xmax:",xmax)
print("rang:",rang)


#plt.hist(x,weights=np.ones_like(x)/len(x))

'''plt.plot(xrange,y1)
plt.plot(xrange,y2)
plt.savefig("figure.jpeg")
print("calculo terminado")'''
