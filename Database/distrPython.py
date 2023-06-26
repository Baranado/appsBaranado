import pandas as pd

from scipy import stats
import sqlite3
conn=sqlite3.connect('dataSenamhi.db')
query='select gestion, max(Precipitación) as Pmax24 from (select gestion,Precipitación from datos where estacion="Tupiza") group by gestion'
df=pd.read_sql_query(query,conn)
mean=df['Pmax24'].mean()
std=df['Pmax24'].std()
#std=var**.5
prob=0.90
x=[]
#"normal"
x.append(stats.norm.ppf(prob,mean,std))
#"lognormal"
x.append(stats.lognorm.ppf(prob,mean,std))
'''
alpha
"alpha"
anglit
"anglit"
arcsine
"arcsine"
argus
"Argus distribution"
beta
"beta"
betaprime
"beta prime"
bradford
"Bradford"
burr
"Burr (Type III)"
burr12
"Burr (Type XII)"
cauchy
"Cauchy"
chi
"chi"
chi2
"chi-squared"
cosine
"cosine"
crystalball
"Crystalball distribution"
dgamma
"double gamma"
dweibull
"double Weibull"
erlang
"Erlang"
expon
"exponential"
exponnorm
"exponentially modified Normal"
exponweib
"exponentiated Weibull"
exponpow
"exponential power"
f
"F"
fatiguelife
"fatigue-life (Birnbaum-Saunders)"
fisk
"Fisk"
foldcauchy
"folded Cauchy"
foldnorm
"folded normal"
genlogistic
"generalized logistic"
gennorm
"generalized normal"
genpareto
"generalized Pareto"
genexpon
"generalized exponential"
genextreme
"generalized extreme value"
gausshyper
"Gauss hypergeometric"
gamma
"gamma"
gengamma
"generalized gamma"
genhalflogistic
"generalized half-logistic"
genhyperbolic
"generalized hyperbolic"
geninvgauss
"Generalized Inverse Gaussian"
gibrat
"Gibrat"
gompertz
"Gompertz (or truncated Gumbel)"
gumbel_r
"right-skewed Gumbel"
gumbel_l
"left-skewed Gumbel"
halfcauchy
"Half-Cauchy"
halflogistic
"half-logistic"
halfnorm
"half-normal"
halfgennorm
"The upper half of a generalized normal"
hypsecant
"hyperbolic secant"
invgamma
"inverted gamma"
invgauss
"inverse Gaussian"
invweibull
"inverted Weibull"
johnsonsb
"Johnson SB"
johnsonsu
"Johnson SU"
kappa4
"Kappa 4 parameter distribution"
kappa3
"Kappa 3 parameter distribution"
ksone
"Kolmogorov-Smirnov one-sided test statistic distributio"
kstwo
"Kolmogorov-Smirnov two-sided test statistic distribution"
kstwobign
"Limiting distribution of scaled Kolmogorov-Smirnov two-sided test statistic"
laplace
"Laplace"
laplace_asymmetric
"asymmetric Laplace"
levy
"Levy"
levy_l
"left-skewed Levy"
levy_stable
"Levy-stable"
logistic
"logistic (or Sech-squared)"
loggamma
"log gamma"
loglaplace
"log-Laplace"
loguniform
"loguniform or reciprocal"
lomax
"Lomax (Pareto of the second kind)"
maxwell
"Maxwell"
mielke
"Mielke Beta-Kappa / Dagum"
moyal
"Moyal"
nakagami
"Nakagami"
ncx2
"non-central chi-squared"
ncf
"non-central F distribution"
nct
"non-central Student's t"
norminvgauss
"Normal Inverse Gaussian"
pareto
"Pareto"
pearson3
"pearson type III"
powerlaw
"power-function"
powerlognorm
"power log-normal"
powernorm
"power normal"
rdist
"R-distributed (symmetric beta)"
rayleigh
"Rayleigh"
rice
"Rice"
recipinvgauss
"reciprocal inverse Gaussian"
semicircular
"semicircular"
skewcauchy
"skewed Cauchy random variable"
skewnorm
"skew-normal random variable"
studentized_range
"studentized range"
t
"Student's t"
trapezoid
"trapezoidal"
triang
"triangular"
truncexpon
"truncated exponential"
truncnorm
"truncated normal"
truncpareto
"upper truncated Pareto"
truncweibull_min
"doubly truncated Weibull minimum"
tukeylambda
"Tukey-Lamdba"
uniform
"uniform"
vonmises
"Von Mises"
vonmises_line
"Von Mises"
wald
"Wald"
weibull_min
"Weibull minimum"
weibull_max
"Weibull maximum"
wrapcauchy
"wrapped Cauchy"'''

print(f'{"Arithmetic mean":.<25} {mean}')
#print(f'{"var":.<25} {var}')
print(f'{"Standard deviation":.<25} {std}')
#print(f'{"skew":.<25} {skew}')
#print(f'{"kurt":.<25} {kurt}')
print("Normal distribution:")
print(x)
