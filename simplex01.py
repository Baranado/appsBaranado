from scipy.optimize import linprog
c = [-5,-2]
A = [[3,2]]
b = [2400]
x0_bounds = (0, 600)
x1_bounds = (0, 800)
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
print('z',res.fun,sep=':')
print('sol',res.x,sep=':')
print(res.message)
