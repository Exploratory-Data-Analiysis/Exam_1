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
    solares detectadas em um período de tiempo.

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
PROM=[]
for i in df["energy.kev"]:
    r=re.findall(r"[\d\.\d]+", i)
    prom=(float(r[0])+float(r[1]))/2
    PROM.append(prom)
df=df.set_index(["duration.s"])
df["Eprom"]=PROM
df2=pd.DataFrame(df,columns=["Eprom"])
plt.figure(figsize=(12,7),dpi=150)
plt.grid()
#df["Eprom"].plot()
#df["duration.s"].plot()
plt.scatter(df2.index,df2["Eprom"])