import pandas as pd
print('estacion:')
estacion=input()
print('numero de hojas')
n=int(input())
dfi=[]
for iloop in range(1,n+1):
    dfi.append(pd.read_excel(f'{estacion}{iloop}.xlsx'))
df=pd.concat(dfi)
df.to_excel(f'{estacion}.xlsx',index=False)
