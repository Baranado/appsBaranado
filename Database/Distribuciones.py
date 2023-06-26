import math
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
#datos=[18.0,22.2,27.0,28.3,10.0,38.0,66.4,62.5,24.0,24.0,37.0,20.4,28.4,54.0,40.0,21.0,40.0,38.0,50.0,45.0,27.0,34.0,52.0,27.0,37.0,33.0,29.0,30.5,17.5,38.0,37.5,31.5,33.0,31.0,30.0,15.7,26.5,24.7,19.0,15.0,19.0,18.5,20.1,28.4,38.5,25.9,29.0,20.5,22.5,20.0,21.4,36.8,24.6,19.5,27.5,20.0,26.2,24.2,44.0,58.0,49.0,49.5,25.2,54.8,48.0,48.0,28.4,24.2,20.5,21.0,22.0,20.5,43.4,14.2,22.2]
estacion="Mojo"
conn=sqlite3.Connection("dataSenamhi.db")
query=f"select gestion, max(Precipitación) as Pmax24 from (select gestion, Precipitación from datos where estacion = '{estacion}' and Precipitación > 0) group by gestion"
#print(query)
df=pd.read_sql_query(query,conn)
conn.commit()
conn.close()
def normpdf(x,u):
    return math.exp(-0.5*((x-u[0])/u[1])**2)/math.sqrt(2*math.pi)/u[1]
def lognormpdf(x,u):
    return math.exp(-0.5*((math.log(x)-u[0])/u[1])**2)/math.sqrt(2*math.pi)/u[1]/x
n=df["Pmax24"].size
mu=df["Pmax24"].mean()  
sigma=df["Pmax24"].std()
param=[[mu,sigma],[math.log(mu**2/math.sqrt(mu**2+sigma**2)),math.sqrt(math.log(sigma**2/mu**2+1))]]
xmin=df["Pmax24"].min()
xmax=df["Pmax24"].max()
print(xmax,xmin)
interv=50
delta=(xmax-xmin)/interv
wbins=5
nbins=int(math.ceil((xmax-xmin)/wbins))
xrange=[]
for i in range(0,interv):
    xrange.append(xmin+i*delta)
y1=[normpdf(item,param[0]) for item in xrange]
y2=[lognormpdf(item,param[1]) for item in xrange]
fig,ax=plt.subplots()
plt.hist(df["Pmax24"],nbins,density=True,alpha=0.5,edgecolor="black")
ax.plot(xrange, y1, "-", label="normal")
ax.plot(xrange, y2, "--", label="lognormal")
ax.set_xlabel("Precipitation")
ax.set_ylabel("Probability density")
ax.set_title(f"Frequency distributions: {estacion}\n$\mu={round(mu,3)}$, $\sigma={round(sigma,3)}$")
fig.tight_layout()
plt.savefig("figure.jpeg")
