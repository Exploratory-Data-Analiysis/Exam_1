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

def Filtro(df,col,cond):
    a=df[col] == cond
    dfa=df[a]
    return dfa

format = '%Y-%m-%d%H:%M:%S'
df['Datetime0'] = pd.to_datetime(df['start.date'] + df['start.time'].astype("str")\
  , format=format)
df = df.set_index(['Datetime0'])
del df['start.date']
del df['start.time']
del df['end']
del df['flare']

Emax=[]
Emin=[]
Eprom=[]
for i in df["energy.kev"]:
    r=re.findall(r"[\d\.\d]+", i)
    prom=(float(r[0])+float(r[1]))/2
    Emin.append(float(r[0]))
    Emax.append(float(r[1]))
    Eprom.append(prom)
df["Emin"]=Emin
df["Emax"]=Emax
df["Eprom"]=Eprom
del df["energy.kev"]


# Se hace un filtro para los eventos que tienen un factor de calidad máximo Q1
Q13=df["flag.3"] == "Q1"
Q14=df["flag.4"] == "Q1"
Q15=df["flag.5"] == "Q1"
dfQ1= pd.concat([df[Q13],df[Q14],df[Q15]])
dfQ1= dfQ1.sort_values("Datetime0")

F1 = pd.DataFrame(dfQ1['flag.1'].value_counts(), columns=['flag.1'])
F2 = pd.DataFrame(dfQ1['flag.2'].value_counts(), columns=['flag.2'])
F3 = pd.DataFrame(dfQ1['flag.3'].value_counts(), columns=['flag.3'])
F4 = pd.DataFrame(dfQ1['flag.4'].value_counts(), columns=['flag.4'])
F5 = pd.DataFrame(dfQ1['flag.5'].value_counts(), columns=['flag.5'])
# =============================================================================
# plt.figure(figsize=(12,7),dpi=150)
# F1.plot(kind="bar")
# F2.plot(kind="bar")
# F3.plot(kind="bar")
# F4.plot(kind="bar")
# F5.plot(kind="bar")
# =============================================================================

P12=Filtro(df,"flag.2","P1")
P13=Filtro(df,"flag.3","P1")
P15=Filtro(df,"flag.5","P1")
P1= pd.concat([P12,P13,P15])

#plt.scatter(df["Emax"],df["peak.c/s"])
#sns.kdeplot(df,x="duration.s",y="Emax")
#plt.scatter(dfQ1.index,dfQ1["Emin"],s=0.1,c="b")
plt.xlabel("Duración [s]")
plt.ylabel("Energía máxima [KeV]")

plt.figure(figsize=(12,7),dpi=150)
plt.xlim(-1100,1100)
plt.ylim(-1100,1100)
plt.grid(True)
plt.scatter(dfQ1["x.pos.asec"],dfQ1["y.pos.asec"],s=0.1)

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
