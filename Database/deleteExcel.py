import os
print('estacion:')
estacion=input()
print('numero de hojas')
n=int(input())
for iloop in range(1,n+1):
    os.remove(f'{estacion}{iloop}.xlsx')
