import math
import pandas as pd
import scipy.stats as stats
import numpy as np
x=pd.Series([
18.0,22.2,27.0,28.3,10.0,38.0,66.4,62.5,24.0,24.0,
37.0,20.4,28.4,54.0,40.0,21.0,40.0,38.0,50.0,45.0,
27.0,34.0,52.0,27.0,37.0,33.0,29.0,30.5,17.5,38.0,
37.5,31.5,33.0,31.0,30.0,15.7,26.5,24.7,19.0,15.0,
19.0,18.5,20.1,28.4,38.5,25.9,29.0,20.5,22.5,20.0,
21.4,36.8,24.6,19.5,27.5,20.0,26.2,24.2,44.0,58.0,
49.0,49.5,25.2,54.8,48.0,48.0,28.4,24.2,20.5,21.0,
22.0,20.5,43.4,14.2,22.2
])
y=np.log10(x)
prob=.9
n=x.count()
mu=x.mean()
sigma=x.std()
muy=y.mean()
sigmay=y.std()
x1=stats.norm.ppf(prob, mu, sigma)
p1=stats.norm.cdf(x1, mu, sigma)
x2=stats.lognorm.ppf(prob, sigmay)
p2=stats.lognorm.cdf(x2, sigmay)
#print("x:")
#print(x)
print(y)
print(n)
print(f"{'Arithmetic mean':.<30} {mu}")
print(f"{'Arithmetic mean log':.<30} {muy}")
print(f"{'Standard deviation':.<30} {sigma}")
print(f"{'Standard deviation log':.<30} {sigmay}")
print(f"{'Lower tail probability':.<30} {prob}")
print(f"{'Percent point function, Normal':.<30} {x1}")
print(f"{'Cumulative Density Function':.<30} {p1}")
print(f"{'Percent point functi LogNormal':.<30} {x2}")
print(f"{'Cumulative Density Function':.<30} {p2}")
