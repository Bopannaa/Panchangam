#%%
import datetime
import numpy as np
import pandas as pd

# %%
year = input('Enter the Year: ')
first_part = 'https://www.mypanchang.com/caltable.php?cityname=Mysore-Karnataka-India&yr='+str(year)+'&mn='
second_part = '&monthtype=0'
output_name = 'Panchanga' + str(year) + '.csv'

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
df.to_csv('/home/bopanna/Documents/Projects/PythonProjects/Panchangam/PanchangaDownloads/'+ output_name)

# %%
df = pd.read_csv('/home/bopanna/Documents/Projects/PythonProjects/Panchangam/PanchangaDownloads/'+ output_name)

# %%
start_date = '01-01-'+ str(year)
end_date = '31-12-'+ str(year)
dates = pd.date_range(start_date, end_date)
df['Date'] = pd.to_datetime(dates)

# %%
df = df.iloc[:,1:]
df = df.set_index('Date')
df.head()

# %%
sunrise = df['Sunrise']
sunrise = [pd.to_datetime(i).time() for i in sunrise]
sunrise = [((t.hour * 60 + t.minute) * 60 + t.second) for t in sunrise]
df['Sunrise'] = sunrise

# %%
sunset = df['SunSet']
sunset = [pd.to_datetime(i).time() for i in sunset]
sunset = [((t.hour * 60 + t.minute) * 60 + t.second) for t in sunset]
df['SunSet'] = sunset

# %%
moonrise = df['Moonrise']
moonrise = [pd.to_datetime(i).time() if i != 'None' else datetime.time(0, 0, 0) for i in moonrise]
moonrise = [((t.hour * 60 + t.minute) * 60 + t.second) for t in moonrise]
df['Moonrise'] = moonrise

# %%
thiti = df['Tithi']
thiti = [str(t).split(' ',1)[0] for t in thiti]
df['Tithi'] = thiti

# %%
nakshatra = df['Nakshatra']
nakshatra = [str(n).split(" ",1)[0] for n in nakshatra]
df['Nakshatra'] = nakshatra

# %%
yoga = df['Yoga']
yoga = [str(y).split(' ',1)[0] for y in yoga]
df['Yoga'] = yoga

# %%
karana = df['Karana']
karana = [str(k).split(' ',1)[0] for k in karana]
df['Karana'] = karana

# %%
sun = df['Sun']
sun = [str(s).split(' ',1)[0] for s in sun]
df['Sun'] = sun

# %%
moon= df['Moon']
moon= [str(s).split(' ',1)[0] for s in moon]
df['Moon'] = moon

# %%
rahukala = df['Rahukala']
rahukala_start = [str(r).split('-',1)[0] for r in rahukala]
rahukala_end= [str(r).split('-',1)[1] for r in rahukala]
rahukala_start = [pd.to_datetime(t).time() for t in rahukala_start]
rahukala_end = [pd.to_datetime(t).time() for t in rahukala_end]
rahukala_start = [((t.hour * 60 + t.minute) * 60 + t.second) for t in rahukala_start]
rahukala_end = [((t.hour * 60 + t.minute) * 60 + t.second) for t in rahukala_end]
df['RahukalaStart'] = rahukala_start
df['RahukalaEnd'] = rahukala_end
df.drop('Rahukala', axis=1, inplace=True)

# %%
yamaganda= df['Yamaganda']
yamaganda_start = [str(r).split('-',1)[0] for r in yamaganda]
yamaganda_end= [str(r).split('-',1)[1] for r in yamaganda]
yamaganda_start = [pd.to_datetime(t).time() for t in yamaganda_start]
yamaganda_end = [pd.to_datetime(t).time() for t in yamaganda_end]
yamaganda_start = [((t.hour * 60 + t.minute) * 60 + t.second) for t in yamaganda_start]
yamaganda_end = [((t.hour * 60 + t.minute) * 60 + t.second) for t in yamaganda_end]
df['YamagandaStart'] = yamaganda_start
df['YamagandaEnd'] = yamaganda_end
df.drop('Yamaganda', axis=1, inplace=True)

# %%
gulikai= df['Gulikai']
gulikai_start = [str(r).split('-',1)[0] for r in gulikai]
gulikai_end= [str(r).split('-',1)[1] for r in gulikai]
gulikai_start = [pd.to_datetime(t).time() for t in gulikai_start]
gulikai_end = [pd.to_datetime(t).time() for t in gulikai_end]
gulikai_start = [((t.hour * 60 + t.minute) * 60 + t.second) for t in gulikai_start]
gulikai_end = [((t.hour * 60 + t.minute) * 60 + t.second) for t in gulikai_end]
df['GulikaiStart'] = gulikai_start
df['GulikaiEnd'] = gulikai_end
df.drop('Gulikai', axis=1, inplace=True)

# %%
abhijit_muhurtha = df['AbhijitMuhurtha']
abhijit_muhurtha_start = [str(i).split('-',1)[0] if i != 'none' else 'none' for i in abhijit_muhurtha]
abhijit_muhurtha_end = [str(i).split('-',1)[1] if i != 'none' else 'none' for i in abhijit_muhurtha]
abhijit_muhurtha_start = [pd.to_datetime(t).time() if t != 'none' else datetime.time(0, 0, 0) for t in abhijit_muhurtha_start]
abhijit_muhurtha_end = [pd.to_datetime(t).time() if t != 'none' else datetime.time(0, 0, 0) for t in abhijit_muhurtha_end]
abhijit_muhurtha_start = [((t.hour * 60 + t.minute) * 60 + t.second) for t in abhijit_muhurtha_start]
abhijit_muhurtha_end = [((t.hour * 60 + t.minute) * 60 + t.second) for t in abhijit_muhurtha_end]
df['AbhijitMuhurthaStart'] = abhijit_muhurtha_start
df['AbhijitMuhurthaEnd'] = abhijit_muhurtha_end
df.drop('AbhijitMuhurtha', axis=1, inplace=True)

# %%
durmuhurtha = df['Durmuhurtha']
durmuhurtha = [i[:17] for i in durmuhurtha]
durmuhurtha_start = [str(r).split('-',1)[0] for r in durmuhurtha]
durmuhurtha_end= [str(r).split('-',1)[1] for r in durmuhurtha]
durmuhurtha_start = [pd.to_datetime(t).time() for t in durmuhurtha_start]
durmuhurtha_end = [pd.to_datetime(t).time() for t in durmuhurtha_end]
durmuhurtha_start = [((t.hour * 60 + t.minute) * 60 + t.second) for t in durmuhurtha_start]
durmuhurtha_end = [((t.hour * 60 + t.minute) * 60 + t.second) for t in durmuhurtha_end]
df['DurmuhurthaStart'] = durmuhurtha_start
df['DurmuhurthaEnd'] = durmuhurtha_end
df.drop('Durmuhurtha', axis=1, inplace=True)

# %%
df.drop(['Varjyam','Amritkalam','Astha/Udaya','Fire Location'], axis=1,inplace=True)

# %%
surya_nakshatra = df['Surya Nakshatra']
surya_nakshatra = [str(k).split(' ',1)[0] for k in surya_nakshatra]
df['Surya Nakshatra'] = surya_nakshatra

# %%
tamil_yoga = df['Tamil Yoga']
tamil_yoga = [str(k).split(' ',1)[0] for k in tamil_yoga]
df['Tamil Yoga'] = tamil_yoga

# %%
anandadi_yoga = df['Anandadi Yoga']
anandadi_yoga = [str(k).split(' ',1)[0] for k in anandadi_yoga]
df['Anandadi Yoga'] = anandadi_yoga

# %%
df.to_csv('/home/bopanna/Documents/Projects/PythonProjects/Panchangam/ModifiedPanchangas/'+ output_name)
# %%