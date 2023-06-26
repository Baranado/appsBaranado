import os
import pandas as pd
# folder path
dir_path = r'./'
# list  to store files
dfi = []
# Iterate directory
for file in os.listdir(dir_path):
# check only text files
    if file.endswith('.xlsx'):
        dfi.append(pd.read_excel(file))
        os.remove(file)
df=pd.concat(dfi)
df.to_excel('Senamhi1.xlsx',index=False)
print('concatenate finish')
