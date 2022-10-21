#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:31:59 2022

@author: equipo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:58:43 2022

    Análisis Exploratorio de datos para una base de datos de las fulguraciones \
    solares detectadas por la misión RHESSI de la NASA entre los años 2002 y\
    2018.

@author: Forero
"""
import pandas as pd
import re 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/home/equipo/Documents/Academic Files/Uniquindio/Semestre 7/Física Computacional/2002to2018.csv")

format = '%Y-%m-%d%H:%M:%S'
df['Datetime0'] = pd.to_datetime(df['start.date'] + df['start.time'].astype("str")\
  , format=format)
df = df.set_index(['Datetime0'])
del df['start.date']
del df['start.time']

Eprom=[]
for i in df["energy.kev"]:
    r=re.findall(r"[\d\.\d]+", i)
    prom=(float(r[0])+float(r[1]))/2
    Eprom.append(prom)
df["Eprom"]=Eprom

# Se hace un filtro para los eventos que tienen un factor de calidad máximo Q1
Q13=df["flag.3"] == "Q1"
Q14=df["flag.4"] == "Q1"
Q15=df["flag.5"] == "Q1"
dfQ1= pd.concat([df[Q13],df[Q14],df[Q15]])
dfQ1= dfQ1.sort_values("Datetime0")

print(dfQ1['flag.1'].value_counts())
print(dfQ1['flag.2'].value_counts())
plt.figure(figsize=(12,7),dpi=150)
dfQ1["flag.1"].plot.hist()
# =============================================================================
# df2= df.set_index(["Eprom"])
# print(df2)
# plt.figure(figsize=(12,7),dpi=150)
# plt.grid()
# plt.scatter(df2.index,df2["total.counts"])
# =============================================================================

#df1=pd.DataFrame(df,columns=["Eprom"])
#df["duration.s"].plot()
#plt.scatter(df2.index,df2["Eprom"])

# =============================================================================
# =============================================================================
# PS = df['flag.2'] == "PS"
# dfPS = df[PS]
# print(dfPS.head(20))
# =============================================================================
# plt.figure(figsize=(12,7),dpi=150)
# plt.scatter(dfPS.index,dfPS["Eprom"])
# 
# =============================================================================
