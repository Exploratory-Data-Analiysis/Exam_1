# Análisis Exploratorio de Datos: Erupciones solares
Este repositorio contiene 3 archivos:
1. Base de datos (.csv) que contine un total de xxxxx filas y xx columnas.
2. Archivo .py con el programa utilizado para analizar la base de datos.
3. Archivo .pdf que contiene el análisis detallado de la base de datos.

Se tiene una base de datos que contiene información sobre 116.143 eventos de erupciones solares registrados entre *Febrero de 2002* y *Marzo de 2018* distribuida en 18 columnas, a continuación se explica de forma breve el contenido de cada columna.
- flare: Número que indifica la erupción solar.
- start.date: Fecha de inicio de la erucpión.
- start.time: Hora de inicio.
- peak: Hora a la que se presenta el máximo.
- end: Hora de finalización
- duration.s: Duración de la erupción.
- peak.c/s: Recuento de picos por segundo	
- total.counts: Recuento total de picos 
- energy.kev: Energía producida por la fulguración (KeV)
- x.pos.asec: La posición X por segundo de arco
- y.pos.asec: La posición Y por segundo de arco
- radial: Unidad em segundo de arco
- active.region.ar: Región activa del Sol 
- flag.1: Código de bandera de la fulguración 1
- flag.2: Código de bandera de la fulguración 2	
- flag.3: Código de bandera de la fulguración 3	
- flag.4: Código de bandera de la fulguración 4	
- flag.5: Código de bandera de la fulguración 5

#### Guia de las flags:

- a0: In attenuator state 0 (None) sometime during flare
- a1: In attenuator state 1 (Thin) sometime during flare
- a2: In attenuator state 2 (Thick) sometime during flare
- a3: In attenuator state 3 (Both) sometime during flare
- An: Attenuator state (0=None, 1=Thin, 2=Thick, 3=Both) at peak of flare
- DF: Front segment counts were decimated sometime during flare
- DR: Rear segment counts were decimated sometime during flare
- ED: Spacecraft eclipse (night) sometime during flare
- EE: Flare ended in spacecraft eclipse (night)
- ES: Flare started in spacecraft eclipse (night)
- FE: Flare ongoing at end of file
- FR: In Fast Rate Mode
- FS: Flare ongoing at start of file
- GD: Data gap during flare
- GE: Flare ended in data gap
- GS: Flare started in data gap
- MR: Spacecraft in high-latitude zone during flare
- NS: Non-solar event
- PE: Particle event: Particles are present
- PS: Possible Solar Flare; in front detectors, but no position
- Pn: Position Quality: P0 = Position is NOT valid, P1 = Position is valid
- Qn: Data Quality: Q0 = Highest Quality, Q11 = Lowest Quality
- SD: Spacecraft was in SAA sometime during flare
- SE: Flare ended when spacecraft was in SAA
- SS: Flare started when spacecraft was in SAA

El objetivo de realizar un análisis exploratorio de datos sobre una base de datos de este tipo es observar si las fulguraciones obedecen algún comportamiento estadístico partícular, además de predecir comportamientos específicos como los picos de emisión o las regiones de mayor de actividad de las fulguraciones. 

## Objetivos observacionales

- Determinar las características de los procesos en los que se libera energía, y localizar donde estos se llevan a cabo.
- Registrar el espectro generado por los iones y electrones acelerados y ver su evolución en el tiempo.
- Determinar la contribución de las partículas de alta energía en las llamaradas solares, mediante la medición de rayos X, rayos gamma y luz visible. 
- Caracterizar el campo magnético y el plasma que se encuentra en la región donde ocurren los procesos no-térmicos.
- Estudiar el comportamiento de las llamaradas leves e intensas. Las similitudes podrían sugerir que todos los todos los procesos osn manifestaciones del mismo fenómeno.
- Encontrar las características de las micro-llamaradas y estimar su contribución al calentamiento de la corona solar.
- Determinar la composición elemental de los iones acelerados y de la atmósfera solar con la que interactúan.

