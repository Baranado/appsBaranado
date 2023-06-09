import scipy.stats as stats
import pandas as pd
norm_data = stats.norm.rvs(size=100,loc=0, scale=1)
norm_fram = pd.DataFrame(norm_data).plot(kind='density')
print(norm_fram)
