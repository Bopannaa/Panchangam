#%%
import numpy as np
import pandas as pd

# %%
first_part = 'https://www.mypanchang.com/caltable.php?cityname=Mysore-Karnataka-India&yr=2021&mn='
second_part = '&monthtype=0'

# %%
links = [first_part + str(i) + second_part for i in range(1,13)]

# %%
dfs = [pd.read_html(link) for link in links]

# %%
dfs = [df[1] for df in dfs]

# %%
for df in dfs:
    df.columns = df.iloc[0]

# %%
for df in dfs:
    df.drop(0,inplace=True)
# %%
df = pd.concat(dfs)
# %%
df.head()
# %%
df.to_csv('/home/bopanna/tempCal.csv')
# %%
