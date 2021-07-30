#%%
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.tools.datetimes import to_datetime

# %%
read_name = '/home/bopanna/Documents/Projects/PythonProjects/Panchangam/Data/Panchangam2020.csv'
save_name = '/home/bopanna/Documents/Projects/PythonProjects/Panchangam/Data/Panchangam2020C.csv'


# %%
df = pd.read_csv(read_name)

# %%
temp = df.columns
import re
temp = [re.sub(r"[\n\t\s]*","",t) for t in temp]
temp

# %%
df.columns = temp
df.to_csv(save_name)

# %%
sunrise = df['Sunrise']
sunrise = [pd.to_datetime(i).time() for i in sunrise]

# %%
sunrise_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in sunrise]

# %%
df['Sunrise'] = sunrise_sec

# %%
df.to_csv(save_name)

# %%
sunset = df['SunSet']

# %%
sunset = [pd.to_datetime(i).time() for i in sunset]

# %%
sunset_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in sunset]

# %%
df['SunSet'] = sunset_sec

# %%
df.to_csv(save_name)

# %%
moonrise = df['Moonrise']
moonrise = [pd.to_datetime(i).time() if i != 'None' else datetime.time(0, 0, 0) for i in moonrise]

moonrise_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in moonrise]

df['Moonrise'] = moonrise_sec
df.to_csv(save_name)

# %%
thiti = df['Tithi']
thiti = [str(t) for t in thiti]

thiti = [t.split(' ',1)[0] for t in thiti]
thiti[:15]
df['Tithi'] = thiti

df.to_csv(save_name)

# %%
nakshatra = df['Nakshatra']
nakshatra = [str(n) for n in nakshatra]
nakshatra = [n.split(" ",1)[0] for n in nakshatra]
nakshatra[:30]
df['Nakshatra'] = nakshatra

df.to_csv(save_name)

# %%
yoga = df['Yoga']
yoga = [str(y).split(' ',1)[0] for y in yoga]
yoga[:15]
df['Yoga'] = yoga
df.to_csv(save_name)

# %%
df.drop('Karana',axis=1,inplace=True)
df.to_csv(save_name)

sun = df['Sun']
sun = [str(s).split(' ',1)[0] for s in sun]
sun[:15]
df['Sun'] = sun
df.to_csv(save_name)

# %%
moon= df['Moon']
moon= [str(s).split(' ',1)[0] for s in moon]
moon[:15]
df['Moon'] = moon
df.to_csv(save_name)

# %%
rahukala = df['Rahukala']
rahukala_start = [str(r).split('-',1)[0] for r in rahukala]
rahukala_end= [str(r).split('-',1)[1] for r in rahukala]
rahukala_start = [pd.to_datetime(t).time() for t in rahukala_start]
rahukala_end = [pd.to_datetime(t).time() for t in rahukala_end]
rahukala_start_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in rahukala_start]
rahukala_end_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in rahukala_end]
df['Rahukala_Start'] = rahukala_start_sec
df['Rahukala_end'] = rahukala_end_sec
df.to_csv(save_name)

# %%
df.drop('FireLocation',axis=1,inplace=True)
df.to_csv(save_name)

# %%
yamaganda= df['Yamaganda']
yamaganda_start = [str(r).split('-',1)[0] for r in yamaganda]
yamaganda_end= [str(r).split('-',1)[1] for r in yamaganda]
yamaganda_start = [pd.to_datetime(t).time() for t in yamaganda_start]
yamaganda_end = [pd.to_datetime(t).time() for t in yamaganda_end]
yamaganda_start_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in yamaganda_start]
yamaganda_end_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in yamaganda_end]
df['Yamaganda_Start'] = yamaganda_start_sec
df['Yamaganda_end'] = yamaganda_end_sec
df.to_csv(save_name)

# %%
gulikai= df['Gulikai']
gulikai_start = [str(r).split('-',1)[0] for r in gulikai]
gulikai_end= [str(r).split('-',1)[1] for r in gulikai]
gulikai_start = [pd.to_datetime(t).time() for t in gulikai_start]
gulikai_end = [pd.to_datetime(t).time() for t in gulikai_end]
gulikai_start_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in gulikai_start]
gulikai_end_sec = [((t.hour * 60 + t.minute) * 60 + t.second) for t in gulikai_end]
df['Gulikai_Start'] = gulikai_start_sec
df['Gulikai_end'] = gulikai_end_sec
df.to_csv(save_name)

# %%
df.drop(['Astha/Udaya','AbhijitMuhurtha','Durmuhurtha','Varjyam','Amritkalam'],axis=1,inplace=True)
df.to_csv(save_name)

# %%
df.drop(['Rahukala','Yamaganda','Gulikai'],axis=1,inplace=True)
df.to_csv(save_name)

# %%
suryaNakshatra= df['SuryaNakshatra']
suryaNakshatra= [str(s).split(' ',1)[0] for s in suryaNakshatra]
suryaNakshatra[:15]
df['SuryaNakshatra'] = suryaNakshatra
df.to_csv(save_name)

# %%
tamilYoga= df['TamilYoga']
tamilYoga= [str(s).split(' ',1)[0] for s in tamilYoga]
tamilYoga[:15]
df['TamilYoga'] = tamilYoga
df.to_csv(save_name)

# %%
anandadiYoga= df['AnandadiYoga']
anandadiYoga= [str(s).split(' ',1)[0] for s in anandadiYoga]
anandadiYoga[:15]
df['AnandadiYoga'] = anandadiYoga
df.to_csv(save_name)