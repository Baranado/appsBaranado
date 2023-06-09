
import math
import numpy as np
import pandas as pd
datos=np.array([94.3,93.0,95.5,95.3,92.4,94.4,92.8,93.2,93.6,95.5,92.9,93.6,95.7,93.8,94.8,93.9,92.7,91.6,93.6,93.7,94.2,95.7,94.7,94.3,92.7,94.5,96.2,95.4,93.7,91.9,94.7,92.7,95.0,93.0,92.9,93.7,92.7,93.3,94.6,96.4,94.1,93.7,94.2,93.7,94.0,93.9,93.6,94.6,92.3,94.4])
print("ANALISIS DE FRECUENCIAS".center(52))
n = len(datos)
k = 1 + 3.322 * math.log10(n)
xmin=datos.min()
xmax=datos.max()
rango=xmax-xmin
interv = math.ceil(k)
clase=2*math.ceil(rango/interv/2*10)/10
xo = xmin-(clase*interv-rango)/2
xf = xmax+(clase*interv-rango)/2
intervals = pd.interval_range(start=xo,freq=clase,periods=interv,closed="right")
df = pd.DataFrame(index=intervals)
#df["LimInf"] = df.index.left
#df["LimSup"] = df.index.right
df["x"] = df.index.mid
df["F"] = pd.cut(datos, bins=df.index).value_counts()
df["F*"] = df["F"].cumsum()
df["*F"] = df.loc[::-1,"F"].cumsum()[::-1] 
df["%f"] = df["F"]*100/n
df["%f*"] = df["%f"].cumsum()
df["*%f"] = df.loc[::-1,"%f"].cumsum()[::-1] 
print(df)
print(f"{'datos':.<10} {n:>6}")
print(f"{'xmin':.<10} {xmin:>6}")
print(f"{'xmax':.<10} {xmax:>6}")   
print(f"{'rango':.<10} {round(rango,2):>6}")
#print(f"interv:{interv}")   
#print(f"clase:{clase}")   
#print(f"xo:{xo}")   
#print(f"xf:{xf}")   
