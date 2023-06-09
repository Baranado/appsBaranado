from scipy.optimize import minimize
so1=22907
so2=22522
xo=[100,200,150,100]
def A(x):
    return x[2]*x[1]+x[0]*x[3]
def M(x):
    return x[2]*x[1]**2/2+x[0]*x[3]*(x[1]-x[3]/2)
def c1(x):
    return M(x)/A(x)
def c2(x):
    return x[1]-c1(x)
def I(x):
    return x[2]*x[1]*(x[1]**2/12+(c2(x)-x[1]/2)**2)+x[0]*x[3]*(x[3]**2/12+(c1(x)-x[3]/2)**2)
def s1(x):
    return I(x)/c1(x)
def s2(x):
    return I(x)/c2(x)
def k1(x):
    return s2(x)/A(x)
def k2(x):
    return s1(x)/A(x)
def Q(x):
    return (k1(x)+k2(x))/x[1]

def fun(x):
    return A(x)

def constraint1(x):
    return s1(x)-so1
def constraint2(x):
    return s2(x)-so2
def constraint3(x):
    return 12*x[3]-x[0]
def constraint4(x):
    return 3*x[2]-x[0]
def constraint5(x):
    return 2*x[3]-x[2]
def constraint6(x):
    return x[2]-x[3]

cons1={'type':'ineq','fun':constraint1}
cons2={'type':'ineq','fun':constraint2}
cons3={'type':'ineq','fun':constraint3}
cons4={'type':'ineq','fun':constraint4}
cons5={'type':'ineq','fun':constraint5}
cons6={'type':'ineq','fun':constraint6}
cons=[cons1,cons2,cons3,cons4,cons5,cons6]
bnds=[(10,None),(20,None),(15,None),(10,None)]
sol=minimize(fun,xo,method='trust-constr',constraints=cons,bounds=bnds)
u=sol.x
print(f'fun:\t{-sol.fun}')
print(f'x:\t{u}')
print(f'A:{A(u)}')
print(f'M:{M(u)}')
print(f'c1:{c1(u)}')
print(f'c2:{c2(u)}')
print(f'I:{I(u)}')
print(f's1:{s1(u)}')
print(f's2:{s2(u)}')
print(f'k1:{k1(u)}')
print(f'k2:{k2(u)}')
print(f'Q:{Q(u)}')
print(f'fun:{fun(u)}')

