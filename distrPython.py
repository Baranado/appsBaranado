from scipy.stats import norm
x=85
p=0.85
u=70
s=12
p1=norm.cdf(x, loc=u, scale=s)
x1=norm.ppf(p, loc=u, scale=s)
print(f'{"probabilidad normal":.<30}{p1}')
print(f'{"valor de la variable":.<30}{x1}')

