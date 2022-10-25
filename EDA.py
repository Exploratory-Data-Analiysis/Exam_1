#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:58:43 2022

    Análisis Exploratorio de datos para una base de datos de las fulguraciones \
    solares detectadas por la misión RHESSI de la NASA entre los años 2002 y\
    2018.

@author: Forero
"""
def Filtro(df,col,cond):
    a=df[col] == cond
    dfa=df[a]
    return dfa

import pandas as pd
import re 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df=pd.read_csv("/home/equipo/Documents/Academic Files/Uniquindio/Semestre 7/Física Computacional/2002to2018.csv")

# Limpieza de la base de datos
    
## Nueva columna (index) Datetime0 y eliminación de otras no tratadas:
format = '%Y-%m-%d%H:%M:%S'
df['Datetime0'] = pd.to_datetime(df['start.date'] + df['start.time'].astype\
  ("str"), format=format)
df = df.set_index(['Datetime0'])
del df['start.date']
del df['start.time']
del df['end']
del df['flare']

df.isnull().any() #Se tiene que solo las 3 últimas colum. tienen datos nulos

## Sustituyendo valores nulos de las flags y creación de nueva columna Flags
df=df.fillna(value="")
df["Flags"]=df["flag.1"]+" "+df["flag.2"]+" "+df["flag.3"]+" "+df["flag.4"]\
+" "+df["flag.5"] 
for i in range (1,6): del df["flag."+str(i)]

## Nuevas columnas Emin, Emax y Eprom:
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

# Explorando la base de datos

## Recuento de los eventos parar diferentes rangos de energía
sns.countplot(x="energy.kev", data=df.sort_values('Eprom'), hue='energy.kev')
plt.legend(title='Rango de energía [KeV]', loc='right', prop={'size': 8})
plt.xlabel('Rango de energía [KeV]', fontsize=16)
plt.ylabel('Frecuencia', fontsize=16)
plt.savefig("G1.png",dpi=300)

## Boxplot de las posiciones x,y
plt.figure(figsize=(4,4), dpi = 150)
sns.boxplot(data=df.sort_values('Eprom'), x='energy.kev', y="x.pos.asec")
plt.ylabel('x [asec]', fontsize=16)
plt.xlabel('Rango de energía [KeV]', fontsize=16)
plt.savefig("G2.png",dpi=300)
plt.figure(figsize=(4,4), dpi = 150)
sns.boxplot(data=df.sort_values('Eprom'), x='energy.kev', y="y.pos.asec")
plt.ylabel('y [asec]', fontsize=16)
plt.xlabel('Rango de energía [KeV]', fontsize=16)
plt.savefig("G3.png",dpi=300)

## Scatter e histograma para las posiciones x,y para diferentes rangos de energía
sns.jointplot(data=df.sort_values('Eprom'), x="x.pos.asec", y="y.pos.asec",\
              hue="energy.kev",xlim=(-1500,1500),ylim=(-1500,1500),height=12)
plt.ylabel('y [asec]', fontsize=16)
plt.xlabel('x [asec]', fontsize=16)
plt.savefig("G4.png",dpi=300)

## Boxplot de la duración de las llamaradas
plt.figure(figsize=(4,4), dpi = 150)
sns.boxplot(data=df.sort_values('Eprom'), x='energy.kev', y="duration.s")
plt.ylabel('Duración [s]', fontsize=16)
plt.xlabel('Rango de energía [KeV]', fontsize=16)
plt.savefig("G5.png",dpi=300)

## Distribución de la duración para diferentes rangos de energías
plt.figure(figsize=(5,5), dpi = 150)
sns.kdeplot(data=df.sort_values('Eprom'), x='duration.s', hue='energy.kev')
plt.xlabel('Duración [s]')
plt.ylabel('Densidad de energía [KeV]')
plt.savefig("G6.png",dpi=300)

## Boxplot y distribución de de log(duration.s) para diferentes rangos de energía
df["duration.sl"]=np.log(df["duration.s"])
plt.figure(figsize=(4,4), dpi = 150)
sns.boxplot(data=df.sort_values('Eprom'), x='energy.kev', y="duration.sl")
plt.ylabel('log(Duración) [asec]', fontsize=16)
plt.xlabel('Rango de energía [KeV]', fontsize=16)
plt.savefig("G7.png",dpi=300)
plt.figure(figsize=(5,5), dpi = 150)
sns.kdeplot(data=df.sort_values('Eprom'), x='duration.sl', hue='energy.kev')
plt.xlabel('log(Duración) [s]')
plt.ylabel('Densidad de energía [KeV]')
plt.savefig("G8.png",dpi=300)

## Filtro para rangos de energías con mayor frecuencia
dfE3_6=Filtro(df,"energy.kev","3-6")
dfE6_12=Filtro(df,"energy.kev","6-12")
dfE12_25=Filtro(df,"energy.kev","12-25")
dfE25_50=Filtro(df,"energy.kev","25-50")
dfE50_100=Filtro(df,"energy.kev","50-100")
dfE100_300=Filtro(df,"energy.kev","100-300")


# =============================================================================
# sns.set_theme(style="ticks")
# g = sns.jointplot(data=df,x="duration.s", y="total.counts",\
#                   hue="energy.kev", kind="kde")
# =============================================================================


# =============================================================================
# df['duration.s.log'] = np.log(df['duration.s'])
# sns.distplot(df['duration.s.log'], bins=80, kde_kws=dict(color='green', lw=3, shade=True),
#              hist_kws=dict(alpha=1, color= 'gold',edgecolor='red', lw=3))
# plt.xlabel('log(Duración) [s]', fontsize=16)
# plt.ylabel('Rango de energía [KeV]', fontsize=16)
# =============================================================================

# =============================================================================
# sns.pairplot(data=dfE6_12, hue='energy.kev',\
#              vars=['duration.s', 'peak.c/s', 'total.counts'])
# sns.pairplot(data=dfE12_25, hue='energy.kev',\
#              vars=['duration.s', 'peak.c/s', 'total.counts'])
# =============================================================================


# Se hace un filtro para los eventos que tienen un factor de calidad máximo Q1
# =============================================================================
# Q13=df["flag.3"] == "Q1"
# Q14=df["flag.4"] == "Q1"
# Q15=df["flag.5"] == "Q1"
# dfQ1= pd.concat([df[Q13],df[Q14],df[Q15]])
# dfQ1= dfQ1.sort_values("Datetime0")

# F1 = pd.DataFrame(dfQ1['flag.1'].value_counts(), columns=['flag.1'])
# F2 = pd.DataFrame(dfQ1['flag.2'].value_counts(), columns=['flag.2'])
# F3 = pd.DataFrame(dfQ1['flag.3'].value_counts(), columns=['flag.3'])
# F4 = pd.DataFrame(dfQ1['flag.4'].value_counts(), columns=['flag.4'])
# F5 = pd.DataFrame(dfQ1['flag.5'].value_counts(), columns=['flag.5']) 
# plt.figure(figsize=(12,7),dpi=150)
# F1.plot(kind="bar")
# F2.plot(kind="bar")
# F3.plot(kind="bar")
# F4.plot(kind="bar")
# F5.plot(kind="bar")
# =============================================================================





#plt.scatter(df["Emax"],df["peak.c/s"])
#sns.kdeplot(df,x="duration.s",y="Emax")
#plt.scatter(dfQ1.index,dfQ1["Emin"],s=0.1,c="b")



# =============================================================================
# plt.xlabel("Duración [s]")
# plt.ylabel("Energía máxima [KeV]")
# 
# plt.figure(figsize=(12,7),dpi=150)
# plt.xlim(-1100,1100)
# plt.ylim(-1100,1100)
# plt.grid(True)
# plt.scatter(dfQ1["x.pos.asec"],dfQ1["y.pos.asec"],s=0.1)
# =============================================================================






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
