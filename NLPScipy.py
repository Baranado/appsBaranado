import numpy as np
from scipy.optimize import minimize
def objetivo(x):
    return 2*x[0]**2+x[1]**2-3*x[0]*x[1]
def restriccion1(x):
    return 2*x[0]-x[1]+1
def restriccion2(x):
    return -x[0]*x[1]+1
def restriccion3(x):
    return x[0]*x[1]*(x[0]+x[1])-2
rest1={'type':'ineq','fun':restriccion1}
rest2={'type':'ineq','fun':restriccion2}
rest3={'type':'eq','fun':restriccion3}
rest=[rest1,rest2,rest3]
xo=np.array([1,1])
sol=minimize(objetivo,xo,constraints=rest,method='trust-constr')
rpta=sol.x
print(f'sol:\t{rpta}')
print(f'z:\t{objetivo(rpta)}')
