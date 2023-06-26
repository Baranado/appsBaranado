# A partir de las precipitaciones de una estacion en la base de datos, nos devuelve las precipitaciones maximas en 24 horas
import math                                          
import pandas as pd
import numpy as np                                   
import sqlite3
import matplotlib.pyplot as plt
'''
def datPreciMax24(estacion):
    conn=sqlite3.Connection("./Database/dataSenamhi.db"
    cur=conn.cursor()
    query=f'SELECT gestion,MAX(precipitación) AS PrecMax24 FROM preci{estacion} GROUP BY gestion ORDER BY PrecMax24'
    df=pd.read_sql_query(query,conn)
    conn.commit()
    conn.close()
    return df['PrecMax24']
'''
datos=np.array([18.0,22.2,27.0,28.3,10.0,38.0,66.4,62.5,24.0,24.0,37.0,20.4,28.4,54.0,40.0,21.0,40.0,38.0,50.0,45.0,27.0,34.0,52.0,27.0,37.0,33.0,29.0,30.5,17.5,38.0,37.5,31.5,33.0,31.0,30.0,15.7,26.5,24.7,19.0,15.0,19.0,18.5,20.1,28.4,38.5,25.9,29.0,20.5,22.5,20.0,21.4,36.8,24.6,19.5,27.5,20.0,26.2,24.2,44.0,58.0,49.0,49.5,25.2,54.8,48.0,48.0,28.4,24.2,20.5,21.0,22.0,20.5,43.4,14.2,22.2])



n = len(datos)
k = 1 + 3.322 * math.log10(n)
xmin=datos.min()
xmax=datos.max()
rango=xmax-xmin
interv = math.ceil(k)
clase=round(2*math.ceil(rango/interv/2*10)/10,3)
xo = round(xmin-(clase*interv-rango)/2,2)
xf = round(xmax+(clase*interv-rango)/2,2)
intervals=pd.interval_range(start=xo,freq=clase,periods=interv,closed="right") 
intervalo= [pd.Interval(np.round(i.left,2),np.round(i.right,2)) for i in intervals]
df = pd.DataFrame(index=intervalo)
#df["LimInf"] = df.index.left
#df["LimSup"] = df.index.right
df["x"] = df.index.mid
df["F"] = pd.cut(datos, bins=df.index).value_counts()
df["F*"] = df["F"].cumsum()
df["*F"] = df.loc[::-1,"F"].cumsum()[::-1]
df["%f"] = round(df["F"]/n/clase,4)
df["%f*"] = df["%f"].cumsum()
df["*%f"] = df.loc[::-1,"%f"].cumsum()[::-1]

mu=sum(datos)/n
print("mu",mu)
sigma=math.sqrt(sum([(item-mu)**2 for item in datos])/(n-1))
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

xmin=min(datos)
xmax=max(datos)
rang=xmax-xmin
k=math.ceil(1+math.log(n,2))
#binsx=np.linspace(xmin,xmax,k)
#print(binsx)
#df=pd.qcut(x,q=k)
#print(df.value_counts())
#print(df.mind)
print("xmin:",xmin)
print("xmax:",xmax)
print("rang:",rang)

plt.bar(df["x"],df["%f"],width=clase,edgecolor='black')
plt.plot(xrange,y1,color='black')
plt.plot(xrange,y2,color='black')
plt.savefig("figure.jpeg")

print("ANALISIS DE FRECUENCIAS".center(52))
print(df)
print(f"{'datos':.<10} {n:>6}")     
print(f"{'xmin':.<10} {xmin:>6}")        
print(f"{'xmax':.<10} {xmax:>6}")
print(f"{'rango':.<10} {round(rango,2):>6}")

#    print(f"interv:{interv}")
#    print(f"clase:{clase}")
#    print(f"xo:{xo}")
#    print(f"xf:{xf}")
    
'''if __name__ == '__main__':
    datos=np.array([18.0,22.2,27.0,28.3,10.0,38.0,66.4,62.5,24.0,24.0,37.0,20.4,28.4,54.0,40.0,21.0,40.0,38.0,50.0,45.0,27.0,34.0,52.0,27.0,37.0,33.0,29.0,30.5,17.5,38.0,37.5,31.5,33.0,31.0,30.0,15.7,26.5,24.7,19.0,15.0,19.0,18.5,20.1,28.4,38.5,25.9,29.0,20.5,22.5,20.0,21.4,36.8,24.6,19.5,27.5,20.0,26.2,24.2,44.0,58.0,49.0,49.5,25.2,54.8,48.0,48.0,28.4,24.2,20.5,21.0,22.0,20.5,43.4,14.2,22.2])
    statDescrip(datos)'''
